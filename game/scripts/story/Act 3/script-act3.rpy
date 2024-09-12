label act3:
    # TODO: Read player choices and call the correct chapter branch from that
    $ style.say_window = style.window
    $ nb = "namebox"
    "Act 3 is kinda complicated so please read this carefully."
    "There's a reason why this mod requires 2 applications."
    "What the mod is about to do is open the Midnight Club application automatically, so when it does, you're gonna need to set you're options on both of these applications to compensate."
    "In order for this Act to work properly, it needs both applications to run simultaneously as you need to control both Taiyen and Aoruguri at the same time."
    "The UI will be different depending on which character is for which application as a reminder."
    "Most sections will have the 2 characters solo but some will have them be together in the same scene, the mod will wait until both applications are at that scene before continuing."
    "This may seem unneeded, but with this act, not only do your choices matter, but the time you do actions matter too."
    "For example, if you interact with something in one application before interacting with the same thing in the other application, things will be different compared to if you did it the other way around."
    "That's the gist of the situation."
    "Now, as for starting the Act itself..."
    "You will soon see a menu with many branches, these branches unlock based on the choices you have previously made throughout Acts 1 and 2."
    "Simply select the branch you wish to play and hit PLAY to begin."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        "Also, If you are seeing this, that means the mod has detected that you are recording, and you are probably wondering how you are going to record this."
        "Just set up OBS or XSplit to have 2 screens and capture both games."
        "If that doesn't work, then unfortunately... I don't know how to help you."
    "That is all."
    call screen dialog(message="The mod will now open the Midnight Club application, this process could take a while.  When this happens, the command prompt will open up too, close the command prompt and both applications will respond.\nPlease ensure that both this application and the Midnight Club application are both running simultaneously the entire time throughout this Act.", ok_action=[Function(openMidnight), Return()])

    return

# init python:
#     import socket
#     import sys
#     from thread import *
#     def clientreceive():
#         clientreceive1()
#         serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         serversocket.bind(('localhost', 8089))
#         serversocket.listen(2)

#         while True:
#             connection, address = serversocket.accept()
#             buf = connection.recv(64)
#             if len(buf) > 0:
#                 print buf
#                 break
#     def clientsend():
#         clientsend1()
#         clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         clientsocket.connect(('localhost', 8089))
#         clientsocket.send('hello')
#     def clientreceive1():
#         serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         serversocket.bind(('localhost', 8089))
#         serversocket.listen(2)

#         while True:
#             connection, address = serversocket.accept()
#             buf = connection.recv(64)
#             if len(buf) > 0:
#                 print buf
#                 break
#     def clientsend1():
#         clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         clientsocket.connect(('localhost', 8089))
#         clientsocket.send('hello')