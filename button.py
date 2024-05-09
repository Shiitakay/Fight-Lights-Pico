from machine import Pin

#Button class
#Purely exists to track states (pressed, released etc)
#Animations then come back to check the state
class button:
    pin_num = 0
    #state flags
    was_pressed = False
    is_pressed = False
    was_released = False
    released = False
    #used in determining was_* flags
    counter = 0
    led_list = []
    
    #Consructor
    # pin_num: int, pin number on board
    # leds: tuple (int), variable number of leds nums
    def __init__(self, pin_num, leds):
      self.pin_num = pin_num
      self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP) #Defines the pin: (Pin_number, wether Input or Output, Pull up or pull Down)
      self.led_list = list(leds)
    
    # Sets all state flags
    def run(self):
      self.released = False
      self.was_pressed = False
      if not self.pin.value():
        self.counter += 1
        #when the button was just pressed
        if self.counter == 1:
          self.was_pressed = True
        #when the button is pressed
        self.is_pressed = True
      else:
        #when the button was just released
        if self.counter != 0:
          self.counter = 0
          self.released = True
          self.was_released = True
        elif self.counter == 0:
          self.was_released = False
        #when the button is currently not pressed
        self.is_pressed = False
                

        






