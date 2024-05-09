print("animation")
import init
import functions
import config
import time
import statemachine
import math
import init
import button
import random

#total number of anims implemented
num_idles = 6

#cycles through config.colors, while managing whether the colour should be static or changing
#from_menu: boolean, indicates whether this function is being called from the do_menu() func
#           used to manage colour cycling, defaults to False
def change_bg_colour(from_menu = False):

    #if we came from do_menu(), then we want to change the colour and always disable cycling
    if from_menu:
        if init.cycle_bg_colour:
            #if we were cycling, then go to the first colour in the arr
            init.bg_colour_id = 0
        else:
            init.bg_colour_id += 1
        init.cycle_bg_colour = False
        
    #if we came from do_menu, this wont run
    if init.cycle_bg_colour:
        init.bg_colour_id += 1
        
    if init.bg_colour_id >= config.num_colours:
        init.bg_colour_id = 0
        init.cycle_bg_colour = True

#simply indexes the colors array, just here to make code look cleaner
#dont know if pythons overhead for calling functions really matters in this code
def get_bg_colour():
    return config.colors[init.bg_colour_id]

def get_random_colour():
    return random.choice(config.colors)

#all credits for the breathing light goes to Joshua Hrisko, Maker Portal LLC (c) 2021
#runs through an array of preset brightness values to create a breathing effect
def bg_breathing(): #breathing LED
    #TODO: allows users to define a brighness graph to go along, could be cool
    
    step_scaled = math.floor(init.main_ctr * (config.bg_speed / 10)) #magic number = 10
    if step_scaled > init.breathing_ar_len:
        #set brightness to zero as well
        step_scaled = 0
        change_bg_colour()
        init.main_ctr = 0
    brightness = init.breathing_ar[step_scaled]
    functions.pixels_fill(get_bg_colour())
    functions.pixels_show((brightness/255) * config.brightness_mod)

#simple static colour
def bg_static():
    functions.pixels_fill(get_bg_colour())
    functions.pixels_show(config.brightness_mod)

