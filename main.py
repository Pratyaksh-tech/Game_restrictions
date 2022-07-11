import subprocess
import time
import threading
import ui



with open("D:/gamerest/day_mang.txt", "r") as a:
	if a.read() == "":
		print("started today")
		t_stored_time = str(time.localtime()[4]);
		with open("D:/gamerest/day_mang.txt", "w") as f:
			f.write(t_stored_time);
			f.close();


def handle_day():
	while True:
		with open("D:/gamerest/day_mang.txt", "r") as f:
			c = str(f.read());
			f.close();
		print(c + "stored day")	
		if c != str(time.localtime()[4]):
			with open("D:/gamerest/day_mang.txt", "w") as f:
				f.write(str(time.localtime()[4]));
				f.close();
			with open("D:/gamerest/time_mang.txt", "w") as f:
				f.write("0");
				f.close();
			with open("D:/gamerest/gui_mang.txt", "w") as k:
				k.write("0");
				k.close();	

		time.sleep(0.5);
				
def restrict():
	cmd = "tasklist"
	app = "vlc.exe"

	while True:
		with open("D:/gamerest/time_mang.txt", "r") as f:
			t = f.read();
			
			t = int(t);
			f.close();
		a = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
		data = a.stdout.decode().split();
		t+=1;
		if app in data:
			print("ui is on its way")
			with open("D:/gamerest/gui_mang.txt", "r") as s:
				if s.read() == "0":
					ui.mainui();
					with open("D:/gamerest/gui_mang.txt", "w") as k:
						k.write("1");
						k.close();

			print(t)
			with open("D:/gamerest/time_mang.txt", "w") as f:
				newt = str(t);
				f.write(newt);
				f.close();
			if t >=20:
				print("we got it");
				cmd2 = f"taskkill /f /im {app}"
				a2 = subprocess.run(cmd2, shell=True);
				with open("D:/gamerest/gui_mang.txt", "w") as k:
					k.write("1");
					k.close();

			
		else:
			with open("D:/gamerest/gui_mang.txt", "w") as k:
				k.write("0");
				k.close();
			print("no there is no vlc");
			print(t);



		time.sleep(1);
		
thread1 = threading.Thread(target=handle_day);
thread1.start();

thread2 = threading.Thread(target=restrict);
thread2.start();
