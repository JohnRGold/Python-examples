#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this example, we use the pack
manager to create a review example.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():

    root = Tk()
    root.geometry("300x300+300+300")
    _ = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

"""The example shows how to create a more complex layout with multiple frames and pack managers.

self.pack(fill=BOTH, expand=True)
The first frame is the base frame, on which other frames are placed. Note that in addition to organizing children within frames, we also manage the frames on the base frame.

frame1 = Frame(self)
frame1.pack(fill=X)

lbl1 = Label(frame1, text="Title", width=6)
lbl1.pack(side=LEFT, padx=5, pady=5)

entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, expand=True)
The first two widgets are placed on the first frame. The entry is horizontally stretched with the fill and the expand parameters.

frame3 = Frame(self)
frame3.pack(fill=BOTH, expand=True)

lbl3 = Label(frame3, text="Review", width=6)
lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

txt = Text(frame3)
txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
Inside the third frame, we place a label and a text widget. The label is anchored to the north. The text 
widget takes the whole remaining area."""