import tkinter as tk
import api


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("400x400")

        self.total = tk.StringVar()
        self.result = ''

        self.entry = tk.Entry(master, textvariable=self.total, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ['sin', 'cos', 'tan', 'e^', '^'],
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', '('],
            ['0', 'C', '=', '+', ')']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)
        for i in range(5):
            self.master.columnconfigure(i, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                self.result = self.total.get()
                evaluated_result = api.send_input(self.result)
                self.total.set(evaluated_result)
            except Exception as e:
                self.total.set("Error")
        elif button_text == 'C':
            self.result = ''
            self.total.set('')
        else:
            self.result += button_text
            self.total.set(self.result)
