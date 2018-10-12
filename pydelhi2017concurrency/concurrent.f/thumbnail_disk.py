"""

Convert images to thumbnails - using threads or processes

"""

import threading
import glob
import os
from PIL import Image
from queue import Empty
import multiprocessing

class ThumbnailURL_Converter(threading.Thread):
    """ Worker class that process image files and generates thumbnails """

    def __init__(self, queue):
        self.queue = queue
        self.flag = True
        threading.Thread.__init__(self)     

    def thumbnail_image(self, filename, size=(64,64), format='.png'):
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

    def run(self):
        """ Main thread function """

        while self.flag:
            try:
                filename = self.queue.get(timeout=1)
                # print(self,'Got',filename)
                self.thumbnail_image(filename)
            except Empty:
                break

    def stop(self):
        """ Stop the thread """

        self.flag = False
        self.join()


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
    from queue import Queue

    thread = True

    if thread:
        q = Queue(10000)
        print('Running with threads')
        # Fill it with images
        for root,dirs,files in os.walk(os.path.expanduser('~/Pictures/')):
            for f in files:
                q.put(os.path.join(root,f))

        print('Queue size=>',q.qsize())
        # Start 5 converter threads
        threads = []
        for i in range(4):
            t = ThumbnailURL_Converter(q)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
    else:
        filenames = []
        for root,dirs,files in os.walk(os.path.expanduser('~/Pictures/')):
            for f in files:
                filenames.append(os.path.join(root,f))

        pool = multiprocessing.Pool(5)
        pool.map(thumbnail_image, filenames)
        
        
