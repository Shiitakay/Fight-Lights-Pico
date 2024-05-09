from animation import animation
import config

class animation_rainbow_wheel(animation.Animation):
  def wheel(self, pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
  
  def run(self, counter):
    step_scaled = int(counter * 0.2)
    for i in range(0, config.led_cnt):
      rc_index = (i * 256 // config.led_cnt) + (step_scaled % 255)
      config.led_list[i].set_source(self.wheel(rc_index & 255))
    return counter