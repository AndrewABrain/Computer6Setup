import os
import time
import random
from threading import Thread
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def maxVolume():
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))	
	while True:
		current = volume.GetMasterVolumeLevelScalar()
		if not (current == 1.0):
			volume.SetMasterVolumeLevelScalar(1.0, None)

def waitAndLogOut():
	time.sleep(213)
	os.system("shutdown /f -l")

if __name__ == "__main__":
	Thread(target = maxVolume).start()
	Thread(target = waitAndLogOut).start()
