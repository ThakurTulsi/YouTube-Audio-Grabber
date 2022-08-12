from tkinter import *
from tkinter import font
from pytube import YouTube

window = Tk()
window.geometry("600x700")
window.configure(bg= "red")
window.title("YOUTUBE DOWNLOADER")

window.iconbitmap("youtubeicon.ico")
Label(window, text="Welcome to YouTube video Downloader", font=("Arial 20 bold"), fg="black", bg="white").pack(padx=10, pady=50)
window.resizable(False, False)
#window.place(x=30, y=50)
#window.bind("<<window>>", selectcursor)

youtubelink = StringVar()
Label(window, text="Enter the link here: ", font=("Arial 15 italic bold"), fg="black" , bg="lightyellow").place(x= 200, y=160)

Entry_link = Entry(window, width=40, font=20, textvariable= youtubelink, bd=4).place(x=80, y=240)

def youtube_download():
    youtube_url = YouTube(str(youtubelink.get()))
    youtube_data = youtube_url.streams.first()
    youtube_data.download()

    Label(window, text="Download Complete!!", font="Arial 15 italic bold", bg="lightyellow", fg="black").place(x= 200, y=400)
    Label(window, text="THANK YOU!", font="Arial 15 italic bold", bg="white", fg="black").place(x= 240, y=500)


    #Label(window, text="Check out your YT-Downloader folder", font="Arial 15 bold", bg="lightpink", fg="black").place(x= 200, y=300)

Button(window, text="DOWNLOAD", font="Arial 15 bold", bg="lightpink", command= youtube_download, bd=4).place(x= 230, y= 320)



window.mainloop()