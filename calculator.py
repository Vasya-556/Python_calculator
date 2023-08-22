import tkinter as tk
import tkinter.font as tkFont
from tkinter import StringVar

def calc():
    global expression
    try:
        if "%" in expression:
            parts = expression.split("+")
            value = float(parts[0])
            percentage = float(parts[1].replace('%', '')) * 0.01
            result = value + value * percentage
            expression_var.set(result)
        else:
            result = eval(expression)
            expression_var.set(result) 
    except Exception as e:
        expression_var.set("error")
    finally:
        expression = ""
    
def add_symbol(symbol):
    global expression
    expression += symbol
    expression_var.set(expression)

def clear():
    global expression
    expression = ""
    expression_var.set("")
    
def erase():
    global expression
    if len(expression) > 0:
        expression = expression[:-1]
        expression_var.set(expression)

def main():
    global expression_var
    global expression

    window = tk.Tk()
    window.title("Calculator")
    window.geometry("225x320")

    #string for expression
    expression = ""
    expression_var = StringVar()


    #frame for buttons
    frame = tk.Frame()

    #field for expression
    res = tk.Entry(window, textvariable=expression_var)
    res.grid(row=0, column=0, sticky="nsew", columnspan=1)

    #initializating numbers
    btn_0 = tk.Button(text=0,master=frame, width=5,height=3, command=lambda: add_symbol('0'))
    
    btn_1 = tk.Button(text=1,master=frame, width=5,height=3, command=lambda: add_symbol('1'))
    btn_2 = tk.Button(text=2,master=frame, width=5,height=3, command=lambda: add_symbol('2'))
    btn_3 = tk.Button(text=3,master=frame, width=5,height=3, command=lambda: add_symbol('3'))
    
    btn_4 = tk.Button(text=4,master=frame, width=5,height=3, command=lambda: add_symbol('4'))
    btn_5 = tk.Button(text=5,master=frame, width=5,height=3, command=lambda: add_symbol('5'))
    btn_6 = tk.Button(text=6,master=frame, width=5,height=3, command=lambda: add_symbol('6'))
    
    btn_7 = tk.Button(text=7,master=frame, width=5,height=3, command=lambda: add_symbol('7'))
    btn_8 = tk.Button(text=8,master=frame, width=5,height=3, command=lambda: add_symbol('8'))
    btn_9 = tk.Button(text=9,master=frame, width=5,height=3, command=lambda: add_symbol('9'))

    #initializating operators
    #p - plus, m - minus, d - divive, mm - multiply, dd - dot, c - clear, ddd - degre, pp - percentage, r - right, e - equal
    #ee - erase, s - square, cc - cube, rs - root square, l - left
    btn_p = tk.Button(text="+",master=frame,width=5,height=3, command=lambda: add_symbol('+'))
    btn_m = tk.Button(text="-",master=frame,width=5,height=3, command=lambda: add_symbol('-'))
    btn_d = tk.Button(text="/",master=frame,width=5,height=3, command=lambda: add_symbol('/'))
    
    btn_mm = tk.Button(text="*",master=frame,width=5,height=3, command=lambda: add_symbol('*'))
    btn_dd = tk.Button(text=".",master=frame,width=5,height=3, command=lambda: add_symbol('.'))
    btn_c = tk.Button(text="C",master=frame,width=5,height=3, command=lambda: clear())

    btn_ddd = tk.Button(text="x^n",master=frame,width=5,height=3, command=lambda: add_symbol('**'))
    btn_pp = tk.Button(text="%",master=frame,width=5,height=3, command=lambda: add_symbol('%'))
    btn_r = tk.Button(text=")",master=frame,width=5,height=3, command=lambda: add_symbol(')'))

    btn_e = tk.Button(text="=",master=frame,width=5,height=3, command=lambda: calc())
    btn_ee = tk.Button(text="<x",master=frame,width=5,height=3, command=lambda: erase())
    btn_s = tk.Button(text="x^2",master=frame,width=5,height=3, command=lambda: add_symbol('**2'))
    
    btn_cc = tk.Button(text="x^3",master=frame,width=5,height=3, command=lambda: add_symbol('**3'))
    btn_rs = tk.Button(text="√x",master=frame,width=5,height=3, command=lambda: add_symbol('**(1/2)'))
    btn_l = tk.Button(text="(",master=frame,width=5,height=3, command=lambda: add_symbol('('))

    #griding for buttons
    btn_1.grid(row=3,column=0)
    btn_2.grid(row=3,column=1)
    btn_3.grid(row=3,column=2)
    
    btn_4.grid(row=2,column=0)
    btn_5.grid(row=2,column=1)
    btn_6.grid(row=2,column=2)
    
    btn_7.grid(row=1,column=0)
    btn_8.grid(row=1,column=1)
    btn_9.grid(row=1,column=2)

    btn_p.grid(row=3,column=3)
    btn_m.grid(row=3,column=4)
    btn_d.grid(row=4,column=3)

    btn_mm.grid(row=2,column=4)
    btn_dd.grid(row=4,column=2)
    btn_c.grid(row=0,column=3)

    btn_ddd.grid(row=2,column=3)
    btn_pp.grid(row=4,column=0)
    btn_r.grid(row=0,column=2)

    btn_e.grid(row=4,column=4)
    btn_ee.grid(row=0,column=4)
    btn_0.grid(row=4,column=1)

    btn_s.grid(row=1,column=3)
    btn_cc.grid(row=1,column=4)
    btn_rs.grid(row=0,column=0)
    
    btn_l.grid(row=0,column=1)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0,weight=2)

    #change font in res field
    font = tkFont.Font(size=18)
    res["font"] = font

    #add numbers and symbols
    frame.grid(row=1,column=0)
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()