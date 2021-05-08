from tkinter import *
from tkinter.messagebox import *
import pytube


# Download Function
def download():
    button['text'] = "Download Started..."
    root.update_idletasks()
    root.update()
    try:
        video_url = entry.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download("Youtube Downloads/")
        askokcancel("Download Manager", "Download Completed Successfully!")
        Label(root, text="Download Completed Successfully!",
              fg="green", font="calibri12").pack(pady=5)
        button['text'] = "Download"
        root.update()

    except:
        button['text'] = "Download"
        askokcancel("Download Manager", "Download Failed, Try Again!")
        root.update()


# Initialization and customization.
root = Tk()
root.geometry("475x190")
root.minsize(475, 190)
root.maxsize(475, 190)
#root.iconbitmap("/media/vedant/Mass Data Storag/Youtube Downloader/icon.ico")
root.title("Youtube Video Downloader")

# Lables and texts.
title = Label(root, text="Youtube Video Downloader",
              fg="red", font="Calibri 15")
title.pack(anchor="center", padx=15)
label = Label(root, text="Enter video link here :", font="Calibri 12")
label.pack(pady=2, anchor="center")

# Variables for entry.
url = StringVar()

# Entry and Button for video link.
entry = Entry(root, width=40, textvariable="url", font="Calibri 12")
entry.pack(padx=30, anchor="center")
button = Button(root, text="Download", width=20,
                font="calibri 12", command=download)
button.pack(pady=10)
root.mainloop()
