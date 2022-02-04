
import tkinter as tk
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LABEL_COLOR = "#25265E"
LIGHT_GREY = "#F5F5F5"
WHITE = "#CCEDFF"
OFF_WHITE = "#F8FAFF"
DEFAULT_FONT_STYLE = ("Arial", 20)
class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("CALCULATOR")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()


        self.total_label, self.current_label = self.display_label()

        self.button_frame = self.create_button_frame()

        self.digits = {"7": (1, 1), 8: (1, 2), 9: (1, 3),

                       4: (2, 1), 5: (2, 2), 6: (2, 3),

                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), ".": (4, 1)}

        self.operations = {"/": "\u00F7", "*": "\u00D7" , "-": "-", "+": "+"}

        for x in range(0, 5):
            self.button_frame.rowconfigure(x, weight=1)
        for x in range(1,5):
            self.button_frame.columnconfigure(x,weight=1)


        self.create_digits_buttons()
        self.create_operations_button()
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digits=key: self.button_clicked(digits))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.operations_clicked(operator))

    def sqrt(self):
        self.current_expression= str(eval(f"{self.current_expression}**0.5"))
        self.update_current_label()

    def create_sqrt_button(self):
        button= tk.Button(self.button_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                          borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)



    def sqr(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_current_label()

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqr)
        button.grid(row=0,column=2,sticky=tk.NSEW)

    def clear_button_clicked(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="c",bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE
                           , borderwidth=0, command=lambda: self.clear_button_clicked())
        button.grid(row=0, column=1, sticky=tk.NSEW )


    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Not defined"
        finally:
            self.update_current_label()





    def create_equal_button(self):
        button = tk.Button(self.button_frame, text="=", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)


    def create_operations_button(self):
        i = 0
        for operators, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=str(symbol), bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE,borderwidth=0, command=lambda x=operators: self.operations_clicked(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1


    def operations_clicked(self,operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()






    def button_clicked(self,number):
        self.current_expression +=str(number)
        self.update_current_label()

    def create_digits_buttons(self):
        for digits, grid_value in self.digits.items():

            button = tk.Button(self.button_frame, text=str(digits), bg=WHITE, fg=LABEL_COLOR,borderwidth=0,
                               font=DIGIT_FONT_STYLE, command=lambda y=digits : self.button_clicked(y))
            button.grid(row=grid_value[0], column=grid_value[1],  sticky=tk.NSEW)





    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GREY,borderwidth=0)
        frame.pack(expand=True, fill="both")
        return frame

    def display_label(self):
        total_label = tk.Label(self.display_frame, text= self.total_expression, anchor=tk.E,bg= LIGHT_GREY,
                               fg=LABEL_COLOR,padx=20, font=SMALL_FONT_STYLE)
        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GREY,
                                 fg=LABEL_COLOR, padx=20, font=LARGE_FONT_STYLE)
        total_label.pack(expand= True, fill="both")
        current_label.pack(expand= True, fill="both")
        return total_label, current_label


    def create_button_frame(self):
        frame = tk.Button(self.window,pady=120,borderwidth=0)

        frame.pack(expand= True, fill="both")
        return frame
    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:11])

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
