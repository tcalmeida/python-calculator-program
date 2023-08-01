from tkinter import *


def button_press(number):
    global display_text
    display_text += str(number)
    display_label.set(display_text)


def result():
    global display_text

    try:
        total = str(eval(display_text))
        display_label.set(total)
        display_text = total

    except ZeroDivisionError:
        display_label.set("Can't divide by zero")
        display_text = ''

    except SyntaxError:
        display_label.set("Syntax Error")
        display_text = ''


def reset():
    global display_text

    display_label.set('')
    display_text = ''


window = Tk()
window.title('Calculator')
window.geometry('500x500')

display_text = ""
display_label = StringVar()

label = Label(window, textvariable=display_label, font=('Arial ', 20), bg='white', width=24, height=2, pady=5)
label.pack(pady=10)

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, width=9, height=4, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, width=9, height=4, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, width=9, height=4, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, width=9, height=4, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, width=9, height=4, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, width=9, height=4, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, width=9, height=4, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, width=9, height=4, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, width=9, height=4, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, width=9, height=4, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus_button = Button(frame, text='+', width=9, height=4, font=35, command=lambda: button_press('+'))
plus_button.grid(row=0, column=3)

subtraction_button = Button(frame, text='-', width=9, height=4, font=35, command=lambda: button_press('-'))
subtraction_button.grid(row=1, column=3)

multiplication_button = Button(frame, text='*', width=9, height=4, font=35, command=lambda: button_press('*'))
multiplication_button.grid(row=2, column=3)

division_button = Button(frame, text='/', width=9, height=4, font=35, command=lambda: button_press('/'))
division_button.grid(row=3, column=3, padx=8)

equal_button = Button(frame, text='=', width=9, height=4, font=35, command=lambda: result())
equal_button.grid(row=3, column=2)

decimal_button = Button(frame, text='.', width=9, height=4, font=35, command=lambda: button_press('.'))
decimal_button.grid(row=3, column=1)

clear_button = Button(window, text='clear', width=12, height=4, font=40, command=lambda: reset())
clear_button.pack(pady=15)

window.mainloop()
