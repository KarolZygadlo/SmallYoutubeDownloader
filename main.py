import tkinter
import customtkinter
from pytube import YouTube 

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Videos Downloader")

url_var = tkinter.StringVar()
title = customtkinter.CTkLabel(app, text="Insert a youtube link", textvariable=url_var)
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack()





app.mainloop()
