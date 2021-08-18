Keypad
========================

A keypad is a rectangular array of 12 or 16 OFF-(ON) buttons. 
Their contacts are accessed via a header suitable for connection with a ribbon cable or insertion into a printed circuit board. 
In some keypads, each button connects with a separate contact in the header, while all the buttons share a common ground.

.. image:: img/keypad314.png

More often, the buttons are matrix encoded, meaning that each of them bridges a unique pair of conductors in a matrix. 
This configuration is suitable for polling by a microcontroller, which can be programmed to send an output pulse to each of the four horizontal wires in turn. 
During each pulse, it checks the remaining four vertical wires in sequence, to determine which one, if any, is carrying a signal. 
Pullup or pulldown resistors should be added to the input wires to prevent the inputs of the microcontroller from behaving unpredictably when no signal is present.

