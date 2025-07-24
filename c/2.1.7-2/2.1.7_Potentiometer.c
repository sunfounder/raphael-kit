#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>
#include <softPwm.h>

#define SPI_CHANNEL 0  // CE0
#define SPI_SPEED   1000000  // 1MHz
#define LedPin      3

int readADC(int channel) {
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;                             // Start bit
    buffer[1] = (8 + channel) << 4;            // Single-ended mode, channel
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    int value = ((buffer[1] & 3) << 8) | buffer[2];
    return value;
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("WiringPi init failed!\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return 1;
    }

    softPwmCreate(LedPin, 0, 100);

    while (1) {
        int analogVal = readADC(0);  // CH0
        printf("ADC Value: %d\n", analogVal);

        int pwmVal = analogVal * 100 / 1023;  // Normalize to 0–100
        softPwmWrite(LedPin, pwmVal);

        delay(100);
    }

    return 0;
}
