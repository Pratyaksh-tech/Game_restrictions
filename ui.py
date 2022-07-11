from tkinter import *
import time
import threading
import subprocess

def mainui():
	root = Tk();
	root.title("Messege");
	root.geometry("400x300");

	def quit():
		root.destroy();

	lbl1 = Label(root, text="00", font=("Arial", 31));
	lbl1.pack(pady=10)

	lbl2 = Label(root, text="Enter Password to play game.", font=("Arial", 16));
	lbl2.pack(pady=10)

	ent_box = Entry(root, width=30);
	ent_box.pack(pady=10);

	global lbl_wrong;
	lbl_wrong = Label(root, font=("Arial", 16));
	lbl_wrong.pack(pady=10);

	def checkpass():
		password = ent_box.get();
		if password == "bhanu":
			root.destroy();
		else:
			lbl_wrong.config(text="sala suar sahi password daal");
				
	butt1 = Button(root, text="Confirm", font=("Arial", 14), command=checkpass);
	butt1.pack()

	def timer():
		timer_sec = time.localtime()[5] - time_loc;
		lbl1.config(text=timer_sec);
		if timer_sec >= 10:
			app = "vlc.exe"
			cmd2 = f"taskkill /f /im {app}"
			a2 = subprocess.run(cmd2, shell=True);
			root.destroy();
			with open("D:/gamerest/gui_mang.txt", "w") as k:
				k.write("0");
				k.close();
		lbl1.after(1000, timer);	

	global time_loc;
	time_loc = time.localtime()[5];
	timer();

	root.mainloop();

