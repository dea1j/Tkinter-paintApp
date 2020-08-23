# Paint-app
Paint App built in Python, using Tkinter for its Graphical User Interface.

## About
Out of all the GUI methods available in Python, tkinter is the most commonly used method.
<div>
<h4>To create a tkinter app:</h4>
<ul>
<li>Importing the module – tkinter</li>
<li>Create the main window (container)</li>
<li>Add any number of widgets to the main window</li>
<li>Apply the event Trigger on the widgets.</li>
</ul>
</div>

<div>
<h4>A Simple Hello World Program</h4>
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
</div>
<a href="https://docs.python.org/3/library/tkinter.html">Link to official documentation</a>
