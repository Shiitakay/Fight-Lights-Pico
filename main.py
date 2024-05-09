from machine import Pin
import button
import config
from LED import LED


#lights up the onborad led to have an indication of wether the board is running or not
onboard_led = Pin(25, Pin.OUT)
onboard_led.value(True)

# Checks if options buttons are pressed and performs corresponding action
def do_menu():
  if config.options_button.is_pressed:
    if config.options_increase_brightness.was_pressed:
      if config.brightness < 1:
        config.brightness += 0.1
        
    if config.options_decrease_brightness.was_pressed:
      if config.brightness > 0:
        config.brightness -= 0.1
        
    if config.options_change_animation.was_pressed:
      #delete current anim, construct a new one from the list
      del config.curr_anim
      config.curr_anim_index = (config.curr_anim_index + 1) % config.anim_cnt
      config.curr_anim = config.anim_list[config.curr_anim_index]()
      config.main_ctr = 0
        
    if config.options_change_colour.was_pressed:
      config.curr_anim.change_colour()
        
    if config.options_increase_speed.was_pressed:
      config.main_inc += 2
      if config.main_inc > 20:
        config.main_inc = 20
            
    if config.options_decrease_speed.was_pressed:
      config.main_inc -= 2
      if config.main_inc < 0:
        config.main_inc = 0
                
#--------------------------main program-------------------------------------------------------
def main_loop():
  #ordering of these is important
  config.main_ctr += config.main_inc
  config.main_ctr = config.curr_anim.run(config.main_ctr)
  for butt in config.button_list:
    butt.run()
  for led in config.led_list:
    led.set_output()
  do_menu()
  LED.show_output(config.brightness)
    
if __name__ == "__main__":
  while True:
    main_loop()
