const Gpio = require('pigpio').Gpio;
const mcpadc = require('mcp-spi-adc');

// Open MCP3008 channel 0 (analog input CH0)
const adc = mcpadc.openMcp3008(0, { speedHz: 1000000 }, (err) => {
  if (err) {
    console.error("Failed to open ADC channel:", err);
    process.exit(1);
  }

  console.log("MCP3008 channel 0 opened successfully.");

  // Initialize LED on GPIO22 with PWM output mode
  const led = new Gpio(22, { mode: Gpio.OUTPUT });

  // Read ADC value every 100ms and update LED brightness
  setInterval(() => {
    adc.read((err, reading) => {
      if (err) {
        console.error("Error reading ADC:", err);
        return;
      }

      // Convert floating-point value (0.0–1.0) to PWM range (0–255)
      const pwmVal = Math.round(reading.value * 255);

      console.log(`Current analogVal: ${pwmVal}`);

      // Update LED brightness using PWM
      led.pwmWrite(pwmVal);
    });
  }, 100);
});
