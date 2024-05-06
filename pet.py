import tkinter as tk
import time

class ComplexTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Complex Timer with Virtual Pet")

        # Set window to full screen
        master.attributes('-fullscreen', True)
        master.bind('<Escape>', self.exit_fullscreen)

        # Variables
        self.time_left = 0
        self.timer_running = False

        # GUI Elements
        self.main_frame = tk.Frame(master, bg='lightblue')
        self.main_frame.pack(expand=True, fill='both')

        self.exit_button = tk.Button(self.main_frame, text="Exit (Q)", font=("Arial", 18), command=self.exit_fullscreen)
        self.exit_button.pack(padx=10, pady=10, anchor="nw")

        self.pet_label = tk.Label(self.main_frame, text="(っ- ‸ - ς)ᶻ 𝗓 𐰁", font=("Arial", 72), bg='lightblue')
        self.pet_label.pack(expand=True)

        self.timer_label = tk.Label(self.main_frame, text="00:00", font=("Arial", 72), bg='lightblue')
        self.timer_label.pack(pady=50)

        self.timer_text_label = tk.Label(self.main_frame, text="Timer:", font=("Arial", 24), bg='lightblue')
        self.timer_text_label.pack()

        self.custom_time_entry = tk.Entry(self.main_frame, font=("Arial", 24))
        self.custom_time_entry.pack(pady=10)

        self.btn_start = tk.Button(self.main_frame, text="Start", font=("Arial", 24), command=self.start_timer)
        self.btn_start.pack(pady=10)

        self.btn_pause = tk.Button(self.main_frame, text="Pause", font=("Arial", 24), command=self.pause_timer)
        self.btn_pause.pack(pady=10)

        self.btn_reset = tk.Button(self.main_frame, text="Reset", font=("Arial", 24), command=self.reset_timer)
        self.btn_reset.pack(pady=10)

        # Initialize emoji label
        self.emoji_label = tk.Label(self.main_frame, text="", font=("Arial", 72), bg='lightblue')
        self.emoji_label.pack()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_left = int(self.custom_time_entry.get()) if self.custom_time_entry.get() else 300  # default to 5 minutes

            while self.time_left > 0 and self.timer_running:
                # Update timer display
                minutes, seconds = divmod(self.time_left, 60)
                time_format = '{:02d}:{:02d}'.format(minutes, seconds)
                self.timer_label.config(text=time_format)
                self.master.update()
                time.sleep(1)
                self.time_left -= 1

            # Timer is finished
            if self.timer_running:
                self.timer_label.config(text="(ಠ.ಠ)")
                self.emoji_label.config(text="♡⸜(˶˃ ᵕ ˂˶)⸝♡")
                self.master.update()
                time.sleep(2)  # Display "(ಠ.ಠ)" for 2 seconds
                self.reset_timer()

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_left = 0
        self.timer_label.config(text="00:00")
        self.custom_time_entry.delete(0, tk.END)

    def exit_fullscreen(self, event=None):
        self.master.attributes('-fullscreen', False)

def main():
    root = tk.Tk()
    timer_app = ComplexTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
