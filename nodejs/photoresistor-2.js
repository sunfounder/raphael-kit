const Gpio = require('pigpio').Gpio;
const mcpadc = require('mcp-spi-adc');

// Open MCP3008 channel 0 (analog input CH0)
const adc = mcpadc.openMcp3008(0, { speedHz: 1350000 }, (err) => {
  if (err) {
    console.error("Failed to open MCP3008:", err);
    process.exit(1);
  }

  console.log("MCP3008 initialized on SPI0/CE0.");

  // Initialize LED on GPIO22 (PWM capable)
  const led = new Gpio(22, { mode: Gpio.OUTPUT });

  // Set up interval to read ADC and update LED brightness every 100ms
  const interval = setInterval(() => {
    adc.read((err, reading) => {
      if (err) {
        console.error("ADC read error:", err);
        return;
      }

      const adcValue = reading.value;          // Float between 0.0 and 1.0
      const pwmValue = Math.round(adcValue * 255); // Scale to 0–255

      console.log(`ADC = ${adcValue.toFixed(4)}, PWM = ${pwmValue}`);

      led.pwmWrite(pwmValue); // Update LED brightness
    });
  }, 100);

  // Handle Ctrl+C (SIGINT) to clean up
  process.on('SIGINT', () => {
    console.log('\nGracefully shutting down...');
    clearInterval(interval);  // Stop the interval loop
    led.digitalWrite(0);      // Turn off LED
    process.exit(0);
  });
});
