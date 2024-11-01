#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define uchar unsigned char
#define uint unsigned int

#define SPI_CHANNEL    0
#define SPI_SPEED      1000000  // 1 MHz

#define AButtonPin     3   // WiringPi pin 3 (GPIO 22)
#define BButtonPin     4   // WiringPi pin 4 (GPIO 23)

int stage = 0;

uchar arrow[2][8]={
    {0x18,0x0C,0x06,0xFF,0xFF,0x06,0x0C,0x18},// Right arrow
    {0x18,0x30,0x60,0xFF,0xFF,0x60,0x30,0x18},// Left arrow
};

uchar check[2][8]={
    {0x00,0x01,0x02,0x04,0x88,0x50,0x20,0x00},// Correct symbol
    {0x00,0x42,0x24,0x18,0x18,0x24,0x42,0x00},// Incorrect symbol
};

void Delay_xms(uint x)
{
    delay(x);
}

void Write_Max7219_byte(uchar DATA)
{
    wiringPiSPIDataRW(SPI_CHANNEL, &DATA, 1);
}

void Write_Max7219(uchar address1, uchar dat1)
{
    uchar buffer[2];
    buffer[0] = address1;
    buffer[1] = dat1;
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);
}

void Init_MAX7219()
{
    Write_Max7219(0x09, 0x00); // Decode Mode: No decode
    Write_Max7219(0x0A, 0x03); // Intensity: 3 (0x00 to 0x0F)
    Write_Max7219(0x0B, 0x07); // Scan Limit: Display digits 0-7
    Write_Max7219(0x0C, 0x01); // Shutdown Register: Normal operation
    Write_Max7219(0x0F, 0x00); // Display Test: Off
}

void Init_WiringPi()
{
    if (wiringPiSetup() == -1)
    {
        printf("Failed to initialize WiringPi\n");
        exit(1);
    }

    // Initialize SPI interface
    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1)
    {
        printf("Failed to initialize SPI\n");
        exit(1);
    }

    // Setup button pins
    pinMode(AButtonPin, INPUT);
    pullUpDnControl(AButtonPin, PUD_UP);

    pinMode(BButtonPin, INPUT);
    pullUpDnControl(BButtonPin, PUD_UP);
}

int get_index()
{
    return rand() % 2; // Generate random index 0 or 1
}

int get_key(uint num)
{
    while (1)
    {
        if (digitalRead(AButtonPin) == LOW)
        {
            if (num == 0)
                return 1; // Correct if arrow points right and A button pressed
            else
                return 0; // Incorrect if arrow points left and A button pressed
        }
        else if (digitalRead(BButtonPin) == LOW)
        {
            if (num == 1)
                return 1; // Correct if arrow points left and B button pressed
            else
                return 0; // Incorrect if arrow points right and B button pressed
        }
    }
}

void display(uint index)
{
    uchar i;
    if (stage == 0)
    {
        // Display arrow
        for (i = 1; i <= 8; i++)
        {
            Write_Max7219(i, arrow[index][i - 1]);
        }
    }
    else if (stage == 1)
    {
        // Display check mark or cross
        for (i = 1; i <= 8; i++)
        {
            Write_Max7219(i, check[index][i - 1]);
        }
    }
}

int main(void)
{
    uint direction, key;

    srand((unsigned)time(NULL)); // Seed random number generator

    Init_WiringPi();
    Delay_xms(50);
    Init_MAX7219();

    while (1)
    {
        if (stage == 0)
        {
            direction = get_index(); // Get random direction
            display(direction);      // Display arrow
            stage = 1;
        }
        else if (stage == 1)
        {
            key = get_key(direction); // Wait for user input
            display(key);             // Display result (correct/incorrect)
            Delay_xms(1000);          // Wait for a second
            stage = 0;
        }
    }

    return 0;
}
