import sys
import functools
import argparse

from PIL import Image
from concurrent.futures import ProcessPoolExecutor, as_completed


def mandelbrotCalcRow(y, w, h, max_iteration = 1000):
    """ Calculate one row of the mandelbrot set with size wxh """
    
    y0 = y * (2/float(h)) - 1 # rescale to -1 to 1

    image_rows = {}
    for x in range(w):
        x0 = x * (3.5/float(w)) - 2.5 # rescale to -2.5 to 1
    
        i, z = 0, 0 + 0j
        c = complex(x0, y0)
        while abs(z) < 2 and i < max_iteration:
            z = z**2 + c
            i += 1

        color = (i % 8 * 32, i % 16 * 16, i % 32 * 8)
        image_rows[y*w + x] = color

    return image_rows
        
def mandelbrotCalcSet(w, h, max_iteration=10000, output='mandelbrot_mp.png'):
    """ Calculate a mandelbrot set given the width, height and
    maximum number of iterations """

    image = Image.new("RGB", (w, h))
    image_rows = {}
    
    mandelbrot_callable = functools.partial(mandelbrotCalcRow, w=w, h=h, max_iteration=max_iteration)

    with ProcessPoolExecutor(max_workers=10) as executor:
        future_map = (executor.submit(mandelbrot_callable, y) for y in range(h))
        for future in as_completed(future_map):
            image_rows = future.result()
            for k,v in image_rows.items():
                x,y = k % w, k // w             
                image.putpixel((x,y), v)
            
    image.save(output, "PNG")
    print('Saved to',output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='mandelbrot', description='Mandelbrot fractal generator (parallel version)')
    parser.add_argument('-W','--width',help='Width of the image',type=int, default=640)
    parser.add_argument('-H','--height',help='Height of the image',type=int, default=480) 
    parser.add_argument('-n','--niter',help='Number of iterations',type=int, default=1000)
    parser.add_argument('-o','--output',help='Name of output image file',default='mandelbrot_mp.png')
    
    args = parser.parse_args()
    print('Creating mandelbrot set with size %(width)sx%(height)s, #iterations=%(niter)s' % args.__dict__)
    mandelbrotCalcSet(args.width, args.height, max_iteration=args.niter, output=args.output) 

