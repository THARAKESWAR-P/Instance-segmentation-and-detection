####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
import PIL.Image
from matplotlib import pyplot as plt
from my_package.data import Dataset
from my_package.model import InstanceSegmentationModel
from my_package.analysis.visualize import plot_visualization

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
import os.path
from tkinter import *
from tkinter import ttk, filedialog
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):
    ####### CODE REQUIRED (START) #######
    # This function should pop-up a dialog for the user to select an input image file.
    # Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
    # Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
    # Once the output is computed it should be shown automatically based on choice the dropdown button is at.
    # To have a better clarity, please check out the sample video.
    global filename
    filename = filedialog.askopenfilename(title='Open a file', initialdir='./data/imgs', filetypes=(('img files', '*.jpg *.png'),))
    if filename:
        e.delete(0, "end")
        img_idx = int(os.path.splitext(os.path.basename(filename))[0])
        outputs_path = ['./outputs/' + f'Bounding-box/{os.path.basename(filename)}',
                      './outputs/' + f'Segmentation/{os.path.basename(filename)}']
        boxes, masks, classes, score = segmentor(dataset[img_idx]['image'])
        plot_visualization(dataset[img_idx]['image'], masks, boxes, classes, output=outputs_path)
        process(clicked)
    ####### CODE REQUIRED (END) #######


# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):
    ####### CODE REQUIRED (START) #######
    # Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
    # Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
    # Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
    global canvas, filename
    canvas.get_tk_widget().destroy()
    if filename:
        clicked_img = PIL.Image.open('./outputs/' + clicked.get() + '/' + os.path.basename(filename))
        img = PIL.Image.open(filename)
        figure = plt.figure(figsize=(14, 6))
        plot1 = figure.add_subplot(121)
        plot1.axis('off')
        plot2 = figure.add_subplot(122)
        plot2.axis('off')
        plot1.imshow(img)
        plot2.imshow(clicked_img)
        plt.close()
        canvas = FigureCanvasTkAgg(figure, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=4)
        e.delete(0, 'end')
    else:
        e.delete(0, 'end')
        e.insert(0, "")
    ####### CODE REQUIRED (END) #######


# `main` function definition starts from here.
if __name__ == '__main__':
    ####### CODE REQUIRED (START) ####### (2 lines)
    # Instantiate the root window.
    # Provide a title to the root window.
    root = Tk()
    root.title("20CS10044_A4")
    ####### CODE REQUIRED (END) #######

    # Setting up the segmentor model.
    annotation_file = './data/annotations.jsonl'
    transforms = []

    # Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
    # Instantiate the dataset.
    dataset = Dataset(annotation_file, transforms=transforms)

    # Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])

    e = Entry(root, width=70)
    e.grid(row=0, column=0)
    filename = ''

    ####### CODE REQUIRED (START) #######
    # Declare the file browsing button
    canvas = FigureCanvasTkAgg()
    browse_button = Button(root, text='Browse files', command=partial(fileClick, clicked, dataset, segmentor))
    browse_button.grid(row=0, column=1)
    ####### CODE REQUIRED (END) #######

    ####### CODE REQUIRED (START) #######
    # Declare the drop-down button
    dropdown_button = ttk.Combobox(root, textvariable=clicked, values=options)
    dropdown_button.grid(row=0, column=2)
    ####### CODE REQUIRED (END) #######

    # This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process", command=partial(process, clicked))
    myButton.grid(row=0, column=3)

    ####### CODE REQUIRED (START) ####### (1 line)
    # Execute with mainloop()
    root.mainloop()
    ####### CODE REQUIRED (END) #######
