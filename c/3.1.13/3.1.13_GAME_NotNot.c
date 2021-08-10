#include <bcm2835.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>

#define uchar unsigned char
#define uint unsigned int

#define Max7219_pinCS  RPI_GPIO_P1_24
#define AButtonPin  RPI_GPIO_P1_15
#define BButtonPin  RPI_GPIO_P1_16

int stage = 0;

uchar arrow[2][8]={
{0x18,0x0C,0x06,0xFF,0xFF,0x06,0x0C,0x18},//right
{0x18,0x30,0x60,0xFF,0xFF,0x60,0x30,0x18},//left
};

uchar check[2][8]={
{0x00,0x01,0x02,0x04,0x88,0x50,0x20,0x00},//right
{0x00,0x42,0x24,0x18,0x18,0x24,0x42,0x00},//wrong
};

void Delay_xms(uint x)
{
	bcm2835_delay(x);
}

void Write_Max7219_byte(uchar DATA)
{
	bcm2835_gpio_write(Max7219_pinCS,LOW);
	bcm2835_spi_transfer(DATA);
}

void Write_Max7219(uchar address1,uchar dat1)
{
	bcm2835_gpio_write(Max7219_pinCS,LOW);
	Write_Max7219_byte(address1);
	Write_Max7219_byte(dat1); 
	bcm2835_gpio_write(Max7219_pinCS,HIGH);
}

void Init_MAX7219()
{
	Write_Max7219(0x09,0x00);
	Write_Max7219(0x0a,0x03);
	Write_Max7219(0x0b,0x07);
	Write_Max7219(0x0c,0x01);
	Write_Max7219(0x0f,0x00);
}

void Init_BCM2835()
{
	bcm2835_spi_begin();
	bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);
	bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);
	bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_256);
	bcm2835_gpio_fsel(Max7219_pinCS, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(AButtonPin, BCM2835_GPIO_FSEL_INPT);
	bcm2835_gpio_set_pud(AButtonPin, BCM2835_GPIO_PUD_UP);
	bcm2835_gpio_fsel(BButtonPin, BCM2835_GPIO_FSEL_INPT);
	bcm2835_gpio_set_pud(BButtonPin, BCM2835_GPIO_PUD_UP);
	bcm2835_gpio_write(arrow[0][0],HIGH);
}

int get_index()
{
	srand((unsigned)time(NULL));
	return rand()%2;
}

int get_key(uint num)
{
	while (1)
	{
		if (1 == bcm2835_gpio_lev(AButtonPin) && num == 0){
			return 1;
		}
		else if (1 == bcm2835_gpio_lev(BButtonPin) && num == 1){
			return 1;
		}
		else if (1 == bcm2835_gpio_lev(AButtonPin) && num == 1){
			return 0;
		}
		else if (1 == bcm2835_gpio_lev(BButtonPin) && num == 0){
			return 0;
		}
	}
}

void display(uint index){
	uchar i;
	if (stage == 0){
		for(i=1;i<9;i++)
        {
            Write_Max7219(i,arrow[index][i-1]);
        }
	}
	else if(stage == 1){
		for(i=1;i<9;i++)
        {
            Write_Max7219(i,check[index][i-1]);
        }
	}
}

int main(void)
{
	uint direction,key;

	if (!bcm2835_init())
	{
		printf("Unable to init bcm2835.\n");
		return 1;
	}
	Init_BCM2835();
	Delay_xms(50);
	Init_MAX7219();

	while(1)
	{
        if (stage == 0)
        {
            direction = get_index();
            display(direction);
			stage = 1;
        }
        else if(stage == 1)
        {
            key = get_key(direction);
            display(key);
			Delay_xms(1000);
			stage = 0;
        }
    }
	// bcm2835_spi_end();
	// bcm2835_close();
	return 0;
}
