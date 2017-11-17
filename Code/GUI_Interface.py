from tkinter import *
import os
import webbrowser

commands_file = "Commands.txt";

# Open Forum Function
def openForum():
    webbrowser.open('https://github.com/Codiscite/Conver');
    
# Add Command Function
def addCommand():
    value1 = comIN.get();
    value2 = comOUT.get();
    
    file = open(commands_file, 'a');
    file.write(value1 + "=" + value2 + "\n");
    file.close();

# Speech To Text Function
def runSTT():
    os.system("py SpeechToTextTest.py");

def quitApp():
    window.destroy();
    exit()

# Open Main Window and Name it
window = Tk();
window.title("Conver CRI Interface");
window.geometry("500x400");

# Define Voice Button
voiceBTN_Photo = PhotoImage(file="dictationBTN.png");
voiceBTN = Button(window, width=300, image=voiceBTN_Photo, command=runSTT);

inL = Label(text="Custom Command:");
comIN = Entry(window);
outL = Label(text="->");
comOUT = Entry(window);

addCommandBTN = Button(window, width=15, text="Add Command", command=addCommand)

# Define Quit Button
forumBTN = Button(window, width=20, text="View Docs", command=openForum);
quitBTN = Button(window, width=10, text="Exit", command=quitApp);

# Setup Widgets
voiceBTN.pack();
quitBTN.pack(side=BOTTOM);
forumBTN.pack(side=BOTTOM);

inL.pack(side=LEFT);
comIN.pack(side=LEFT);
outL.pack(side=LEFT);
comOUT.pack(side=LEFT);
addCommandBTN.pack(side=RIGHT);

# Start Running
window.mainloop();
