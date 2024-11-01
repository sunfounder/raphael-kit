#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <stdio.h>

#define SPI_CHANNEL    0           // Define SPI channel (0 or 1)
#define SPI_SPEED      1000000     // SPI speed set to 1 MHz

// Function to write data to a MAX7219 register
void max7219_write(unsigned char address, unsigned char data) {
    unsigned char buffer[2];
    buffer[0] = address;   // Register address to write to
    buffer[1] = data;      // Data to write into the register
    wiringPiSPIDataRW(SPI_CHANNEL, buffer, 2);  // Send data via SPI
}

// Function to initialize the MAX7219 display module
void max7219_init() {
    max7219_write(0x09, 0x00); // Decode Mode: No decoding for digits (useful for 7-segment displays)
    max7219_write(0x0A, 0x03); // Intensity: Set brightness level (0x00 to 0x0F)
    max7219_write(0x0B, 0x07); // Scan Limit: Display digits 0-7 (all 8 digits)
    max7219_write(0x0C, 0x01); // Shutdown Register: Normal operation (not in shutdown mode)
    max7219_write(0x0F, 0x00); // Display Test: Normal operation (no test mode)

    // Clear all digits on the display
    for (int i = 1; i <= 8; i++) {
        max7219_write(i, 0x00); // Write 0 to each digit register
    }
}

// Function to display a pattern on the MAX7219
void max7219_display(unsigned char *data) {
    for (int i = 1; i <= 8; i++) {
        max7219_write(i, data[i - 1]); // Write each row of the pattern to the display
    }
}

// Function to display a pattern for a specified duration
void display_pattern(const unsigned char pattern[8], int delay_ms) {
    max7219_display((unsigned char *)pattern); // Display the pattern
    delay(delay_ms);                           // Wait for the specified time in milliseconds
}

// Array of patterns to display
const unsigned char patterns[][8] = {
    // Square pattern
    {
        0b11111111, // Row 1
        0b10000001, // Row 2
        0b10000001, // Row 3
        0b10000001, // Row 4
        0b10000001, // Row 5
        0b10000001, // Row 6
        0b10000001, // Row 7
        0b11111111  // Row 8
    },
    // Heart pattern
    {
        0b01100110, // Row 1
        0b11111111, // Row 2
        0b11111111, // Row 3
        0b11111111, // Row 4
        0b01111110, // Row 5
        0b00111100, // Row 6
        0b00011000, // Row 7
        0b00000000  // Row 8
    },
    // Number 0
    {
        0b00111100, // Row 1
        0b01100110, // Row 2
        0b11000011, // Row 3
        0b11000011, // Row 4
        0b11000011, // Row 5
        0b11000011, // Row 6
        0b01100110, // Row 7
        0b00111100  // Row 8
    },
    // Number 1
    {
        0b00011000, // Row 1
        0b00111000, // Row 2
        0b01111000, // Row 3
        0b00011000, // Row 4
        0b00011000, // Row 5
        0b00011000, // Row 6
        0b01111110, // Row 7
        0b01111110  // Row 8
    },
    // Number 2
    {
        0b01111110, // Row 1
        0b11000011, // Row 2
        0b00000011, // Row 3
        0b00001110, // Row 4
        0b00110000, // Row 5
        0b11000000, // Row 6
        0b11111111, // Row 7
        0b00000000  // Row 8
    },
    // Number 3
    {
        0b01111110, // Row 1
        0b11000011, // Row 2
        0b00000011, // Row 3
        0b00111110, // Row 4
        0b00000011, // Row 5
        0b11000011, // Row 6
        0b01111110, // Row 7
        0b00000000  // Row 8
    },
    // Number 4
    {
        0b00001110, // Row 1
        0b00011110, // Row 2
        0b00110110, // Row 3
        0b01100110, // Row 4
        0b11111111, // Row 5
        0b00000110, // Row 6
        0b00000110, // Row 7
        0b00000000  // Row 8
    },
    // Number 5
    {
        0b11111111, // Row 1
        0b11000000, // Row 2
        0b11111110, // Row 3
        0b00000011, // Row 4
        0b00000011, // Row 5
        0b11000011, // Row 6
        0b01111110, // Row 7
        0b00000000  // Row 8
    },
    // Number 6
    {
        0b00111110, // Row 1
        0b01100000, // Row 2
        0b11000000, // Row 3
        0b11111110, // Row 4
        0b11000011, // Row 5
        0b11000011, // Row 6
        0b01111110, // Row 7
        0b00000000  // Row 8
    },
    // Number 7
    {
        0b11111111, // Row 1
        0b11000011, // Row 2
        0b00000110, // Row 3
        0b00001100, // Row 4
        0b00011000, // Row 5
        0b00110000, // Row 6
        0b00110000, // Row 7
        0b00000000  // Row 8
    },
    // Number 8
    {
        0b01111110, // Row 1
        0b11000011, // Row 2
        0b11000011, // Row 3
        0b01111110, // Row 4
        0b11000011, // Row 5
        0b11000011, // Row 6
        0b01111110, // Row 7
        0b00000000  // Row 8
    },
    // Number 9
    {
        0b01111110, // Row 1
        0b11000011, // Row 2
        0b11000011, // Row 3
        0b01111111, // Row 4
        0b00000011, // Row 5
        0b00000110, // Row 6
        0b01111100, // Row 7
        0b00000000  // Row 8
    },
};

int main() {
    if (wiringPiSetup() == -1) {
        printf("Failed to initialize WiringPi\n");
        return 1;
    }

    if (wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED) == -1) {
        printf("Failed to initialize SPI\n");
        return 1;
    }

    max7219_init();  // Initialize the MAX7219 module

    // Display patterns in a loop
    while (1) {
        // Display the square pattern
        display_pattern(patterns[0], 1000);  // Display for 1000 milliseconds

        // Display the heart pattern
        display_pattern(patterns[1], 1000);

        // Display numbers 0-9
        for (int i = 2; i <= 11; i++) {
            display_pattern(patterns[i], 1000);
        }
    }

    return 0;
}
