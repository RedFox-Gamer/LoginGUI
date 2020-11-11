from tkinter import *
from tkinter import ttk

window = Tk()

U,P = StringVar(), StringVar()
U2,P2 = StringVar(), StringVar()
#Define the user's credentials
def check_data():
    if U.get() == 'Adam' and P.get() == 'Stark':
        print("Successful login!")
    else:
        print("Login failed! Check your Username/Password")

ttk.Label(window, text = "Username: ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "Password: ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = U).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = P, show = "*").grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)
window.mainloop()