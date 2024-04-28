import sys
import os
import random
import pygame
import tkinter as tk
import subprocess

class ColorPickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lucky Pick")
        self.master.geometry("490x300")  # Adjusted screen size
        self.master.configure(bg="#333")  # Set background color to dark shade

        self.colors = ["black"] * 49 + ["pink"] * 49 + ["yellow"] * 2

        # Adjusted height of the labels to make them equal
        label_height = 3

        self.label1 = tk.Label(master, bg="#333", fg="white", width=6, height=label_height)  # Adjusted width and height of the labels
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.label1.grid_columnconfigure(0, weight=1, uniform="result_label")  # Make width uniform

        self.label2 = tk.Label(master, bg="#333", fg="white", width=6, height=label_height)  # Adjusted width and height of the labels
        self.label2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        self.label2.grid_columnconfigure(0, weight=1, uniform="result_label")  # Make width uniform

        self.label3 = tk.Label(master, bg="#333", fg="white", width=6, height=label_height)  # Adjusted width and height of the labels
        self.label3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        self.label3.grid_columnconfigure(0, weight=1, uniform="result_label")  # Make width uniform

        self.master.grid_rowconfigure(0, weight=1)  # Make row 0 stretchable
        self.master.grid_columnconfigure((0, 1, 2), weight=1)  # Make columns 0, 1, 2 stretchable

        self.volume_scale = tk.Scale(master, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=self.set_volume)
        self.volume_scale.grid(row=1, column=0, columnspan=3, pady=5, padx=5, sticky="ew")

        self.spin_button = tk.Button(master, text="Spin", command=self.spin)
        self.spin_button.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.back_button = tk.Button(master, text="Back", command=self.back_to_choose)
        self.back_button.grid(row=2, column=2, padx=5, pady=10, sticky="ew")

        self.volume = 0.5  # Initial volume

    def flash_labels(self):
        # Define colors for flashing effect
        flash_colors = ["red", "blue", "green", "orange", "purple"]

        # Flash labels with random colors for a short duration
        for _ in range(5):
            self.label1.config(bg=random.choice(flash_colors))
            self.label2.config(bg=random.choice(flash_colors))
            self.label3.config(bg=random.choice(flash_colors))
            self.master.update_idletasks()  # Update the GUI
            self.master.after(100)  # Pause briefly

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load("/home/hao/Documents/BP/lucky_for_the_win.wav")  # Replace "your_sound_file.wav" with your sound file path
        pygame.mixer.music.play()

    def set_volume(self, value):
        self.volume = float(value)

    def spin(self):
        self.play_sound()  # Add sound effect
        self.flash_labels()  # Add flashing effect
        picked_colors = random.sample(self.colors, 3)
        self.label1.config(bg=picked_colors[0])
        self.label2.config(bg=picked_colors[1])
        self.label3.config(bg=picked_colors[2])

    def reset(self):
        self.label1.config(bg="#333")
        self.label2.config(bg="#333")
        self.label3.config(bg="#333")

    def back_to_choose(self):
        self.master.withdraw()  # Hide the current window
        subprocess.Popen(["python3", "/home/hao/Documents/BP/choose.py"])  # Launch choose.py script

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
