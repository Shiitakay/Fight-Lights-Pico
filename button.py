print("button")
from machine import Pin
import config
import functions
import time
import init
import machine


#button class
class button:
    name = ""
    colorRGB = (0,0,0) #the rgb color the button, this changes for every iteration
    savedRGB = (0,0,0) #this changes only when pressed
    led_list = [] #holds the same list as config[0]
    counter = 0
    was_pressed = False #tracks if the button was pressed
    highest_prio = False 
    is_pressed = False #flag to track if the button is currently pressed
    was_released = False #flag to track if the button has been pressed
    pin_num = 0 #the pin number of the button
    fade = False #flag for fade
    released = False #flag to track if the button has been released
    time = 0 #time to track the interpolation
    bg_colors = ()#current background color before fade
    config = ((0,0,0), False, 1) #(list of leds, color, Fade on or off, brightness): gets its values from config.py
    brightness = 1 #brightness when the button is pressed, values between 0 - 1
    last_color = (0,0,0)
    fadein_speed = 0
    fadeout_speed = 0
        
    def __init__(self,pin_num,name, handler): #constructor, takes a pin_number and a function for a handler that gets called for the interrupt
        self.name = name
        self.pin_num = pin_num #sets the variable for pin_num
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP) #Defines the pin: (Pin_number, wether Input or Output, Pull up or pull Down)
        self.pin.irq(trigger= Pin.IRQ_FALLING, handler = handler)#enables interrupt for the button with handler
        
        
    #gets called from the config.py to set the config variable and the led_list variable
    def set_config(self, led_list, color, fade, brightness, fadein_speed, fadeout_speed):
        self.fade = fade
        self.config = (color, self.fade)
        self.led_list = led_list
        self.brightness = brightness
        self.fadein_speed = fadein_speed
        self.fadeout_speed = fadeout_speed
        
        
    #run function, controls all behaviour of a button, on press, when released and when currently not pressed
    #gets permanently called from the main loop
    def run(self):
        self.released = False
        # this is checking if the button has any leds assigned to it
        if self.led_list[0] < 0: #do nothing if the button is set to -1 in config.py
            return
        self.was_pressed = False
        if not self.pin.value():
            self.counter = self.counter +1
            ######################when the button was just pressed###########################
            if self.counter == 1:
                self.was_pressed = True
            ######################when the button is pressed###########################
            self.is_pressed = True
            init.bg_counter = init.setback_value #sets back the idle counter, so idle mode doesn't trigger during a press

        else:
            #############when the button was just released#########################
            if self.counter != 0:
                self.counter = 0
                self.released = True
                self.was_released = True
            elif self.counter == 0:
                self.was_released = False
                
            
            ################when the button is currently not pressed###############   
            self.is_pressed = False
                

        






