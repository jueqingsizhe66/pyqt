#date :2013-1-21
#author :zhaoliang
#function: teach you to use debug : 1:debug  2:h 3:u 4:u 5:u until :the old frame

import numpy as np
import pylab as pl

def test_debug():
    
    x = np.linspace(1,50,10000)
    img = np.sin(x*np.cos(x))
    img.shape = 100,-1  #when -1,it will increment the length auto!
    pl.imshow(img)#imshow needs 2-dim array
    pl.show()
      
