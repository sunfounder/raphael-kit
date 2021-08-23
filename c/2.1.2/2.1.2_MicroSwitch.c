/**********************************************************************
* Filename    : 2.1.2_MicroSwitch.c
* Description : 
* Author      : sunfounder
* E-mail      : support@sunfounder.com
* website     : www.sunfounder.com
* Update      : 2021/05/27
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>

#define microPin		0
#define led1			3
#define led2 			2

int main(void)
{
	// When initialize wiring failed, print message to screen
	if(wiringPiSetup() == -1){
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(microPin, INPUT);
	pinMode(led1, OUTPUT);
	pinMode(led2, OUTPUT);
	
	while(1){
		// micro switch high, led1 on
		if(digitalRead(microPin) == 1){
			digitalWrite(led1, LOW);
			digitalWrite(led2, HIGH);
			printf("LED1 on\n");
		}
		// micro switch low, led2 on
		if(digitalRead(microPin) == 0){
			digitalWrite(led2, LOW);
			digitalWrite(led1, HIGH);
			printf(".....LED2 on\n");
		}
		delay(500);
	}

	return 0;
}


