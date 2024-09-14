# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time

project = 'SunFounder Ulimate Raphael Kit for Raspberry Pi'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# SunFounder logo

#html_js_files = [
#    'https://ezblock.cc/readDocFile/custom.js',
#]
#html_css_files = [
#    'https://ezblock.cc/readDocFile/custom.css',
#]

#### RTD+

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    './lang.js', # new
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ext-language_tools.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/theme-chrome.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',

]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]



# Multi-language

language = 'en' # Before running make html, set the language.
locale_dirs = ['locale/'] # .po files for other languages are placed in the locale/ folder.

gettext_compact = False # Support for generating the contents of the folders inside source/ into other languages.


# Purchase links of components
rst_epilog = """

.. |link_Raphael_kit| raw:: html

    <a href="https://www.sunfounder.com/products/raphael-kit?_pos=1&_sid=e78196ab0&_ss=r" target="_blank">Raphael Kit</a>

.. |link_picow_buy| raw:: html

    <a href="https://www.sunfounder.com/products/raspberry-pi-pico-w" target="_blank">BUY</a>
    
.. |link_led_buy| raw:: html

    <a href="https://www.sunfounder.com/products/500pcs-5-colors-x-100pcs-5mm-leds-with-white-red-yellow-green-blue-colors-kit-box" target="_blank">BUY</a>

.. |link_resistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/1-4w-resistor-assortment-kit-40-values-400pcs" target="_blank">BUY</a>

.. |link_wires_buy| raw:: html

    <a href="https://www.sunfounder.com/products/560pcs-jumper-wire-kit-with-14-lengths" target="_blank">BUY</a>

.. |link_breadboard_buy| raw:: html

    <a href="https://www.sunfounder.com/products/sunfounder-breadboard-kit" target="_blank">BUY</a>

.. |link_rgb_led_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-5mm-4-pin-rgb-common-cathode-led" target="_blank">BUY</a>

.. |link_button_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-6x6x5-mm-miniature-push-button" target="_blank">BUY</a>

.. |link_capacitor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/ceramic-capacitor-assortment-kit-set-of-600-small-assorted-capacitors" target="_blank">BUY</a>

.. |link_potentiometer_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10pcs-10k-ohm-trim-potentiometer-breadboard" target="_blank">BUY</a>

.. |link_photoresistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-photoresistor-photo-light-sensitive-resistor-5516" target="_blank">BUY</a>

.. |link_thermistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/50pcs-ntc-thermistor-mf11-103-10k-ohm" target="_blank">BUY</a>

.. |link_transistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10-values-200pcs-power-supply-general-transistor-npn-pnp-assortment-kit-bc337-bc327-2n2222-2n2907-2n3904-2n3906-s8050-s8550-a1015-c1815-set" target="_blank">BUY</a>

.. |link_relay_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10pcs-srs-05vdc-sl-c-5v-relay-coil-spdt-6-pin-pcb-electromagnetic-power-relay" target="_blank">BUY</a>

.. |link_passive_buzzer_buy| raw:: html

    <a href="https://www.sunfounder.com/products/20pcs-3-5v-2-terminals-passive-buzzer" target="_blank">BUY</a>

.. |link_ws2812_buy| raw:: html

    <a href="https://www.sunfounder.com/products/2pcs-8-bit-ws2812b-rgb-led-strip-5050smd-individual-addressable-60pixels-m" target="_blank">BUY</a>

.. |link_i2clcd1602_buy| raw:: html

    <a href="https://www.sunfounder.com/products/i2c-lcd1602-module" target="_blank">BUY</a>

.. |link_motor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/5pcs-1-5v-6v-type-miniature-dc-motors" target="_blank">BUY</a>

.. |link_servo_buy| raw:: html

    <a href="https://www.sunfounder.com/products/sg90-micro-digital-servo" target="_blank">BUY</a>

.. |link_keypad_buy| raw:: html

    <a href="https://www.sunfounder.com/products/membrane-switch-keypad" target="_blank">BUY</a>

.. |link_74hc595_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10-pcs-ic-74hc595-74595-sn74hc595n-8-bit-shift-register-dip-16" target="_blank">BUY</a>

.. |link_7segment_buy| raw:: html

    <a href="https://www.sunfounder.com/products/30pcs-0-56-7-segment-led" target="_blank">BUY</a>

.. |link_ultrasonic_buy| raw:: html

    <a href="https://www.sunfounder.com/products/5pcs-hc-sr04-ultrasonic-module-distance-sensor" target="_blank">BUY</a>

.. |link_dht22_buy| raw:: html

    <a href="https://www.sunfounder.com/products/dht22-am2302-digital-temperature-and-humidity-sensor" target="_blank">BUY</a>

.. |link_receiver_buy| raw:: html

    <a href="https://www.sunfounder.com/products/infrared-receiver-module" target="_blank">BUY</a>

.. |link_rfid_buy| raw:: html

    <a href="https://www.sunfounder.com/products/rfid-kit-blue" target="_blank">BUY</a>

.. |link_pir_buy| raw:: html

    <a href="https://www.sunfounder.com/products/hcsr501-infrared-sensor?_pos=1&_sid=2bd5fd3cc&_ss=r" target="_blank">BUY</a>

.. |link_gpio_board_buy| raw:: html

    <a href="https://www.sunfounder.com/products/t-shape-gpio-extension-board" target="_blank">BUY</a>

.. |link_led_matrix_buy| raw:: html

    <a href="https://www.sunfounder.com/products/aceirmc-4pcs-max7219-dot-matrix-display-module-single-chip-control-led-module-diy-kit-for-arduino-with-5pin-line" target="_blank">BUY</a>

.. |link_diode_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-1n4007-4007-1a-1000v-do-41-high-quality-rectifier-diode-in4007-1n4007" target="_blank">BUY</a>

.. |link_touch_buy| raw:: html

    <a href="https://www.sunfounder.com/products/ttp223-touch-sensor-module" target="_blank">BUY</a>

.. |link_slide_switch_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10pcs-high-knob-3-pin-2-position-breadboard-friendly-spdt-slide-switch" target="_blank">BUY</a>    

.. |link_rotary_encoder_buy| raw:: html

    <a href="https://www.sunfounder.com/products/rotary-encoder-module" target="_blank">BUY</a>

.. |link_humiture_buy| raw:: html

    <a href="https://www.sunfounder.com/products/humiture-sensor-module" target="_blank">BUY</a>

.. |link_reed_switch_buy| raw:: html

    <a href="https://www.sunfounder.com/products/reed-switch-module" target="_blank">BUY</a>

.. |link_obstacle_avoidance_buy| raw:: html

    <a href="https://www.sunfounder.com/products/obstacle-avoidance-sensor" target="_blank">BUY</a>

.. |link_mpu6050_buy| raw:: html

    <a href="https://www.sunfounder.com/products/3pcs-gy-521-mpu-6050-mpu6050-3-axis-accelerometer-gyroscope-module-6-dof-6-axis-accelerometer-gyroscope-sensor-module-16-bit-ad-converter-data-output-iic-i2c-for-arduino" target="_blank">BUY</a>
    
.. |link_mfrc522_rfid_buy| raw:: html

    <a href="https://www.sunfounder.com/products/rfid-kit-blue" target="_blank">BUY</a>

.. |link_camera_buy| raw:: html

    <a href="https://www.sunfounder.com/products/5mp-1080p-camera" target="_blank">BUY</a>   

"""

# language links

rst_epilog += """

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">here</a>

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/de/latest/" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_es_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/es/latest/" target="_blank">Tutoriales en línea de español</a>

.. |link_fr_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/fr/latest/" target="_blank">Tutoriels de français en ligne</a>

.. |link_it_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/raphael-kit/it/latest/" target="_blank">Tutorial online in italiano</a>

    
.. |Adafruit_CircuitPython_DHT| raw:: html

    <a href="https://github.com/adafruit/Adafruit_CircuitPython_DHT" target="_blank">adafruit/Adafruit_CircuitPython_DHT</a>    

"""
