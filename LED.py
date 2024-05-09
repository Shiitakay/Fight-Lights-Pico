import array
import statemachine
import config

# Class to handle colours -> actual LED output
# Mainly exists to resolve issues that could arrive with priority
# and multiple colour sources acting on the same LED
#"static" vars
out_arr = statemachine.ar
class LED:
  out_num = 0
  sources = [] #list of tuples (0, 0, 0)
  
  # Constructor
  #   out_num: int, the corresponding LED it will output to, 0 indexed
  def __init__(self, _out_num):
    self.sources = []
    self.out_num = _out_num
  
  # TODO: handling sources is super primitive and won't solve 
  # the issue fully with current implementation
  # we only consider the value, and not the actual source
  
  # Adds an RGB value to be outputted
  #   Source: tuple (int, int, int), an RGB value to be output
  def add_source(self, source):
    self.sources.append(source)
  
  # Removes an RGB from being outputted
  #   Source: tuple (int, int, int), an RGB value to be removed
  def rem_source(self, source):
    try:
      self.sources.remove(source)
    except:
        pass
    if not self.sources:
      self.set_source((0, 0, 0))
    
  # Directly sets the source as output, bypassing source handling
  #   Source: tuple (int, int, int), an RGB value to be set
  def set_source(self, source):
    out_arr[self.out_num] = (source[1] << 16) + (source[0] << 8) + source[2]
    
  # Clears all sources from its list
  # Called from destructor of animations that use the source system
  def clear_sources(self):
    self.sources.clear()
    
  # Sets the RGB value for the LED this object controls
  # Call after adding all sources with add_source(source)
  def set_output(self):
    if len(self.sources) < 1:
      return
    colour = self.sources[-1]
    out_arr[self.out_num] = (colour[1] << 16) + (colour[0] << 8) + colour[2]
  
  # Static method to set all LEDs to the same colour
  #   colour: tuple (int, int, int), the colour to set
  @staticmethod
  def set_all(colour):
    for led in config.led_list:
      led.set_source(colour)
      
  # Static method to clear all sources
  @staticmethod
  def clear_all_sources():
    for led in config.led_list:
      led.clear_sources()
      
  # Static method to light up all LEDs with their set values 
  #   Brightness: float (0.0 - 1.0), how bright the LEDs should be
  @staticmethod
  def show_output(brightness):
    #brightness should stay in range since its only controlled by do_menu()
    dimmer_ar = array.array("I", [0 for _ in range(config.led_cnt)])
    brightness_scalar = int(255 * brightness)
    for ii, cc in enumerate(out_arr):
      r = (cc >> 8) & 0xFF
      g = (cc >> 16) & 0xFF
      b = cc & 0xFF
      r_out = (r * brightness_scalar) >> 8
      g_out = (g * brightness_scalar) >> 8
      b_out = (b * brightness_scalar) >> 8
      dimmer_ar[ii] = (g_out << 16) | (r_out << 8) | b_out
    statemachine.sm.put(dimmer_ar, 8)
  