from machine import Pin
#imports are staggered since i'm stupid and theyre cyclical now
#data out pin for led strip
PIN_NUM = 0
led_cnt = 38

import LED
#init LED objects
led_list = []
for i in range(0, led_cnt):
  led_list.append(LED.LED(i))

import button
#-----------init buttons
up_button       = button.button(1, (1,11,28,37))
down_button     = button.button(2, (1,12,28,36))
right_button    = button.button(3, (2,12,27,36))
left_button     = button.button(4, (0,12,29,36))

ps_button       = button.button(6, (5,14,24,35))

square_button	= button.button(8, (10,12,19,36))
triangle_button = button.button(9, (8,13,21,35))
r1_button       = button.button(10, (10,13,19,35))
l1_button       = button.button(11, (9,13,20,35))

circle_button   = button.button(12, (9,12,20,36))
x_button        = button.button(13, (8,12,21,36))
l2_button       = button.button(14, (8,11,21,37))
r2_button       = button.button(15, (9,11,20,37))
button_list 	  = [up_button, down_button, right_button, left_button, ps_button, 
                square_button, triangle_button, r1_button, l1_button, 
                circle_button, x_button, l2_button, r2_button]

#set options buttons 
options_button = ps_button
options_increase_brightness = up_button
options_decrease_brightness = down_button
options_change_animation = left_button
options_change_colour = right_button
options_increase_speed = x_button
options_decrease_speed = triangle_button

#we import here to aviod cyclical import issues
from animation import animation, static, breathing, rainbow_wheel, rainbow_cycle, reactive, ripple
#hold function pointers to anim constructors
anim_list = [static.animation_static,
             breathing.animation_breathing,
             rainbow_wheel.animation_rainbow_wheel,
             rainbow_cycle.animation_rainbow_cycle,
             reactive.animation_reactive,
             ripple.animation_ripple]
anim_cnt = len(anim_list)
curr_anim = anim_list[0]()
curr_anim_index = 0

brightness = 1.0
main_ctr = 0
main_inc = 1