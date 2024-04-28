import tkinter as tk
from tkinter import ttk
import random
import pygame
import subprocess

class ColorPickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lucky Color")
        self.master.configure(bg='#333333')  # Set background color of the root window to dark

        # Initialize pygame mixer
        pygame.mixer.init()

        # Random color display
        color_frame = tk.Frame(self.master, bg='#333333', highlightthickness=-2)  # Set background color of the frame to dark and slightly round the corners
        color_frame.pack(pady=15, padx=15)  # Add padx and pady for margin
        self.color_label = tk.Label(color_frame, text='', font=('Helvetica', 20), width=10, height=5, bg='#333333', fg='white',
                                bd=5, relief=tk.RIDGE)  # Set background and text color, add border
        self.color_label.pack()

        # Volume slider
        volume_frame = tk.Frame(self.master, bg='#333333')  # Set background color of the frame to dark
        volume_frame.pack(pady=15, padx=15)  # Add padx and pady for margin
        self.volume_slider = ttk.Scale(volume_frame, from_=0, to=100, orient='horizontal', command=self.update_volume, style='Horizontal.TScale')
        self.volume_slider.pack()

        # Spin button
        spin_frame = tk.Frame(self.master, bg='#333333')  # Set background color of the frame to dark
        spin_frame.pack(pady=15, padx=15)  # Add padx and pady for margin
        self.spin_button = tk.Button(spin_frame, text="Spin", command=self.spin, bg='#555555', fg='white', width=10, height=1, padx=10, pady=5)  # Set background and text color, and adjust size
        self.spin_button.pack()

        # Reset button
        reset_button = tk.Button(self.master, text="Reset", command=self.reset_color, bg='#555555', fg='white', width=10, height=1, padx=10, pady=5)  # Set background and text color, and adjust size
        reset_button.pack(pady=15, padx=15)  # Add padx and pady for margin

        # Back button
        back_button = tk.Button(self.master, text="Back to Choose", command=self.back_to_choose, bg='#555555', fg='white', width=15, height=1, padx=10, pady=5)  # Set background and text color, and adjust size
        back_button.pack(pady=15, padx=15)  # Add padx and pady for margin

        # Generate initial random color
        self.generate_random_color()

    def generate_random_color(self):
        colors = ['white', 'yellow', 'blue', 'green', 'red', 'pink']
        random_color = random.choice(colors)
        self.color_label.config(text='', bg=random_color)  # Set text to empty string

    def flash_color(self):
        for _ in range(5):  # Flash 5 times
            for color in ['white', 'yellow', 'blue', 'green', 'red', 'pink']:
                self.color_label.config(bg=color)
                self.master.update()
                self.master.after(10)  # Flash duration
        self.generate_random_color()  # Generate a random color after flashing

    def reset_color(self):
        self.color_label.config(text='', bg='white')
        self.volume_slider.set(50)
        self.spin_button.config(text='Spin')  # Resetting spin button text

    def spin(self):
        self.play_sound()  # Play sound when the spin button is clicked
        self.flash_color()  # Flash colors when the spin button is clicked
        self.master.after(10, self.generate_random_color)  # Wait for 1 second and generate random color

    def play_sound(self):
        pygame.mixer.music.load("/home/hao/Documents/BP/lucky_for_the_win.wav")
        pygame.mixer.music.play()

    def update_volume(self, value):
        pygame.mixer.music.set_volume(float(value) / 100)

    def back_to_choose(self):
        self.master.withdraw()  # Hide the current window
        subprocess.Popen(["python3", "/home/hao/Documents/BP/choose.py"])  # Launch choose.py script

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
