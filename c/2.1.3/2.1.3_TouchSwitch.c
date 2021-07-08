/**********************************************************************
* Filename    : 2.1.2_TravelSwitch.c
* Description : Make a touch switch to contral which led on
* Author      : sunfounder
* E-mail      : support@sunfounder.com
* website     : www.sunfounder.com
* Update      : 2021/05/27
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define touchPin		0
#define led1			3
#define led2 			2

int main(void)
{
	// When initialize wiring failed, print message to screen
	if(wiringPiSetup() == -1){
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(touchPin, INPUT);
	pinMode(led1, OUTPUT);
	pinMode(led2, OUTPUT);
	
	while(1){
		// touch switch high, led1 on
		if(digitalRead(touchPin) == 1){
			digitalWrite(led1, LOW);
			digitalWrite(led2, HIGH);
			printf("You touch it! \r\n");
		}
		// touch switch low, led2 on
		if(digitalRead(touchPin) == 0){
			digitalWrite(led2, LOW);
			digitalWrite(led1, HIGH);
		}
	}

	return 0;
}




