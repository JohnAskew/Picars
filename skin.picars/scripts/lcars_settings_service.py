import xbmc
if  not xbmc.Player().isPlaying() :
    xbmc.executebuiltin("PlayMedia(/home/osmc/.kodi/addons/skin.picars/lcars/wav/settings/services.mp3)")
