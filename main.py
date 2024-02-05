import instaloader
from tkinter import *

window = Tk()
window.title("Instagram Photo Downloader")
window.minsize(width=300, height=300)

first_label = Label(text="Please enter the username:  ", font=('Arial', 30, "normal"))
first_label.pack()

user_name_entry = Entry()
user_name_entry.pack()

def download():
    try:
        username= user_name_entry.get()
        instaloader.Instaloader().download_profile(username,profile_pic_only=False)
        label_sonuc.config(text="Download completed")
    except Exception as e:
        print(e)
        label_sonuc.config(text="Invalid input or download failed!")

download_button= Button(window, text="Download", command=download)
download_button.pack()

label_sonuc = Label(window, text="")
label_sonuc.pack()



window.mainloop()