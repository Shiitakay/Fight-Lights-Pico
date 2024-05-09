from animation import animation
from LED import LED

class animation_breathing(animation.Animation):
  breathing_list = [i for  i in range(0, 255)]
  breathing_list.extend(i for i in range(255, -1, -1))
  
  def run(self, counter):
    step_scaled = int(counter * 0.1)
    if step_scaled >= len(self.breathing_list):
      counter = 0
      step_scaled = 0
      if self.cycle:
        self.cycle_colour()
    brightness_scalar = self.breathing_list[step_scaled] / 255
    colour_scaled =  (int(self.colour[0] * brightness_scalar),
                      int(self.colour[1] * brightness_scalar),
                      int(self.colour[2] * brightness_scalar))
    LED.set_all(colour_scaled)
    return counter
    