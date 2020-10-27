import rawpy
import imageio
import PIL
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import imshow

path = '/Users/nicholas/Desktop/nati.arw'

raw = rawpy.imread(path)
rgb = raw.postprocess(use_camera_wb=True)
nrgb = raw.postprocess(use_auto_wb=True)
print (rgb.dtype, rgb.shape)

f, axarr = plt.subplots(1,2)

axarr[0].imshow(rgb)
axarr[1].imshow(nrgb)
plt.show()
