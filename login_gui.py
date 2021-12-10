from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import *





window = tk.Tk()

window.geometry('862x519+200+100')
window.title('Log In to BD School')
# window.attributes('-toolwindow', True)
window['background'] = '#3A7FF6'

canvas = tk.Canvas(
    window, bg="#3A7FF6", height=519, width=862,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")



text_box_bg = tk.PhotoImage(file="TextBox_Bg.png")
token_entry_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
URL_entry_img = canvas.create_image(650.5, 248.5, image=text_box_bg)


password_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
password_entry.place(x=490.0, y=137+25, width=321.0, height=35)
password_entry.focus()
email_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
email_entry.place(x=490.0, y=218+25, width=321.0, height=35)






canvas.create_text(
    490.0, 156.0, text="Email", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")
canvas.create_text(
    490.0, 234.5, text="Password", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

# canvas.create_text(
#     646.5, 428.5, text="Generate",
#     fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))


title = tk.Label(
    text="Welcome", bg="#3A7FF6",
    fg="white", font=("Arial-BoldMT", int(30.0)))
title.place(x=27.0, y=120.0)

info_text = tk.Label(
    text="To our BD School System.",
    bg="#3A7FF6", fg="white", justify="left",
    font=("Georgia", int(16.0)))

info_text.place(x=27.0, y=200.0)

















def btn_clicked():
    password = password_entry.get()
    email = email_entry.get()
    

    if not password:
       messagebox.showerror(
            title="Empty Fields!", message="Please enter password.")
       return

    if not email:
        messagebox.showerror(
            title="Empty Fields!", message="Please enter Email.")
        return


generate_btn_img = tk.PhotoImage(file= "button.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=0, highlightthickness=0,
    relief="flat",
    command=btn_clicked)
generate_btn.place(x=557, y=301, width=180, height=55)



window.mainloop()