import  xbmc, subprocess
from __main__ import *

myTranz = "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q=processing"
cmd = "wget -q -U Mozilla -O output.mp3 " + myTranz
xbmc.playSFX('/home/osmc/.kodi/addons/skin.picars/lcars/wav/output.mp3')
