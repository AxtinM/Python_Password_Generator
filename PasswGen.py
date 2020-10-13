import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title('Password Generator')

ttk.Label(main, text="Enter words so we can generate a password", font=('Helvetica', 13), ).grid(row=0, column=0,
                                                                                                 columnspan=4)

# store the word that we will get
hold_str = tk.StringVar()

# widget where we will input our words
entry = ttk.Entry(main, textvariable=hold_str, justify='center', width=20)
entry.grid(row=1, column=1)

# List that will hold the words that we will generate from the Password
l = []


# Function to store the words from the entry
def Post():
    global l
    l.append(entry.get())
    entry.delete(0, tk.END)


# Function to generate a password
def Generate():
    # This function can be changed however the User wants it
    passw = ''
    global l
    for x in l:
        if len(passw) < 10:
            if len(x) > len(l):
                passw += str(len(x) * 12) + x[:len(x) // len(l)].title()
            else:
                passw += str(len(l) * 45) + x[len(l):len(x)].upper()
    entry.insert(0, passw)


# Function to clear the words so we can create another Password
def Clear():
    global l
    l = []


B_Post = ttk.Button(main, text='Post Word', command=Post)
B_Post.grid(row=2, column=0)

B_Gen = ttk.Button(main, text='Generate', command=Generate)
B_Gen.grid(row=2, column=2)

B_Clear = ttk.Button(main, text='Clear Words', command=Clear)
B_Clear.grid(row=2, column=1)

main.mainloop()
