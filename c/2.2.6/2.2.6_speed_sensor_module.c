#include <wiringPi.h>
#include <stdio.h>

#define speedPin		0  // light break pin set to GPIO0
#define Gpin		2
#define Rpin		3

void LED(int color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == 0){
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == 1){
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
}

void Print(int x){
	if ( x == 0 ){
		printf("Light was blocked\n");
	}
}

int main(void){

	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(speedPin, INPUT);
	int temp;
	while(1){
		//Reverse the input of speedPin
		if ( digitalRead(speedPin) == 0 ){  
			temp = 1;
		}
		if ( digitalRead(speedPin) == 1 ){
			temp = 0;
		}

		LED(temp);
		Print(temp);
	}
	return 0;
}




