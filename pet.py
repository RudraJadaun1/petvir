import tkinter as tk
from tkinter import ttk
import time
import random

class ComplexTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Kitchen Timer with Virtual Pet")

        # Variables
        self.total_seconds = 0
        self.timer_interval = None

        # GUI Elements
        self.container = tk.Frame(master, bg='lightblue')
        self.container.pack(expand=True, fill='both')

        self.clock_label = tk.Label(self.container, text="00:00", font=("Arial", 32), bg='lightblue')
        self.clock_label.pack(pady=20)

        self.title_label = tk.Label(self.container, text="Kitchen Timer", font=("Arial", 24), bg='lightblue')
        self.title_label.pack()

        self.pet_label = tk.Label(self.container, text="(>^_^<)", font=("Arial", 64), bg='lightblue')
        self.pet_label.pack(pady=20)

        self.timer_display_label = tk.Label(self.container, text="00:00", font=("Arial", 32), bg='lightblue')
        self.timer_display_label.pack()

        self.timer_controls_frame = tk.Frame(self.container, bg='lightblue')
        self.timer_controls_frame.pack(pady=20)

        self.timer_slider = ttk.Scale(self.timer_controls_frame, from_=0, to=120, orient='horizontal', length=300, command=self.update_timer_display)
        self.timer_slider.pack(side=tk.LEFT, padx=10)

        self.start_btn = tk.Button(self.timer_controls_frame, text="Start", font=("Arial", 16), command=self.start_timer)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.pause_btn = tk.Button(self.timer_controls_frame, text="Pause", font=("Arial", 16), command=self.pause_timer)
        self.pause_btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(self.timer_controls_frame, text="Reset", font=("Arial", 16), command=self.reset_timer)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

        self.quit_btn = tk.Button(self.container, text="Quit", font=("Arial", 16), command=self.quit_app)
        self.quit_btn.pack(pady=20)

        self.update_timer_display()

    def update_clock_display(self):
        minutes = int(self.total_seconds // 60)
        seconds = int(self.total_seconds % 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        self.clock_label.config(text=time_format)

    def update_timer_display(self, event=None):
        self.total_seconds = self.timer_slider.get() * 60
        self.update_clock_display()
        self.timer_display_label.config(text=self.clock_label.cget("text"))

    def update_pet_face(self):
        faces = ['(^_^)', '(>.<)', '(-_-)', '(^o^)']
        random_index = random.randint(0, len(faces)-1)
        self.pet_label.config(text=faces[random_index])

    def start_timer(self):
        if self.timer_interval is None:
            self.total_seconds = self.timer_slider.get() * 60
            self.timer_interval = self.master.after(1000, self.update_timer)

    def update_timer(self):
        self.total_seconds -= 1
        self.update_clock_display()
        self.update_pet_face()
        self.timer_display_label.config(text=self.clock_label.cget("text"))

        if self.total_seconds <= 0:
            self.master.after_cancel(self.timer_interval)
            self.timer_interval = None
            self.total_seconds = 0
            tk.messagebox.showinfo("Time's Up!", "Time is up!")
            self.reset_timer()
        else:
            self.timer_interval = self.master.after(1000, self.update_timer)

    def pause_timer(self):
        if self.timer_interval is not None:
            self.master.after_cancel(self.timer_interval)
            self.timer_interval = None

    def reset_timer(self):
        self.total_seconds = 0
        self.timer_slider.set(0)
        self.update_timer_display()
        self.update_pet_face()

    def quit_app(self, event=None):
        self.master.quit()

def main():
    root = tk.Tk()
    timer_app = ComplexTimerApp(root)
    root.configure(bg='lightblue')  # Set background color to match the container's background

    # Set window size to fit a phone screen and maximize
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    phone_screen_width = int(screen_width * 0.8)  # Adjust as needed
    phone_screen_height = int(screen_height * 0.8)  # Adjust as needed
    root.geometry(f"{phone_screen_width}x{phone_screen_height}+{int((screen_width - phone_screen_width) / 2)}+{int((screen_height - phone_screen_height) / 2)}")

    root.bind('q', timer_app.quit_app)  # Bind 'Q' key to exit the application
    root.attributes("-fullscreen", True)  # Make the app full-screen
    root.mainloop()

if __name__ == "__main__":
    main()
