const Gpio = require('pigpio').Gpio; 

const ir_ob = new Gpio(17, {
  mode: Gpio.INPUT,
  pullUpDown: Gpio.PUD_DOWN,     
  edge: Gpio.FALLING_EDGE        
});

ir_ob.on('interrupt', () => {  
  console.log('Detected Barrier!');        
});


