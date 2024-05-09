from animation import animation
from LED import LED

class animation_static(animation.Animation):
  def change_colour(self):
    self.colour_index += 1
    if self.colour_index == animation.num_colours:
      self.colour_index = 0
    self.colour = animation.colours[self.colour_index]
     
  def run(self, counter):
    LED.set_all(self.colour)
    return 0