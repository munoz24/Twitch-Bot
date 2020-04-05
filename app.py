import tkinter as tk
from tkinter import *
from tkinter import messagebox
import bot
import threading


def main():
    def startbot(button, f):
        messagebox.showinfo(title="Information", message="Close main window to terminate bot")
        botThread = threading.Thread(target=bot.bot, args=(f,))
        botThread.daemon = True
        botThread.start()
        button.config(text="Bot is Running")
        button.config(state=DISABLED)

    root = tk.Tk()
    root.title("Twitch Bot")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=200, width=300, bg="#263D42")
    canvas.pack(fill=BOTH, expand=YES)

    frame = tk.Frame(root, bg="grey")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    runBot = tk.Button(frame, text="Run Bot", padx=40, pady=20, fg="white", bg="black",
                       command=lambda: startbot(button=runBot, f=frame))
    runBot.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
