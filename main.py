from tkinter import *

window = Tk()
window.title("Sign In Screen")
window.geometry("450x300")
window.config(background = "blue")

user_name = Label(window,text = "Username").place(x=40,y=60)
user_password = Label(window, text="Password").place(x=40,y=100)
user_email = Label(window,text="Email").place(x=40,y=140)
user_phone = Label(window, text = "Phone Number").place(x=40,y=180)
user_age = Label(window,text = "Age").place(x=40,y=220)
enter_button = Button(window,text="Enter").place(x=40,y=250)
user_name_input_area = Entry(window, width=30).place(x=110,y=60)
user_password_entry_area = Entry(window, show="*",width = 30).place(x = 110, y=100)
user_email_input_area = Entry(window, width=30).place(x=110,y=140)
user_phone_entry_area = Entry(window, width=30).place(x=150, y=180)
user_age_input_area = Entry(window, width=30).place(x=110,y=220)
leave_button = Button(window, text="Leave App", bd = "5",background="red",command=window.destroy)

leave_button.pack(side="bottom")
window.mainloop()