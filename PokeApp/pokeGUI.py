import tkinter as tk
from tkinter import ttk, messagebox
import query
import sqlite3


class App(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Pokebase")
        master.resizable(False, False)
        master.configure(background="#efefef")
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
        #self.image = sprite_url

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
        else:
            self.name.set(data[1])
            self.id.set(data[0])
            self.base_experience.set(data[2])
            self.weight.set(data[3])
            self.height.set(data[4])


    def configureDB(self):
        conn = sqlite3.connect("Pokemon.db")
        return conn


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    #ttk.Button(root, text="Hello World").grid()
    root.mainloop()