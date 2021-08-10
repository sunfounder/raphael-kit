#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#define  clkPin    0
#define  dtPin    1
#define  swPin     2

static volatile int globalCounter = 0 ;

unsigned char flag;
unsigned char Last_dtPin_Status;
unsigned char Current_dtPin_Status;

void btnISR(void)
{
   globalCounter = 0;
}

void rotaryDeal(void)
{
   Last_dtPin_Status = digitalRead(dtPin);

   while(!digitalRead(clkPin)){
      Current_dtPin_Status = digitalRead(dtPin);
      flag = 1;
   }

   if(flag == 1){
      flag = 0;
      if((Last_dtPin_Status == 0)&&(Current_dtPin_Status == 1)){
         globalCounter --;
      }
      if((Last_dtPin_Status == 1)&&(Current_dtPin_Status == 0)){
         globalCounter ++;
      }
   }
}

int main(void)
{
   if(wiringPiSetup() < 0){
      fprintf(stderr, "Unable to setup wiringPi:%s\n",strerror(errno));
      return 1;
   }

   pinMode(swPin, INPUT);
   pinMode(clkPin, INPUT);
   pinMode(dtPin, INPUT);

   pullUpDnControl(swPin, PUD_UP);

   if(wiringPiISR(swPin, INT_EDGE_FALLING, &btnISR) < 0){
      fprintf(stderr, "Unable to init ISR\n",strerror(errno));
      return 1;
   }

   int tmp = 0;

   while(1){
      rotaryDeal();
      if (tmp != globalCounter){
         printf("%d\n", globalCounter);
         tmp = globalCounter;
      }
   }

   return 0;
}