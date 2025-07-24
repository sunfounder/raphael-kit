#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED   1000000  // 1 MHz
#define BtnPin      3        // WiringPi 3 = BCM GPIO22

// Read from MCP3008 channel (0¨C7)
int read_ADC(int channel) {
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;                            // Start bit
    buffer[1] = (8 + channel) << 4;           // Channel config
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    int result = ((buffer[1] & 0x03) << 8) | buffer[2];
    return result;
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("WiringPi setup failed!\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return 1;
    }

    pinMode(BtnPin, INPUT);
    pullUpDnControl(BtnPin, PUD_UP);

    while (1) {
        int x_val = read_ADC(0);     // VRX on CH0
        int y_val = read_ADC(1);     // VRY on CH1
        int btn_val = digitalRead(BtnPin);  // SW button

        printf("x = %d, y = %d, btn = %d\n", x_val, y_val, btn_val);
        delay(100);
    }

    return 0;
}
