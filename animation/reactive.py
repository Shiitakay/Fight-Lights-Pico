from animation import animation
import config
import button
import random

class animation_reactive(animation.Animation):
  # We track what each button last had set as their colour
  # so we can remove the source
  last_arr = [[0, 0, 0] for _ in config.button_list]
  
  def run(self, counter):
    i = 0
    for butt in config.button_list:
      if butt.was_pressed:
        out_colour = self.colour
        if self.cycle:
          out_colour = random.choice(animation.colours)
        for led in butt.led_list:
          config.led_list[led].add_source(out_colour)
        self.last_arr[i] = list(out_colour)
      elif butt.was_released:
        if self.last_arr[i] == [0, 0, 0]:
          #releasing without having pressed first
          #we still cover this in a try except in rem_source
          continue
        for led in butt.led_list:
          config.led_list[led].rem_source(tuple(self.last_arr[i]))
      i += 1
    return 0