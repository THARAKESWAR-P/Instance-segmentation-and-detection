#Imports
from PIL import Image
import numpy as np

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        # Write your code here
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        w,h = image.size
        if self.crop_type == "center":
            h= int(h/2)
            w= int(w/2)
            lo= u= int(self.shape[0]/2)
            le= r= int(self.shape[1]/2)
            if self.shape[0]%2:
                lo+= 1
            if self.shape[1]%2:
                r+= 1
            return image.crop((w-le, h-u, w+r, h+lo))
        else:
            x1= np.random.randint(0, w-self.shape[1])
            x2= np.random.randint(0, h-self.shape[0])
            return image.crop((x1, x2, x1+self.shape[1], x2+self.shape[0]))






        

 