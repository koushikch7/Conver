import os;

packages = ["wikipedia", "requests", "re", "pushbullet.py", "beautifulsoup4", "gTTS", "SpeechRecognition"]

print("Setting Up Conver...");

def installPackage(package):
	os.system("py -m pip install " + package);

for package in packages:
	installPackage(package);
