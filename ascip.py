import PIL
from PIL import Image
import numpy as np

I = np.asarray(PIL.Image.open('img2.jpg'))
WIDTH = len(I[0])
HEIGHT = len(I)
print(str(WIDTH) + " x " + str(HEIGHT))

#pixels = list(img.getdata())

