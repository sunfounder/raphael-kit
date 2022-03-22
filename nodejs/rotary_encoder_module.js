const Gpio = require('pigpio').Gpio;

const clkPin = new Gpio(17, {
   mode: Gpio.INPUT,
   pullUpDown: Gpio.PUD_DOWN,
   edge: Gpio.RISING_EDGE
});
const dtPin = new Gpio(18, {
   mode: Gpio.INPUT,
   pullUpDown: Gpio.PUD_DOWN,    
   //  edge: Gpio.EITHER_EDGE   
});
const swPin = new Gpio(27, {
   mode: Gpio.INPUT,
   pullUpDown: Gpio.PUD_UP,
   edge: Gpio.FALLING_EDGE
});

var globalCounter = 0;

clkPin.on('interrupt',()=>{
   if(dtPin.digitalRead()==1){
      globalCounter--;
   }
   else{
      globalCounter++;
   }
   console.log(`globalCounter = ${globalCounter}`);
});

swPin.on('interrupt', () => {
   globalCounter = 0;
   console.log(`globalCounter = ${globalCounter}`);
});
