import tkinter as tk
from tkinter import StringVar

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("eror")
        print("eror")
    finally:
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")
# f - function 0 - 9 = create numbers p - plus, m - minus, d - divide, dd - dot, mm - multiply, e - equal(end + show result)

# def f1():
#     result.append(1)
#     lbl_res["text"] = result
# def f2():
#     result.append(2)
#     lbl_res["text"] = result
# def f3():
#     result.append(3)
#     lbl_res["text"] = result
# def f4():
#     result.append(4)
#     lbl_res["text"] = result
# def f5():
#     result.append(5)
#     lbl_res["text"] = result
# def f6():
#     result.append(6)
#     lbl_res["text"] = result
# def f7():
#     result.append(7)
#     lbl_res["text"] = result
# def f8():
#     result.append(8)
#     lbl_res["text"] = result
# def f9():
#     result.append(9)
#     lbl_res["text"] = result
# def f0():
#     result.append(0)
#     lbl_res["text"] = result
# def fp():
#     result.append("+")
#     lbl_res["text"] = result
# def fm():
#     result.append("-")
#     lbl_res["text"] = result
# def fmm():
#     result.append("*")
#     lbl_res["text"] = result
# def fd():
#     result.append("/")
#     lbl_res["text"] = result
# def fdd():
#     result.append(",")
#     lbl_res["text"] = result
# def fe():
#     print(result)
#     a = 0
#     b = 0
#     result2 = None
#     for i in result:
#         if i.isdigit():
#             a = float(i)
#             result.remove(i)
#             break
#
#     for i in result:
#         if i.isdigit():
#             b = float(i)
#             result.remove(i)
#             break
#
#     for i in result:
#         if i == "+":
#             result2 = add(a + b)
#             lbl_res["text"] = result2


window = tk.Tk()
window.title("Simple calculator")
window.geometry("280x280")

equation = StringVar()



frm_numb = tk.Frame()

frm_operation = tk.Frame()

res = tk.Entry(window, textvariable=equation)
res.grid(row=0,column=0, sticky= "NSEW",ipadx=70,columnspan=4)

btn_1 = tk.Button(text="1",master=frm_numb, width=3,height=3, command=lambda: press(1))
btn_2 = tk.Button(text="2",master=frm_numb, width=3,height=3, command=lambda: press(2))
btn_3 = tk.Button(text="3",master=frm_numb, width=3,height=3, command=lambda: press(3))
btn_4 = tk.Button(text="4",master=frm_numb, width=3,height=3, command=lambda: press(4))
btn_5 = tk.Button(text="5",master=frm_numb, width=3,height=3, command=lambda: press(5))
btn_6 = tk.Button(text="6",master=frm_numb, width=3,height=3, command=lambda: press(6))
btn_7 = tk.Button(text="7",master=frm_numb, width=3,height=3, command=lambda: press(7))
btn_8 = tk.Button(text="8",master=frm_numb, width=3,height=3, command=lambda: press(8))
btn_9 = tk.Button(text="9",master=frm_numb, width=3,height=3, command=lambda: press(9))
btn_0 = tk.Button(text="0",master=frm_numb, width=3,height=3, command=lambda: press(0))

btn_9.grid(row=0,column=0)
btn_8.grid(row=0,column=1)
btn_7.grid(row=0,column=2)
btn_6.grid(row=1,column=0)
btn_5.grid(row=1,column=1)
btn_4.grid(row=1,column=2)
btn_3.grid(row=2,column=0)
btn_2.grid(row=2,column=1)
btn_1.grid(row=2,column=2)
btn_0.grid(row=3,column=1)

#p - plus, m - minus, mm - mulitply, d - divide, dd - dot, c - clear
btn_e = tk.Button(text="=",master=frm_numb,width=3,height=3,command=equalpress)
btn_p = tk.Button(text="+",master=frm_operation, width=3,height=3, command=lambda: press("+"))
btn_m = tk.Button(text="-",master=frm_operation, width=3,height=3, command=lambda: press("-"))
btn_mm = tk.Button(text="*",master=frm_operation, width=3,height=3, command=lambda: press("*"))
btn_d = tk.Button(text="/",master=frm_operation, width=3,height=3, command=lambda: press("/"))
btn_dd = tk.Button(text=",",master=frm_numb, width=3,height=3, command=lambda: press("."))
btn_c = tk.Button(text="Clear", master=frm_operation,width=3,height=3,command=clear)

btn_p.grid(row=0,column=0)
btn_m.grid(row=1,column=0)
btn_mm.grid(row=0,column=1)
btn_d.grid(row=1,column=1)
btn_dd.grid(row=3,column=0)
btn_e.grid(row=3,column=2)
btn_c.grid(row=2,column=0)

frm_numb.grid(row=1,column=0)
frm_operation.grid(row=1,column=1,sticky="W")

window.mainloop()