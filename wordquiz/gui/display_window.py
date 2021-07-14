import tkinter as tk


class DisplayWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Word Quiz v0.1")
        self.window.geometry("400x400")

        self.correct_answer = -1
        self.sel = tk.IntVar()
        self.label = tk.Label(self.window)

    def open_window(self):
        self.new_screen(["hogi", "hogu", "hoge", "hogo"], 2)
        self.window.mainloop()

    def select_action(self):
        selection = str(self.sel.get())
        self.label.config(text=selection)

    def new_screen(self, option_list, correct_answer):
        self.correct_answer = correct_answer
        self.sel.set(-1)

        if len(option_list) != 4:
            raise Exception("The number of options for each question must be 4.")

        radio_0 = tk.Radiobutton(self.window, text=option_list[0], variable=self.sel, value=0,
                                 command=self.select_action)
        radio_0.pack()

        radio_1 = tk.Radiobutton(self.window, text=option_list[1], variable=self.sel, value=1,
                                 command=self.select_action)
        radio_1.pack()

        radio_2 = tk.Radiobutton(self.window, text=option_list[2], variable=self.sel, value=2,
                                 command=self.select_action)
        radio_2.pack()

        radio_3 = tk.Radiobutton(self.window, text=option_list[3], variable=self.sel, value=3,
                                 command=self.select_action)
        radio_3.pack()

        self.label.pack()


