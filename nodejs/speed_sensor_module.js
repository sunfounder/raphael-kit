
const Gpio = require('pigpio').Gpio;


const Rpin = new Gpio(22, { mode: Gpio.OUTPUT });
const Gpin = new Gpio(27, { mode: Gpio.OUTPUT });

const speedPin = new Gpio(17, {
    mode: Gpio.INPUT,
    pullUpDown: Gpio.PUD_DOWN,     
    edge: Gpio.EITHER_EDGE        
});

speedPin.on('interrupt', (level) => {
    if (level) {
        console.log("Light was blocked");
    }
    Rpin.digitalWrite(level);
    Gpin.digitalWrite(!level);
});

process.on('SIGINT', function () {
    Rpin.digitalWrite(0);
    Gpin.digitalWrite(0);
    process.exit();
});