import xbmc,  os, subprocess, time

time.sleep(1)
locstr =  xbmc.getInfoLabel('System.CurrentWindow')
myURL = "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=" + locstr
myDir="/home/osmc/.kodi/addons/skin.picars/lcars/wav/output.mp3"
cmd = "wget -q -U Mozilla -O " + myDir + " " + myURL
subprocess.call(['wget', '-q', '-U Mozilla', '-O', myDir, myURL])
xbmc.executebuiltin("PlayMedia(/home/osmc/.kodi/addons/skin.picars/lcars/wav/output.mp3)")
