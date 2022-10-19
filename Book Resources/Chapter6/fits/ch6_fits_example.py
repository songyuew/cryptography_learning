import numpy as np
from astropy.io import fits

file_name = "chapter6/fits/random_array.fits"
hdu = fits.PrimaryHDU()
hdu.data = np.random.random((128,128))
# Note that setting the data automatically populates the header with basic information:
hdu.writeto(file_name, overwrite=True)

data = fits.getdata(file_name)
header = fits.getheader(file_name)

print(header)
print()
print(data)