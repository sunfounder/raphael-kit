#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL 0
#define SPI_SPEED   1000000  // 1MHz
#define VREF        3.3      

int pins[10] = {6, 26, 27, 28, 29, 21, 22, 23, 24, 25};

int read_ADC(int channel)
{
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;  // Start bit
    buffer[1] = (8 + channel) << 4;  // Single-ended mode
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    int value = ((buffer[1] & 3) << 8) | buffer[2];
    return value;
}

void LedBarGraph(int value) {
    for (int i = 0; i < 10; i++) {
        if (i < value)
        digitalWrite(pins[i], HIGH);  
    else
        digitalWrite(pins[i],LOW);
    }
}

int main(void)
{
    if (wiringPiSetup() == -1) {
        printf("setup wiringPi failed!\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        pinMode(pins[i], OUTPUT);
        digitalWrite(pins[i], HIGH);
    }

    while (1) {
        int analogVal = read_ADC(0);  // MCP3008 CH0
        if (analogVal < 0) continue;


        float voltage = analogVal * VREF / 1023.0;
        int level = analogVal * 10 / 1024;  
        if (level > 10) level = 10;  

        LedBarGraph(level);

        printf("ADC Value: %d\tVoltage: %.2f V\tLevel: %d\n", analogVal, voltage, level);

        delay(200);
    }

    return 0;
}
