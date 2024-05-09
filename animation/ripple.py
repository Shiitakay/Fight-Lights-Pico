from animation import animation
import config
import random

class animation_ripple(animation.Animation):
  
  class runner:
    curr_pos = 0
    last_pos = -1
    direction = 0
    
    inc_counter = 0
    last_cnt = 0
    
    lifespan = 0
    ttl = 0
    
    colour = (0,0,0)
    owner = None
    
    def __init__(self, owner, _start_pos, _direction, _init_cnt, _colour):
      self.curr_pos = _start_pos
      self.direction = _direction
      self.last_cnt = _init_cnt
      self.colour = _colour
      self.ttl = config.led_cnt // 2
      self.owner = owner
        
    def run(self, counter):
      inc = counter - self.last_cnt
      self.last_count = counter
      if self.last_pos > -1:
        config.led_list[self.last_pos].set_source((0, 0, 0))
      if self.lifespan >= self.ttl:
        self.owner.runner_list.remove(self)
        del self
        return
      config.led_list[self.curr_pos].set_source(self.colour)
      self.inc_counter += inc
      if self.inc_counter >= 100:
        self.last_pos = self.curr_pos
        self.curr_pos += self.direction
        self.lifespan += 1
        if self.curr_pos >= config.led_cnt:
          self.curr_pos -= config.led_cnt
        elif self.curr_pos < 0:
          self.curr_pos += config.led_cnt
        self.inc_counter = 0
  
  runner_list = []
  def run(self, counter):
    for run in self.runner_list:
      run.run(counter)
    for button in config.button_list:
      if button.was_pressed == True:
        start = button.led_list[0]
        colour = self.colour
        if self.cycle:
          colour = random.choice(animation.colours)
        self.runner_list.append(self.runner(self, start, 1, counter, colour))
        self.runner_list.append(self.runner(self, start, -1, counter, colour))
    return counter
