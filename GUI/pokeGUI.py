"""
@Author: Dante Anthony
@Title: PokeApp
@Version: 1.1.0
"""
from io import BytesIO

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests

from Models.DatabaseManager import DatabaseManager
from Models import query_pokemon_api_for_pokemon_named, Pokemon



class App(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Pokebase")
        master.configure(background="#efefef", height=60, width=60)

        # Pokemon Details
        self.search = tk.StringVar()
        self.id = tk.IntVar()
        self.name = tk.StringVar()
        self.base_experience = tk.IntVar()
        self.weight = tk.IntVar()
        self.height = tk.IntVar()
        self.imageUrl = tk.StringVar()
        self.gif = tk.PhotoImage()

        # DB Manager
        self.database_manager = DatabaseManager(database_name="test2")

        # Create Window
        self._create_widgets()

    def _create_widgets(self):
        # main frame
        mainframe = ttk.Frame(self.master)
        mainframe.pack(anchor='w', expand=True)

        # Name Row
        ttk.Label(mainframe, text="Name: ").grid(column=0, row=0, sticky='w')
        ttk.Label(mainframe, textvariable=self.name).grid(column=1, row=0, sticky='nw', rowspan=1, padx=5)

        # ID Row
        ttk.Label(mainframe, text="ID: ").grid(column=0, row=1, sticky='w')
        ttk.Label(mainframe, textvariable=self.id).grid(column=1, row=1, sticky='nw', rowspan=1, padx=5)

        # XP Row
        ttk.Label(mainframe, text="Base Experience: ").grid(column=0, row=2, sticky='w')
        ttk.Label(mainframe, textvariable=self.base_experience).grid(column=1, row=2, sticky='nw', rowspan=1, padx=5)

        # Weight Row
        ttk.Label(mainframe, text="Weight: ").grid(column=0, row=3, sticky='w')
        ttk.Label(mainframe, textvariable=self.weight).grid(column=1, row=3, sticky='nw', rowspan=1, padx=5)

        # Height Row
        ttk.Label(mainframe, text="Height: ").grid(column=0, row=4, sticky='w')
        ttk.Label(mainframe, textvariable=self.height).grid(column=1, row=4, sticky='nw', rowspan=1, padx=5)

        # Image Section
        self.c = tk.Canvas(mainframe, relief='raised', width=20, height=20)
        self.c.grid(row=0, column=3, rowspan=4, columnspan=2)
        self.c.create_image(20, 20, image=self.gif, anchor='nw')

        # Search Frame - Beneath
        sub_frame = ttk.Frame(self.master, padding="3 3 12 12")
        sub_frame.pack(expand=True)

        self.pokemon_name = ttk.Entry(sub_frame, textvariable=self.search)
        self.pokemon_name.grid(column=1, row=0, sticky='w')
        ttk.Button(sub_frame, text="Search", command=self.get_pokemon_details_from_database) \
            .grid(column=3, row=0, sticky=('e', 'w', 'n', 's'))

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

    def get_pokemon_details_from_database(self):
        if self.database_manager.check_if_database_has(str(self.pokemon_name)) is False:
            new_pokemon = query_pokemon_api_for_pokemon_named(str(self.pokemon_name))
            self.database_manager.add_to_db(new_pokemon)

        # search db for pokemon, if failed presents popup message
        try:
            session = self.database_manager._sessionmaker()
            pokemon = session.query(Pokemon).filter(Pokemon.name == self.pokemon_name.get()).scalar()
            print(pokemon)
            self.name.set(pokemon.name)
            self.id.set(pokemon.id)
            self.base_experience.set(pokemon.base_xp)
            self.weight.set(pokemon.weight)
            self.height.set(pokemon.height)
            self.imageUrl.set(pokemon.sprite_url)
        except AttributeError as e:
            messagebox.showerror("Error", e)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
