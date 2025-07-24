const Gpio = require('pigpio').Gpio;
const mcpadc = require('mcp-spi-adc');

// Open channel 1 (X-axis)
const xChannel = mcpadc.openMcp3008(1, { speedHz: 1350000 }, (err) => {
  if (err) {
    console.error('Failed to open X channel:', err);
    process.exit(1);
  }
});

// Open channel 2 (Y-axis)
const yChannel = mcpadc.openMcp3008(2, { speedHz: 1350000 }, (err) => {
  if (err) {
    console.error('Failed to open Y channel:', err);
    process.exit(1);
  }
});

// Button input on GPIO22 with pull-up
const btn = new Gpio(22, {
  mode: Gpio.INPUT,
  pullUpDown: Gpio.PUD_UP,
});

// Read loop
setInterval(() => {
  xChannel.read((errX, xReading) => {
    if (errX) {
      console.error('X channel read error:', errX);
      return;
    }

    yChannel.read((errY, yReading) => {
      if (errY) {
        console.error('Y channel read error:', errY);
        return;
      }

      const x_val = Math.round(xReading.value * 1023);
      const y_val = Math.round(yReading.value * 1023);
      const btn_val = btn.digitalRead();

      console.log(`x = ${x_val}, y = ${y_val}, btn = ${btn_val}\n`);
    });
  });
}, 100);
