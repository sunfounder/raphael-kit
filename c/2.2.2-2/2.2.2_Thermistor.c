#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>
#include <math.h>

#define SPI_CHANNEL 0  // CE0
#define SPI_SPEED   1000000  // 1MHz

int read_ADC(int channel) {
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;  // Start bit
    buffer[1] = (8 + channel) << 4;  // Single-ended mode + channel
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    int value = ((buffer[1] & 3) << 8) | buffer[2];
    return value;
}

int main(void) {
    int analogVal;
    double Vr, Rt, temp, cel, Fah;

    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed!\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return 1;
    }

    while (1) {
        analogVal = read_ADC(0);  // Read from CH0

        // MCP3008 is 10-bit ADC (0–1023)
        Vr = 3.3 * analogVal / 1023.0;  // Assume Vref = 3.3V
        Rt = 10000.0 * Vr / (3.3 - Vr); // Voltage divider, 10k resistor
        temp = 1 / ((log(Rt / 10000.0) / 3950.0) + (1 / (273.15 + 25.0)));
        cel = temp - 273.15;
        Fah = cel * 1.8 + 32;

        printf("Celsius: %.2f C  Fahrenheit: %.2f F\n", cel, Fah);
        delay(1000);
    }

    return 0;
}

