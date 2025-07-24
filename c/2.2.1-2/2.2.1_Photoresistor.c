#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>
#include <softPwm.h>

#define SPI_CHANNEL 0      // Use SPI channel 0 (CE0)
#define SPI_SPEED   1000000 // 1 MHz SPI speed
#define LedPin      3       // GPIO3 (WiringPi) for LED PWM

// Read ADC value from MCP3008, channel 0~7
int readMCP3008(int channel) {
    if (channel < 0 || channel > 7) return -1;

    unsigned char buffer[3];
    buffer[0] = 1;                          // Start bit
    buffer[1] = (8 + channel) << 4;         // SGL/DIF = 1, D2-D0 = channel
    buffer[2] = 0;

    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 3);

    // Combine the result
    int result = ((buffer[1] & 3) << 8) | buffer[2];
    return result;
}

int main(void) {
    if (wiringPiSetup() == -1) {
        printf("wiringPi init failed!\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("SPI setup failed!\n");
        return 1;
    }

    softPwmCreate(LedPin, 0, 100); // Init software PWM

    while (1) {
        int analogVal = readMCP3008(0); // Read from CH0
        printf("ADC Value: %d\n", analogVal);

        // Scale 10-bit ADC value (0¨C1023) to PWM range (0¨C100)
        int pwmVal = analogVal * 100 / 1023;
        softPwmWrite(LedPin, pwmVal);

        delay(100);
    }

    return 0;
}
