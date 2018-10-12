# mandelbrot_mp.py
# Mandelbrot fractal generator with multiprocessing

import sys
from PIL import Image
import functools
import argparse
from multiprocessing import Manager, Pool

def mandelbrot_calc_row(y, w, h, max_iteration = 1000):
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

def mandelbrot_calc_set(w, h, max_iteration=10000, output='mandelbrot_mp.png'):
    """ Calculate a mandelbrot set given the width, height and
    maximum number of iterations """

    image = Image.new("RGB", (w, h))

    image_rows = {}
    pool = Pool(4)
    mandelbrot_partial = functools.partial(mandelbrot_calc_row, w=w, h=h, 
                                           max_iteration=max_iteration)
    for image_row in pool.map(mandelbrot_partial, range(h)):
        image_rows.update(image_row)
        
    # import json
    # json.dump(image_rows, open('test.json','w'))

    for i in range(w*h):
        x,y = i % w, i // w
        image.putpixel((x,y), image_rows[i])
            
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
    mandelbrot_calc_set(args.width, args.height, max_iteration=args.niter, output=args.output) 

