# MandelbrotGenerator
These python scripts allow for easy generation of high-quality fractal images. You can choose to generate the Mandelbrot Set, Burning Ship, or Julia Sets using these two python scripts. These scripts rely on Pillow and Numpy, so those packages must be installed before you use this code on your machine.

# How it works
The first script (newfractal.py) will generate either the Mandelbrot Set or Burning Ship fractal based on input from the user. It uses the image white600x600.png as a base canvas for the image. Additionally, if the user requests, the final image can be made 4K by using the image white4096x4096 as a baseline instead. Currently, the zoom scale and custom origin for the image are hard coded, but the center of the image and zoom can be changed within the code.

# Julia Sets
In order to generate Julia set images, the second script (julia.py) works in a very similar fashion as the first script. The user is prompted on if they would like their image to be in 4K before prompting the user for two real-number values. These values are used for the Julia set's c-value, a complex number which determines the way the Julia set will look based on points from the original Mandelbrot set image.
