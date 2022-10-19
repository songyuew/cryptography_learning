import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from astropy.io import fits
from astropy.visualization import astropy_mpl_style

location_lat = "Encrypted latitude"
location_long = "Encrypted longitude"
author = "Encrypted name here"
satellite = "Encrypted satellite name"

# load image as pixel array
img_file = Image.open('chapter6/fits/ch6_secret_image.jpg')
xsize, ysize = img_file.size
print("Image size: {} x {}".format(xsize, ysize))
plt.style.use(astropy_mpl_style)
plt.imshow(img_file)

r, g, b = img_file.split()
r_data = np.array(r.getdata())
g_data = np.array(g.getdata())
b_data = np.array(b.getdata())
print(r_data.shape)

r_data = r_data.reshape(ysize, xsize)
g_data = g_data.reshape(ysize, xsize)
b_data = b_data.reshape(ysize, xsize)

red = fits.PrimaryHDU(data=r_data)
red.header["AUTHOR"] = author
red.header["LATOBS"] = location_lat
red.header["LONGOBS"] = location_long
red.header["SATNAME"] = satellite
red.writeto('chapter6/fits/red.fits', overwrite=True)

green = fits.PrimaryHDU(data=g_data)
green.header["AUTHOR"] = author
green.header["LATOBS"] = location_lat
green.header["LONGOBS"] = location_long
green.header["SATNAME"] = satellite
green.writeto('chapter6/fits/green.fits', overwrite=True)

blue = fits.PrimaryHDU(data=b_data)
blue.header["AUTHOR"] = author
blue.header["LATOBS"] = location_lat
blue.header["LONGOBS"] = location_long
blue.header["SATNAME"] = satellite
blue.writeto('chapter6/fits/blue.fits', overwrite=True)