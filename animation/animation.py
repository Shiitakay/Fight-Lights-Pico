from LED import LED
#"static" vars
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

colours = [red, orange, light_orange, yellow,
          lime,green,turqoise,blue,light_blue,
          cyan,violet,pink]
num_colours = len(colours)

class Animation:
  colour = (0, 0, 0)
  colour_index = 0
  cycle = True
  cycle_index = 0
  
  #Constructor
  def __init__(self):
    #clean up from prev anim that was running
    LED.clear_all_sources()
    LED.set_all((0, 0, 0))
    LED.show_output(0)
    self.colour_index = 0
    self.colour = colours[0]
    self.cycle = True
    self.cycle_index = 0
    
    
  # Runs the animation and sets the lEDs
  #   counter, int, counter used calculate the stage of the animation
  #  Returns:
  #    int, new value for counter to be used
  def run(self, counter):
    pass
    
  # Changes the colour of the animation
  # Should be called from do_menu only
  # cycle_colour should be called from animations instead
  def change_colour(self):
    if self.cycle:
      self.cycle = False
      self.cycle_index = 0
    elif self.colour_index + 1 == num_colours:
      self.cycle = True
      self.colour_index = 0
    else:
      self.colour_index += 1
    
    self.colour = colours[self.colour_index]
    
    
  # Changes the colour of the animation
  # Should be called from animations only
  # change_colour should be called from main instead
  def cycle_colour(self):
    self.cycle_index += 1
    if self.cycle_index == num_colours:
      self.cycle_index = 0
    self.colour = colours[self.cycle_index]