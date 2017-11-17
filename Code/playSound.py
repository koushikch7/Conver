import pyglet, sys, time, os;
from mutagen.mp3 import MP3;

sound = pyglet.resource.media(sys.argv[1])
sound.play()

audio = MP3(sys.argv[1]);
time.sleep(audio.info.length + 0.1);
os.system("py SpeechToTextTest.py");

pyglet.app.run()
