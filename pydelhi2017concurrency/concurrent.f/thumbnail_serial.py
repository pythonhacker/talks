"""

Convert images to thumbnails - in serial fashion (no concurrency)

"""

import os
from PIL import Image

def thumbnail_image(filename, size=(64,64), format='.png'):
    """ Convert image thumbnails, given a filename """

    try:
        im=Image.open(filename)         
        im.thumbnail(size, Image.ANTIALIAS)

        basename = os.path.basename(filename)
        thumb_filename = os.path.join('thumbs',
                                      basename.rsplit('.')[0] + '_thumb.png')
        im.save(thumb_filename)
        print('Saved',thumb_filename)
    except Exception as e:
        print('Error converting file',filename)

    return True
    
if __name__ == '__main__':
    
    for root,dirs,files in os.walk(os.path.expanduser('~/Pictures/')):
        for f in files:
            thumbnail_image(os.path.join(root,f))
        
        
