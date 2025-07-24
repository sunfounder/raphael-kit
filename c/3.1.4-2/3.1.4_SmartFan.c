#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>
#include <softPwm.h>
#include <math.h>

#define SPI_CHANNEL 0
#define SPI_SPEED   1000000
#define MotorPin1   21
#define MotorPin2   22
#define MotorEnable 23
#define BtnPin      3

int read_ADC(int channel)
{
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;                      // Start bit
    buffer[1] = (8 + channel) << 4;     // Single-ended mode and channel
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    int result = ((buffer[1] & 3) << 8) | buffer[2];
    return result;
}

int temperture()
{
    int analogVal = read_ADC(0);
    double Vr = 3.3 * analogVal / 1023.0;  // Use 3.3V as Vref for MCP3008
    double Rt = 10000.0 * Vr / (3.3 - Vr);
    double temp = 1 / (((log(Rt / 10000.0)) / 3950.0) + (1 / (273.15 + 25.0)));
    double cel = temp - 273.15;
    double Fah = cel * 1.8 + 32;
    printf("Celsius: %.2f C  Fahrenheit: %.2f F\n", cel, Fah);
    return (int)cel;
}

int motor(int level)
{
    if (level == 0) {
        digitalWrite(MotorEnable, LOW);
        return 0;
    }
    if (level >= 4) {
        level = 4;
    }
    digitalWrite(MotorEnable, HIGH);
    softPwmWrite(MotorPin1, level * 25);
    return level;
}

void setup()
{
    if (wiringPiSetup() == -1) {
        printf("wiringPi setup failed!\n");
        return;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return;
    }

    softPwmCreate(MotorPin1, 0, 100);
    softPwmCreate(MotorPin2, 0, 100);
    pinMode(MotorEnable, OUTPUT);
    pinMode(BtnPin, INPUT);
}

int main(void)
{
    setup();
    int currentState, lastState = 0;
    int level = 0;
    int currentTemp, markTemp = 0;

    while (1) {
        currentState = digitalRead(BtnPin);
        currentTemp = temperture();

        if (currentTemp <= 0) continue;

        if (currentState == 1 && lastState == 0) {
            level = (level + 1) % 5;
            markTemp = currentTemp;
            delay(500);
        }

        lastState = currentState;

        if (level != 0) {
            if (currentTemp - markTemp <= -2) {
                level = level - 1;
                markTemp = currentTemp;
            }
            if (currentTemp - markTemp >= 2) {
                level = level + 1;
                markTemp = currentTemp;
            }
        }

        level = motor(level);
    }

    return 0;
}
