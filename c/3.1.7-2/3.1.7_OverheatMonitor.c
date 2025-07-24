#include <wiringPi.h>
#include <stdio.h>
#include <wiringPiI2C.h>
#include <wiringPiSPI.h>
#include <string.h>
#include <math.h>

typedef unsigned char uchar;
typedef unsigned int  uint;

#define Joy_BtnPin 3      // GPIO22 -> WiringPi 3
#define buzzPin    4      // GPIO23 -> WiringPi 4
#define LedPin     5      // GPIO24 -> WiringPi 5
#define SPI_CHANNEL 0
#define SPI_SPEED   1000000

int LCDAddr    = 0x27;
int BLEN       = 1;
int fd;
int upperTem   = 40;

// Global variable to store the last joystick change
int lastJoystickChange = 0;

int read_ADC(int channel) {
    if (channel < 0 || channel > 7) return -1;
    unsigned char buffer[3];
    buffer[0] = 1;
    buffer[1] = (8 + channel) << 4;
    buffer[2] = 0;
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);
    return ((buffer[1] & 0x03) << 8) | buffer[2];
}

void write_word(int data){
    int temp = data;
    if (BLEN)      temp |= 0x08;
    else           temp &= 0xF7;
    wiringPiI2CWrite(fd, temp);
}

void send_command(int comm){
    int buf = comm & 0xF0;
    buf |= 0x04; write_word(buf); delay(2); buf &= 0xFB; write_word(buf);
    buf = (comm & 0x0F) << 4;
    buf |= 0x04; write_word(buf); delay(2); buf &= 0xFB; write_word(buf);
}

void send_data(int data){
    int buf = data & 0xF0;
    buf |= 0x05; write_word(buf); delay(2); buf &= 0xFB; write_word(buf);
    buf = (data & 0x0F) << 4;
    buf |= 0x05; write_word(buf); delay(2); buf &= 0xFB; write_word(buf);
}

void lcd_init(){
    send_command(0x33); delay(5);
    send_command(0x32); delay(5);
    send_command(0x28); delay(5);
    send_command(0x0C); delay(5);
    send_command(0x01); wiringPiI2CWrite(fd, 0x08);
}

void lcd_clear(){
    send_command(0x01);
}

void write_lcd(int x, int y, const char data[]){
    int addr = 0x80 + 0x40 * y + x;
    send_command(addr);
    for (int i = 0; i < (int)strlen(data); i++)
        send_data(data[i]);
}

int get_joystick_value(){
    int x = read_ADC(1);
    int y = read_ADC(2);

    // Dead-band filtering to reduce small fluctuations
    if (x > 900)      return  1;   // 右
    else if (x < 100) return -1;   // 左
    else if (y > 900) return -10;  // 上
    else if (y < 100) return  10;  // 下
    else              return   0; 
}

void upper_tem_setting(){
    write_lcd(0,0, "Upper Adjust:");

    int change = get_joystick_value();

    // Only respond to actual direction change
    if (change != 0 && change != lastJoystickChange) {
        upperTem += change;
        lastJoystickChange = change;
    }
    else if (change == 0) {
        // Allow next change after returning to center
        lastJoystickChange = 0;
    }

    // Display current upperTem
    char str[6];
    snprintf(str, sizeof(str), "%d", upperTem);
    write_lcd(0,1, str);
    // Clear remaining LCD characters
    write_lcd(strlen(str),1, "            ");

    delay(100);
}

double temperature(){
    int raw = read_ADC(0);
    double Vr = 3.3 * ((double)raw / 1023.0);
    double Rt = 10000.0 * Vr / (3.3 - Vr);
    double tempK = 1.0 / ((log(Rt/10000.0)/3950.0) + 1.0/(273.15+25.0));
    return tempK - 273.15;
}

void monitoring_temp(){
    char str[6];
    double cel = temperature();
    snprintf(str, sizeof(str), "%.2f", cel);
    write_lcd(0,0, "Temp: ");
    write_lcd(6,0, str);

    snprintf(str, sizeof(str), "%d", upperTem);
    write_lcd(0,1, "Upper: ");
    write_lcd(7,1, str);
    delay(100);

    if (cel >= upperTem) {
        digitalWrite(buzzPin, HIGH);
        digitalWrite(LedPin,  HIGH);
    } else {
        digitalWrite(buzzPin, LOW);
        digitalWrite(LedPin,  LOW);
    }
}

void setup_all(){
    fd = wiringPiI2CSetup(LCDAddr);
    lcd_init();
    if (wiringPiSetup() == -1 ||
        wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("Setup failed!\n");
        return;
    }
    pinMode(Joy_BtnPin, INPUT);
    pullUpDnControl(Joy_BtnPin, PUD_UP);
    pinMode(buzzPin, OUTPUT);
    pinMode(LedPin,  OUTPUT);
}

int main(void){
    setup_all();

    int lastBtnState = HIGH;
    int stage = 0;

    while (1) {
        int curBtn = digitalRead(Joy_BtnPin);
        // Switch mode when button changes from LOW to HIGH (button released)
        if (curBtn == HIGH && lastBtnState == LOW) {
            stage = (stage + 1) % 2;
            lastJoystickChange = 0;  // Clear debounce status
            delay(100);
            lcd_clear();
        }
        lastBtnState = curBtn;

        if (stage == 1)
            upper_tem_setting();
        else
            monitoring_temp();
    }

    return 0;
}
