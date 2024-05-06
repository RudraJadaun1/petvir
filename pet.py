import tkinter as tk
import time

class CookPetTimer:
    def __init__(self, master):
        self.master = master
        master.title("Cook Pet Timer")

        # Variables
        self.timer_running = False
        self.time_left = 0

        # GUI Elements
        self.label_timer = tk.Label(master, text="00:00", font=("Arial", 24))
        self.label_timer.pack()

        self.btn_start = tk.Button(master, text="Start", command=self.start_timer)
        self.btn_start.pack(side=tk.LEFT, padx=10)

        self.btn_stop = tk.Button(master, text="Stop", command=self.stop_timer)
        self.btn_stop.pack(side=tk.LEFT, padx=10)

        self.btn_reset = tk.Button(master, text="Reset", command=self.reset_timer)
        self.btn_reset.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_left = 300  # 5 minutes

            while self.time_left > 0 and self.timer_running:
                minutes, seconds = divmod(self.time_left, 60)
                time_format = '{:02d}:{:02d}'.format(minutes, seconds)
                self.label_timer.config(text=time_format)
                self.master.update()
                time.sleep(1)
                self.time_left -= 1

            # Timer is finished
            if self.timer_running:
                self.label_timer.config(text="Time's up!")
                self.master.update()
                time.sleep(2)  # Display "Time's up!" for 2 seconds
                self.reset_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 0
        self.label_timer.config(text="00:00")

def main():
    root = tk.Tk()
    timer_app = CookPetTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
