import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x450")
        self.root.resizable(False, False)
        
        # Create display frame
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        display_font = font.Font(size=24)
        self.display = tk.Entry(
            root, textvariable=self.display_var, 
            font=display_font, bd=10, insertwidth=2,
            width=14, borderwidth=4, justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # Span 4 columns
        ]
        
        # Create buttons
        button_font = font.Font(size=18, weight='bold')
        for btn in buttons:
            text = btn[0]
            if len(btn) == 4:  # For the '=' button that spans columns
                button = tk.Button(
                    root, text=text, padx=20, pady=20, font=button_font,
                    command=lambda t=text: self.on_button_click(t)
                )
                button.grid(row=btn[1], column=btn[2], columnspan=btn[3], sticky="nsew")
            else:
                button = tk.Button(
                    root, text=text, padx=20, pady=20, font=button_font,
                    command=lambda t=text: self.on_button_click(t)
                )
                button.grid(row=btn[1], column=btn[2])
        
        # Configure grid weights
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        self.current_input = ""
        self.operation = None
        self.first_number = 0
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.handle_digit(button_text)
        elif button_text == 'C':
            self.clear()
        elif button_text == '=':
            self.calculate()
        else:
            self.handle_operator(button_text)
    
    def handle_digit(self, digit):
        if self.display_var.get() == "0" and digit != '.':
            self.current_input = digit
        else:
            if digit == '.' and '.' in self.current_input:
                return  # Prevent multiple decimal points
            self.current_input += digit
        self.display_var.set(self.current_input)
    
    def handle_operator(self, operator):
        if self.current_input:
            self.first_number = float(self.current_input)
            self.operation = operator
            self.current_input = ""
            self.display_var.set(operator)
    
    def calculate(self):
        if self.operation and self.current_input:
            second_number = float(self.current_input)
            try:
                if self.operation == '+':
                    result = self.first_number + second_number
                elif self.operation == '-':
                    result = self.first_number - second_number
                elif self.operation == '*':
                    result = self.first_number * second_number
                elif self.operation == '/':
                    if second_number == 0:
                        raise ZeroDivisionError
                    result = self.first_number / second_number
                
                # Display result
                self.display_var.set(str(result))
                self.current_input = str(result)
                self.operation = None
                self.first_number = 0
            except ZeroDivisionError:
                self.display_var.set("Error: Division by zero")
                self.current_input = ""
                self.operation = None
    
    def clear(self):
        self.current_input = ""
        self.operation = None
        self.first_number = 0
        self.display_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()