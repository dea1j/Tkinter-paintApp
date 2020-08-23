from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
# import PIL
# from PIL import Image, ImageDraw, ImageGrab, ImageTk

root=Tk()
root.title("Paint")
root.geometry("800x800")

brushColor = 'black'

def paint(e):
    # Brush Parameters
    # brushColor = 'green'
    brushSize = int(mySlider.get())
    # Brush type / capstyle: BUTT, ROUND, PROJECTING
    brushType2 = brushType.get()

    # Starting Point
    x1 = e.x -1
    y1 = e.y -1
    # Ending Point
    x2 = e.x + 1
    y2 = e.y + 1

    myCanvas.create_line(x1, y1, x2, y2, fill=brushColor, width=brushSize, capstyle=brushType2, smooth=True)

# Change brush Size
def changeBrushSize(e):
    sliderLabel.config(text=int(mySlider.get()))
    # sliderLabel.config(text='%0.0f' % float(mySlider.get()))


# Change Brush Color
def changeBrushColor():
    global brushColor
    brushColor = 'black'
    brushColor= colorchooser.askcolor(color=brushColor)[1]


# Change Canvas Color
def changeCanvasColor():
    global bgColor
    bgColor = 'black'
    bgColor= colorchooser.askcolor(color=bgColor)[1]
    myCanvas.config(bg=bgColor)

# Clear Screen
def clearScreen():
    myCanvas.delete(ALL)
    myCanvas.config(bg='wheat')

# Save Image 
def saveImage():
    result = filedialog.asksaveasfilename(initialdir="/Users/mac/Desktop/foldersvskla/Pelumi's Class/GUI", filetypes=(('png files', '*.png'), ('all files', '*.*')))
    
    if result.endswith('.png'):
        pass
    else:
        result = result + 'png'
    if result:
        x=root.winfo_rootx() + myCanvas.winfo_rootx()
        y=root.winfo_rooty() + myCanvas.winfo_rooty()
        x1=x+myCanvas.winfo_width()
        y1=y+myCanvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)




# Create Canvas
w = 600
h = 400
myCanvas = Canvas(root, width=w, height=h, bg='wheat')
# myCanvas.grid(row=1, column=2)
myCanvas.pack(pady=20)

# myCanvas.create_line(0, 100, 300, 100, fill='red')
# myCanvas.create_line(150, 0, 150, 500, fill='red')

myCanvas.bind('<B1-Motion>', paint)


# Create brush option frame
brushFrame = Frame(root)
brushFrame.pack(pady=20)

# Brush Size
brushSizeFrame = LabelFrame(brushFrame, text='Brush Size')
brushSizeFrame.grid(row=0, column=0, padx=50)
#Brush Slider
mySlider = ttk.Scale(brushSizeFrame, from_=1, to=100, command=changeBrushSize, orient=VERTICAL, value=10)
mySlider.pack(pady=10, padx=10)

#Brush Size Label
sliderLabel = Label(brushSizeFrame, text=mySlider.get())
sliderLabel.pack(pady=5)

#Brush Type
brushTypeFrame = LabelFrame(brushFrame, text='Brush Type', height=400)
brushTypeFrame.grid(row=0, column=1, padx=50)

brushType = StringVar()
brushType.set('round')

# Create Radio Button for Brush type
brushTypeRadio1 = Radiobutton(brushTypeFrame, text='Round', variable=brushType, value='round')
brushTypeRadio1.pack(anchor=W)
brushTypeRadio2 = Radiobutton(brushTypeFrame, text='Slash', variable=brushType, value='butt')
brushTypeRadio2.pack(anchor=W)
brushTypeRadio3 = Radiobutton(brushTypeFrame, text='Diamond', variable=brushType, value='projecting')
brushTypeRadio3.pack(anchor=W)

# Change Color
changeColorsFrame = LabelFrame(brushFrame, text='Change Color')
changeColorsFrame.grid(row=0, column=3)
# Change brush color button
brushColorButton = Button(changeColorsFrame, text='Brush Color', command=changeBrushColor)
brushColorButton.pack(pady=10, padx=10)

# Change Canvas color button
canvasColorButton = Button(changeColorsFrame, text='Canvas Color', command=changeCanvasColor)
canvasColorButton.pack(pady=10, padx=10)


# Program Options Frame
optionFrame = LabelFrame(brushFrame, text='Program Option')
optionFrame.grid(row=0, column=4, padx=50)

# Clear Screen Button
clearButton = Button(optionFrame, text='Clear Screen', command=clearScreen)
clearButton.pack(pady=10, padx=10)

# Save Image
saveImageButton = Button(optionFrame, text='Save to PNG', command=saveImage)
saveImageButton.pack(pady=10, padx=10)


root.mainloop()