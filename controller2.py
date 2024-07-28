import pyfirmata2

comport = 'COM5'

board = pyfirmata2.Arduino(comport)

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

def led(fingerUp):
    leds = [led_1, led_2, led_3, led_4, led_5]
    for i in range(len(fingerUp)):
        if fingerUp[i] == 1:
            leds[i].write(1)
        else:
            leds[i].write(0)
