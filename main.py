print("main")
import time
from machine import Pin
import statemachine
import button
import config
import functions
import init
import random
import animation
import _thread

if config.activate_player_led:
    import playerLED


#clear the init.code variable to free up the memory if the main has been started from another config
init.code = ""

#lights up the onborad led to have an indication of wether the board is running or not
onboard_led = Pin(25, Pin.OUT)
onboard_led.value(True)

# Set and show pixels for background
def do_bg():
    #micropython has no switch statements
    if config.bg_mode == 0:
        animation.bg_breathing()
    elif config.bg_mode == 1:
        animation.bg_static()
    elif config.bg_mode == 2:
        animation.bg_rainbow_wheel()
    elif config.bg_mode == 3:
        animation.bg_rainbow_cycle()
    elif config.bg_mode == 4:
        animation.reactive_light()
    elif config.bg_mode == 5:
        animation.reactive_ripple()

# Rather than using different config files, things will be changable just using some buttons
# Led_options + 
#   increase_brightness
#   decrease_brightness
#   change_animation
#   change_colour
#   increse_speed
#   decrease_speed
# We dont really need an off button, just let brightness go to 0
# We dont really need two-way cycling for animation or colour
def do_menu():
    if config.options_button.is_pressed:
        if config.options_increase_brightness.was_pressed:
            functions.increase_brightness(config.brightness_steps)
            
        if config.options_decrease_brightness.was_pressed:
            functions.decrease_brightness(config.brightness_steps)
            
        if config.options_change_animation.was_pressed:
            config.bg_mode = (config.bg_mode + 1) % animation.num_idles
            init.main_ctr = 0
            init.bg_colour_id = 0
            init.cycle_bg_colour = True
            functions.pixels_fill(config.blank)
            
        if config.options_change_colour.was_pressed:
            #currently, anything that cycles will still cycle
            #TODO: have breathing/runway only use one colour when the buttons are pressed
            #       maybe think of something for the rainbow gradient as well
            animation.change_bg_colour(from_menu = True)
            functions.pixels_set_range(functions.get_lit_pixels(), animation.get_bg_colour())
            functions.pixels_show(config.brightness_mod)
            
        if config.options_increase_speed.was_pressed:
            init.main_inc += 2
            if init.main_inc > 20:
                init.main_inc = 20
            '''
            config.bg_speed += 1
            if config.bg_speed > 10:
                config.bg_speed = 10
               ''' 
        if config.options_decrease_speed.was_pressed:
            #currently, we straight up multiply values by the speed, so chagning speed makes things jump around a lot
            #TODO: find a way to increase the speed without moving accross the timeline
            #      most likely have to use some sort of step to increase to main_ctr rather than just multiply it later on
            #       changing main cntr increment has some issues, the speed seems to actually change
            init.main_inc -= 2
            if init.main_inc < 0:
                init.main_inc = 0
            '''
            config.bg_speed -= 1
            if config.bg_speed < 1:
                config.bg_speed = 1    
                '''
#--------------------------main program-------------------------------------------------------
def main():
    do_bg()
    for butt in config.button_list:
        butt.run()
    do_menu()
    init.main_ctr += init.main_inc

#main loop
while True:
    main()  

        
