#when launching this module by accident it will launch the main.py instead
if __name__ == '__main__':
    import init
    with open('main.py', 'r') as f:
        init.code = f.read()
    exec(init.code)

print("config")
#Fight Lights Pico V2.4.0

from machine import Pin
from init import random, rainbow, smooth
import button
import functions
import init

blank = (0,0,0)
red = (255,0,0)
orange = (255,127,0)
light_orange = (255,200,0)
yellow = (255,255,0)
lime = (160,255,0)
green = (0,255,0)
turqoise = (64,224,208)
blue = (0,0,255)
light_blue = (0,193,255)
violet = (170,0,255)
pink = (255,0,170)
cyan = (0,255,255)

colors = [red,orange,light_orange,yellow,lime,green,turqoise,blue,light_blue,violet,pink,cyan]
num_colours = len(colors)
bg_colour_index = 0
bg_speed = 1

profile_name = "OneButtonPer"
led_count = 38
PIN_NUM = 0
leniency = 1
brightness_mod = 1
brightness_steps = 0.1
bg_mode = 0
bg_after = 10
save_stats = False
input_reset_time = 50
profile_color = (255,0,0)
clear_background_on_press = False
background = ((1,blank,1),(1,blank,2),(1,blank,3),(1,blank,4),(1,blank,5),(1,blank,6),(1,blank,7),(1,blank,8),(1,blank,9),(1,blank,10),(1,blank,11),(1,blank,12),(1,blank,13),(1,blank,14),(1,blank,15),(1,blank,16),(1,blank,17),(1,blank,18),(1,blank,19),(1,blank,20),(1,blank,21),(1,blank,22),(1,blank,23),(1,blank,24),(1,blank,25),(1,blank,26),(1,blank,27),(1,blank,28),(1,blank,29),(1,blank,30),(1,blank,31),(1,blank,32),(1,blank,33),(1,blank,34),(1,blank,35),(1,blank,36),(1,blank,37),(1,blank,38))

#-----------init buttons
up_button		 = button.button(1, 'up', functions.clear_led)
down_button		 = button.button(2, 'down', functions.clear_led)
right_button	 = button.button(3, 'right', functions.clear_led)
left_button		 = button.button(4, 'left', functions.clear_led)

ps_button		 = button.button(6, 'ps', functions.clear_led)

square_button	 = button.button(8, 'square', functions.clear_led)
triangle_button	 = button.button(9, 'triangle', functions.clear_led)
r1_button		 = button.button(10, 'r1', functions.clear_led)
l1_button		 = button.button(11, 'l1', functions.clear_led)

circle_button	 = button.button(12, 'circle', functions.clear_led)
x_button		 = button.button(13, 'x', functions.clear_led)
l2_button		 = button.button(14, 'l2', functions.clear_led)
r2_button		 = button.button(15, 'r2', functions.clear_led)

button_list 	= [up_button, down_button, right_button, left_button, ps_button, square_button, triangle_button,
                    r1_button, l1_button, circle_button, x_button, l2_button, r2_button]
init.button_list_length = len(button_list)


up_button.set_config((1,11,28,37,), violet, True, 1, 100, 4)
down_button.set_config((1,12,28,36,), violet, True, 1, 100, 4)
right_button.set_config((2,12,27,36,), violet, True, 1, 100, 4)
left_button.set_config((0,12,29,36,), violet, True, 1, 100, 4)

ps_button.set_config((5,14,24,35,), violet, True, 1, 100, 4)

square_button.set_config((10,12,19,36,), violet, True, 1, 100, 4)
triangle_button.set_config((8,13,21,35,), violet, True, 1, 100, 4)
r1_button.set_config((10,13,19,35,), violet, True, 1, 100, 4)
l1_button.set_config((9,13,20,35,), violet, True, 1, 100, 4)

circle_button.set_config((9,12,20,36,), violet, True, 1, 100, 4)
x_button.set_config((8,12,21,36,), violet, True, 1, 100, 4)
l2_button.set_config((8,11,21,37,), violet, True, 1, 100, 4)
r2_button.set_config((9,11,20,37,), violet, True, 1, 100, 4)

options_button = ps_button
options_increase_brightness = up_button
options_decrease_brightness = down_button
options_change_animation = left_button
options_change_colour = right_button
options_increase_speed = x_button
options_decrease_speed = triangle_button
rainbow_speed = 1000

#------------init player led
activate_player_led = False
playerLED_brightness = 1
playerLED_PIN_NUM = 16
P1_color = yellow
P2_color = yellow
P3_color = yellow
P4_color = yellow
############do not delete this line#######################