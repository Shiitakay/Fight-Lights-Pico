from animation import animation
from LED import LED
import math

class animation_rainbow_cycle(animation.Animation):
 
  def HSVtoRGB(self, hsvcolor):
    H = hsvcolor[0]
    S = hsvcolor[1]
    V = hsvcolor[2]
    
    if H > 359:
      print("ERROR H can only take values from 0-359")
    if S > 100:
      print("ERROR S can only take values from 0-100")
    if V > 100:
      print("ERROR V can only take values from 0-100")
    
    S = S / 100
    V = V / 100
    
    C = V * S
    Hs = H / 60
    det = (Hs%2) - 1
  
    if det < 0:
      det = det * (-1)
    
    X = C * (1-det)
    if Hs >= 0 and Hs < 1:
      R = C
      G = X
      B = 0
    if Hs >= 1 and Hs < 2:
      R = X
      G = C
      B = 0
    if Hs >= 2 and Hs < 3:
      R = 0
      G = C
      B = X
    if Hs >= 3 and Hs < 4:
      R = 0
      G = X
      B = C
    if Hs >=4 and Hs < 5:
      R = X
      G = 0
      B = C
    if Hs >= 5 and Hs < 6:
      R = C
      G = 0
      B = X
    
    m = V-C
    
    R = (R+m)*255
    G = (G+m)*255
    B = (B+m)*255
    return (math.ceil(R), math.ceil(G), math.ceil(B))
  
  def run(self, counter):
    step_scaled = int(counter * 0.1)
    hsv_col = (step_scaled % 359,100,100)
    LED.set_all(self.HSVtoRGB(hsv_col))
    return counter