import tkinter as tk
import subprocess

class Choose:
    def __init__(self, master):
        self.master = master
        self.master.title("E-Lucky Pick")

        # Set background color
        self.master.configure(bg="#333")

        # Create and pack labels
        tk.Label(self.master, text="Welcome to the Lucky App!", font=("Helvetica", 16), bg="#333", fg="white").pack(pady=20)
        tk.Label(self.master, text="Choose an option below:", bg="#333", fg="white").pack()

        # Create and pack buttons
        tk.Button(self.master, text="Run Lucky Pick", command=self.run_lucky_pick, bg="#555", fg="white").pack(pady=10)
        tk.Button(self.master, text="Run Lucky Color", command=self.run_lucky_color, bg="#555", fg="white").pack(pady=10)

        # Exit button
        tk.Button(self.master, text="Exit", command=self.close_window, bg="#555", fg="white").pack(pady=10)

    def run_lucky_pick(self):
        subprocess.Popen(["python3", "/home/hao/Documents/BP/lucky_pick.py"])
        self.master.after(100, self.close_window)  # Close the window after 100 milliseconds

    def run_lucky_color(self):
        subprocess.Popen(["python3", "/home/hao/Documents/BP/lucky_color.py"])
        self.master.after(100, self.close_window)  # Close the window after 100 milliseconds

    def close_window(self):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Choose(root)
    root.mainloop()
