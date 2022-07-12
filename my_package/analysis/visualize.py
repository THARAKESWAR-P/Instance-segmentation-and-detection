#Imports
import random

from PIL import ImageDraw, Image
import numpy as np


def plot_visualization(img, smasks, bboxes, labels, output):  # Write the required arguments
    image = Image.fromarray(np.uint8(img.transpose((1, 2, 0)) * 255))
    orig_image = Image.fromarray(np.uint8(img.transpose((1, 2, 0)) * 255))
    for i in range(min(3, len(bboxes))):
        ImageDraw.Draw(image).rectangle(bboxes[i], outline='red', width=4)
    for i in range(min(3, len(bboxes))):
        ImageDraw.Draw(image).text(bboxes[i][0], labels[i], fill='yellow')
    image.save(output[0])

    for i in range(min(3, len(smasks))):
        arr = orig_image.load()
        h, w = smasks[i][0].shape
        R = 255
        G = 255
        B = 255
        if i == 0:
            B = 0
        if i == 1:
            B = 255
            G = 0
        if i == 2:
            G = 255
            R = 0
        for y in range(h):
            for x in range(w):
                if smasks[i][0][y][x] > 0.4:
                    # r, g, b = arr[x, y]
                    arr[x, y] = (R, G, B)
    orig_image.save(output[1])

# The function should plot the predicted boxes on the images and save them.
# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.