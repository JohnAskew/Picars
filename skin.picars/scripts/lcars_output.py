import xbmc, subprocess

myTranz = "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=processing"
cmd = "wget -q -U Mozilla -O output.wav " + myTranz
xbmc.executebuiltin('Notification('+ cmd +' , '+ myTranz +', 2000,/home/osmc/.kodi/addons/skin.picars/lcars/avi/yellow.gif)')
xbmc.playSFX('/home/osmc/.kodi/addons/skin.picars/lcars/wav/output.wav')
