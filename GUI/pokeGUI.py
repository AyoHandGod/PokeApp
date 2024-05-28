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
from Models import pokeQuery, Pokemon


class App(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        master.title("Pokebase")
        master.configure(background="#efefef", height=60, width=60, highlightbackground="blue", highlightthickness=1)

        # Pokemon Details
        self.search = tk.StringVar()
        self.id = tk.IntVar()
        self.name = tk.StringVar()
        self.base_experience = tk.IntVar()
        self.weight = tk.IntVar()
        self.height = tk.IntVar()
        self.image_url = ""
        self.gif = Image.open('pokeimage.png')

        # DB Manager
        self.database_manager = DatabaseManager(database_name="test2")

        # Create Window
        self._create_widgets()

    def _create_widgets(self):
        # main frame
        self.mainframe = ttk.Frame(self.master)
        self.mainframe.pack(anchor='w', expand=True)

        # Name Row
        ttk.Label(self.mainframe, text="Name: ").grid(column=0, row=0, sticky='NSEW')
        ttk.Label(self.mainframe, textvariable=self.name).grid(column=1, row=0, sticky='NSEW', padx=5)

        # ID Row
        ttk.Label(self.mainframe, text="ID: ").grid(column=0, row=1, sticky='NSEW')
        ttk.Label(self.mainframe, textvariable=self.id).grid(column=1, row=1, sticky='NSEW', padx=5)

        # XP Row
        ttk.Label(self.mainframe, text="Base Experience: ").grid(column=0, row=2, sticky='NSEW')
        ttk.Label(self.mainframe, textvariable=self.base_experience).grid(column=1, row=2, sticky='NSEW',
                                                                          padx=5)

        # Weight Row
        ttk.Label(self.mainframe, text="Weight: ").grid(column=0, row=3, sticky='NSEW')
        ttk.Label(self.mainframe, textvariable=self.weight).grid(column=1, row=3, sticky='NSEW', padx=5)

        # Height Row
        ttk.Label(self.mainframe, text="Height: ").grid(column=0, row=4, sticky='NSEW')
        ttk.Label(self.mainframe, textvariable=self.height).grid(column=1, row=4, sticky='NSEW', padx=5)

        # Search Frame - Beneath
        sub_frame = ttk.Frame(self.master, padding="3 3 12 12")
        sub_frame.pack(expand=True)

        self.pokemon_name = ttk.Entry(sub_frame, textvariable=self.search)
        self.pokemon_name.grid(column=1, row=0, sticky='NSEW')
        ttk.Button(sub_frame, text="Search", command=self.get_pokemon_details_from_database) \
            .grid(column=3, row=0, sticky='NSEW')

    def image_grab(self):

        image_response = requests.get(self.image_url)
        self.gif = Image.open(BytesIO(image_response.content))

        # Image Section
        tkpic = ImageTk.PhotoImage(self.gif)
        img = ttk.Label(self.mainframe, image=tkpic)
        img.image = tkpic
        img.grid(column=2, row=0, rowspan=4)

    def get_pokemon_details_from_database(self):
        target_pokemon = self.pokemon_name.get()
        if self.database_manager.check_if_database_has(str(target_pokemon)) is False:
            print("executed")
            new_pokemon = pokeQuery(str(target_pokemon))
            self.database_manager.add_to_db(new_pokemon)

        # search db for pokemon, if failed presents popup message
        try:
            session = self.database_manager._sessionmaker()
            pokemon = session.query(Pokemon).filter(Pokemon.name == self.pokemon_name.get()).scalar()
            print(pokemon)
            self.name.set(pokemon.name.title())
            self.id.set(pokemon.id)
            self.base_experience.set(pokemon.base_xp)
            self.weight.set(pokemon.weight)
            self.height.set(pokemon.height)
            self.image_url = pokemon.image
            self.image_grab()
        except AttributeError as e:
            messagebox.showerror("Error", e)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
