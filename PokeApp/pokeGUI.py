import tkinter as tk
from tkinter import ttk, messagebox


class App(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Pokebase")
        master.resizable(False, False)
        master.configure(background="#efefef")
        self._createWidgets()
        #master.bind('<Return>', self.calculate)

    def _createWidgets(self):
        # main frame
        mainframe = ttk.Frame(self.master)
        mainframe.pack(anchor='w', expand=True)

        # Variables
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

        sub_frame = ttk.Frame(self.master, padding="3 3 12 12")
        sub_frame.pack(expand=True)

        pokemon = ttk.Entry(sub_frame, )
        pokemon.grid(column=1, row=0, sticky='w')
        ttk.Button(sub_frame, text="Search").grid(column=3, row=0, sticky=('e', 'w', 'n', 's'))




if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    #ttk.Button(root, text="Hello World").grid()
    root.mainloop()