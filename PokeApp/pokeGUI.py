"""
@Author: Dante Anthony
@Title: PokeApp
@Version: 1.1.0
"""
import tkinter as tk
from tkinter import ttk, messagebox
import query
import sqlite3
from PIL import Image, ImageTk
import requests



class App(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Pokebase")
        master.configure(background="#efefef", height=60, width=40)
        self.dataBase = query.baseStart("Pokemon")
        self._createWidgets()
        #master.bind('<Return>', self.calculate)

    def _createWidgets(self):
        # main frame
        mainframe = ttk.Frame(self.master)
        mainframe.pack(anchor='w', expand=True)

        # Variables
        self.search = tk.StringVar()
        self.id = tk.IntVar()
        self.name = tk.StringVar()
        self.base_experience = tk.IntVar()
        self.weight = tk.IntVar()
        self.height = tk.IntVar()
        self.imageUrl = tk.StringVar()
        self.gif = tk.PhotoImage()

        ttk.Label(mainframe, text="Name: ").grid(column=0, row=0, sticky='w')
        ttk.Label(mainframe, textvariable=self.name).grid(column=1, row=0, sticky='nw', rowspan=1, padx=5)

        ttk.Label(mainframe, text="ID: ").grid(column=0, row=1, sticky='w')
        ttk.Label(mainframe, textvariable=self.id).grid(column=1, row=1, sticky='nw', rowspan=1, padx=5)

        ttk.Label(mainframe, text="Base Experience: ").grid(column=0, row=2, sticky='w')
        ttk.Label(mainframe, textvariable=self.base_experience).grid(column=1, row=2, sticky='nw', rowspan=1, padx=5)

        ttk.Label(mainframe, text="Weight: ").grid(column=0, row=3, sticky='w')
        ttk.Label(mainframe, textvariable=self.weight).grid(column=1, row=3, sticky='nw', rowspan=1, padx=5)

        ttk.Label(mainframe, text="Height: ").grid(column=0, row=4, sticky='w')
        ttk.Label(mainframe, textvariable=self.height).grid(column=1, row=4, sticky='nw', rowspan=1, padx=5)

        self.c = tk.Canvas(mainframe, relief='raised', width=20, height=20)
        self.c.grid(row=0, column=3, rowspan=4, columnspan=2)
        self.c.create_image(20, 20, image=self.gif, anchor='nw')

        sub_frame = ttk.Frame(self.master, padding="3 3 12 12")
        sub_frame.pack(expand=True)

        self.pokemon = ttk.Entry(sub_frame, textvariable=self.search)
        self.pokemon.grid(column=1, row=0, sticky='w')
        ttk.Button(sub_frame, text="Search", command=self.checkDatabase).grid(column=3, row=0, sticky=('e', 'w', 'n', 's'))

    def checkDatabase(self):
        conn = self.configureDB()
        data = query.checkDB2(conn, self.pokemon.get())
        if data is False:
            query.pokeQuery(self.dataBase, self.pokemon.get())
            self.checkDatabase()
        else:
            self.name.set(data[1])
            self.id.set(data[0])
            self.base_experience.set(data[2])
            self.weight.set(data[3])
            self.height.set(data[4])
            self.imageUrl.set(data[5])
            self.gif = self.imageGrab()
            self.c.create_image(20, 20, image=self.gif, anchor='nw')

    def configureDB(self):
        conn = sqlite3.connect("Pokemon.db")
        return conn

    def imageGrab(self):
        im = Image.open(requests.get(self.imageUrl.get(), stream=True).raw)
        self.gif = ImageTk.PhotoImage(im)
        return self.gif


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    #ttk.Button(root, text="Hello World").grid()
    root.mainloop()