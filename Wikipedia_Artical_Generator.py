from selenium import webdriver
import tkinter as tk

# create main widget
main = tk.Tk()
main.title("Wikipedia Article Randomizer")
main.geometry("320x100")
main.config(bg="#E0C799")

# Set up Driver
PATH = "/usr/local/bin/geckodriver"
driver = webdriver.Firefox(executable_path=PATH)


def B_Yes():
    main.quit()

def B_Another():
    driver.get("https://en.wikipedia.org/wiki/Special:Random")

tk.Label(main, text="Does this Article interrest you ?"
         , font=("Helvetica", 15), bg="#E0C799", fg='#B37400', padx=20, pady=20).grid(row=0, column=0, columnspan=3)

driver.get("https://en.wikipedia.org/wiki/Special:Random")

B_yes = tk.Button(main, bg='#86775B', fg='#FFFFFF', font=('Helvetica',12), text="Yes", command=B_Yes).grid(row=1, column=0)

B_another = tk.Button(main,bg='#86775B', fg='#FFFFFF', font=('Helvetica',12), text="Another One", command=B_Another).grid(row=1, column=1)

main.mainloop()
