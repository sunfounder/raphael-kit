const mcpadc = require('mcp-spi-adc');

// Open MCP3008 channel 0 (CH0), analog input from thermistor voltage divider
const adc = mcpadc.openMcp3008(0, { speedHz: 1350000 }, (err) => {
  if (err) {
    console.error('Failed to open MCP3008 channel:', err);
    process.exit(1);
  }

  console.log('MCP3008 thermistor channel opened.');

  setInterval(() => {
    adc.read((err, reading) => {
      if (err) {
        console.error('ADC read error:', err);
        return;
      }

      const adcValue = reading.value; // Float: 0.0–1.0
      const raw = Math.round(adcValue * 1023); // 10-bit integer value

      const Vr = 3.3 * raw / 1023; // Convert to voltage (assuming 3.3V Vref)
      const R0 = 10000;            // Fixed resistor: 10k
      const B = 3950;              // B constant
      const Rt = R0 * Vr / (3.3 - Vr); // Thermistor resistance

      const tempK = 1 / ((Math.log(Rt / R0) / B) + (1 / (273.15 + 25))); // Kelvin
      const tempC = tempK - 273.15; // Celsius
      const tempF = tempC * 1.8 + 32; // Fahrenheit

      console.log(`Celsius: ${tempC.toFixed(2)} °C  |  Fahrenheit: ${tempF.toFixed(2)} °F`);
    });
  }, 1000);
});