#https://core-electronics.com.au/tutorials/how-to-use-ws2812b-rgb-leds-with-raspberry-pi-pico.html
#uses colour wheel to display a gradient across the strip
def bg_rainbow_wheel():
    step_scaled = math.floor(init.main_ctr * (config.bg_speed / 10))
    for i in range(config.led_count):
        rc_index = (i * 256 // config.led_count) + (step_scaled % 255)
        functions.pixels_set(i, functions.wheel(rc_index & 255))
    functions.pixels_show(config.brightness_mod)
    
#cycles through rainbow colours one at a time
#basically just changes the hue slider every loop
def bg_rainbow_cycle():
    step_scaled = math.floor(init.main_ctr * (config.bg_speed / 10))
    hsv_col = (step_scaled % 359,100,100)
    functions.pixels_fillHSV(hsv_col)
    functions.pixels_show(config.brightness_mod)
    
def reactive_light():
    released_flag = False
    for button in config.button_list:
        if button.was_pressed == True:
            print("here")
            functions.pixels_set_range(button.led_list, get_bg_colour())
        elif button.was_released == True:
            released_flag = True
            functions.pixels_set_range(button.led_list, config.blank)
    #horribly innefficient - thisll be the first thing to convince me of a rewrite of the entire code
    if released_flag:
        for button in config.button_list:
            if button.is_pressed:
                functions.pixels_set_range(button.led_list, get_bg_colour())
    functions.pixels_show(config.brightness_mod)

class runner:
    curr_pos = 0
    last_pos = -1
    #end_pos = 38
    lifespan = 0
    ttl = 0
    direction = 0
    colour = (0,0,0)
    inc_counter = 0
    
    def __init__(self, _start_pos, _direction, _colour):
        self.curr_pos = _start_pos
        #self.end_pos = _end_pos
        self.direction = _direction
        self.colour = _colour
        self.ttl = config.led_count // 2
        init.runner_list.append(self)
        
    def run(self):
        if self.last_pos > -1:
            functions.pixels_set(self.last_pos, config.blank)
        if self.lifespan >= self.ttl:
            init.runner_list.remove(self)
            del self
            return
        functions.pixels_set(self.curr_pos, self.colour)
        self.inc_counter += init.main_inc
        if self.inc_counter >= 20:
            self.last_pos = self.curr_pos
            self.curr_pos += self.direction
            self.lifespan += 1
            if self.curr_pos >= config.led_count:
                self.curr_pos -= config.led_count
            elif self.curr_pos < 0:
                self.curr_pos += config.led_count
            self.inc_counter = 0
            

def reactive_ripple():
    for button in config.button_list:
        if button.was_pressed == True:
            start = button.led_list[0]
            #end = button.led_list[2]
            colour = None
            if init.cycle_bg_colour == True:
                colour = get_random_colour()
            else:
                colour = get_bg_colour()
            runner(start, 1, colour)
            runner(start, -1, colour)
            #runner(end, 1, colour)
            #runner(end, -1, colour)
    for run in init.runner_list:
        run.run()
    functions.pixels_show(config.brightness_mod)
            
                                                    
    
    
    
def bg_runway():
    fade_speed = 10
    led_count = config.led_count
    backwards = False
    cnt = random.randint(0, 359)
    sleep_time = 0.05
    while init.bg_counter > init.bg_ticks:
        cnt += 60
        cnt = cnt % 359
        hsv_col = (cnt, 100,100)
        hsv_col2 = (360-cnt, 100, 100)
        color = functions.HSVtoRGB(hsv_col)
        for i, k in zip(range(led_count), range(led_count-1, -1, -1)):
            if init.bg_counter <= init.bg_ticks:
                return
            #time.sleep_ms(400)
            functions.pixels_set(i,color)
            #functions.pixels_set(k,color2)
            functions.pixels_show(config.brightness_mod)
            
            for j in range(led_count):
                if init.bg_counter <= init.bg_ticks:
                    return
                pxl_color = functions.get_pixelcolor(j)
                hsv_color = functions.RGBtoHSV(pxl_color)
                value = hsv_color[2]-fade_speed
                if value < 10:
                    value = 10
                hsv_color = (hsv_color[0],hsv_color[1], value)
                pxl_color = functions.HSVtoRGB(hsv_color)
                functions.pixels_set(j,pxl_color)
            
            time.sleep(sleep_time)
            if i == 0:
                if not backwards:
                    sleep_time -= 0.001
                else:
                    sleep_time += 0.001
                if sleep_time <= 0:
                    backwards = True
                if sleep_time >= 0.05:
                    backwards = False


def color_change():
    for i in range(360):
        #time.sleep_ms(2)
        functions.pixels_fillHSV((i,100,100))
        functions.pixels_show(config.brightness_mod)
        if i == 359:
            hsv_col = [359,100,100]
            for j in range(0,100):
                functions.pixels_fillHSV((359,100,100-j))
                functions.pixels_show(config.brightness_mod)
                
def pulsing_light(wait_ms=100):
    position = 0
    for i in range(config.led_count * 2):
        position = position+1
        for j in range(config.led_count):
            functions.pixels_set(j,(round(((math.sin(j+position) * 127 + 128)/255)*255),round(((math.sin(j+position) * 127 + 128) /255)*100), round(((math.sin(j+position) * 127 + 128) /255)*100)))
        functions.pixels_show(config.brightness_mod)
        time.sleep(wait_ms/1000.0)


def color_fade_out(led_pos, color_rgb, speed=1):
    color_hsv = functions.RGBtoHSV(color_rgb)
    val = color_hsv[2]
    
    while val > 0:
        new_hsv = [color_hsv[0],color_hsv[1],val]
        for i in range(len(led_pos)):
            functions.pixels_setHSV(led_pos[i], new_hsv)
        functions.pixels_show(config.brightness_mod)
        val -= speed
        if val < 0:
            val = 0
        
        

        
#fades in an led at led_pos, into color of color_rgb
def color_fade_in(led_pos, color_rgb, speed=1):
    color_hsv = functions.RGBtoHSV(color_rgb)
    
    val = 0
    while val < color_hsv[2]:
        val += speed
        if val > 100:
            val = 100
        new_hsv = [color_hsv[0],color_hsv[1],val]
        for i in range(len(led_pos)):
            functions.pixels_setHSV(led_pos[i], new_hsv)
        functions.pixels_show(config.brightness_mod)

def fireball(led_order, color_rgb, speed=16):
    #led_order = (7,8,6,9,5,10,4,11,3,12,2,13,1,14,0,15)

    for i in range(0,len(led_order),2):
        color_fade_in((led_order[i],led_order[i+1]), color_rgb, speed)

    #time.sleep_ms(50)
    for j in range(0,len(led_order),2):
        color_fade_out((led_order[j],led_order[j+1]), color_rgb, speed)
        
    for but in button.button_list:
        but.time = 0
        
def flash_all(color_rgb):
    functions.pixels_fill(color_rgb)
    functions.pixels_show(config.brightness_mod)
    time.sleep_ms(10)
    
    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)
    time.sleep_ms(10)
    
    functions.pixels_fill(color_rgb)
    functions.pixels_show(config.brightness_mod)
    time.sleep_ms(10)
    
    functions.pixels_fill((0,0,0))
    functions.pixels_show(config.brightness_mod)

#lights up the led at pos with color
def light_led(pos, color):
    for i in pos:
        functions.pixels_set(i,config.colors[init.random_color])
        #functions.pixels_show(config.brightness_mod)
    
        
