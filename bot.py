import socket
import tkinter

HOST = "irc.twitch.tv"
PORT = 6667
NICK = ""             # Twitch Channel
PASS = ""             # Get this from https://twitchapps.com/tmi/
                      # "oauth:(followed by a long string"

BOTNICK = ""          # Name of Bot (Second Twitch Account)            
BOTPASS = ""          # Same format as the other PASS

def bot(fr):

    def send_message(message, s):

        botSock = socket.socket()
        botSock.connect((HOST, PORT))
        botSock.send(bytes("PASS " + BOTPASS + "\r\n", "UTF-8"))
        botSock.send(bytes("NICK " + BOTNICK + "\r\n", "UTF-8"))
        botSock.send(bytes("JOIN #" + NICK + "\r\n", "UTF-8"))

        botSock.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))

    print("Bot is Running")
 
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
    sock.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
    sock.send(bytes("JOIN #" + NICK + "\r\n", "UTF-8"))

    while True:
        line = str(sock.recv(1024))
        if "End of /NAMES list" in line:
            break

    while True:
        for line in str(sock.recv(1024)).split('\\r\\n'):

            parts = line.split(':')
            if len(parts) < 3:
                continue

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                msg = parts[2][:len(parts[2])]

            usernamesplit = parts[1].split("!")
            username = usernamesplit[0]

            print(username + ": " + msg)

            count = 0
            for _ in fr.winfo_children():
                count += 1

            notbutton = 0
            for widget in fr.winfo_children():
                if count > 5:
                    if notbutton > 0:
                        widget.destroy()
                notbutton += 1
            
            if msg == "!test":
                label = tkinter.Label(fr, text=username + ":" + msg, fg="black")
                label.pack()
                send_message("This is a test command", sock)
