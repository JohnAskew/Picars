#!/usr/bin/env python
import xbmc
import json
jsonSWAT_Sel_Vol = '{"jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["volume"]}, "id": 1}'
jsonSWAT_Notify = '{"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Volume Level","message":"%s","image":"info"},"id":1}'
result = json.loads(xbmc.executeJSONRPC(jsonSWAT_Sel_Vol))['result']['volume']
print result
new_vol = int((result / 2))
print new_vol
xbmc.executebuiltin("XBMC.SetVolume(%d)" %( new_vol, ) )
xbmc.executebuiltin("Notification(Completed...Vol. set to:," + str( new_vol, ) + " ,1500,/home/osmc/.kodi/addons/skin.picars/lcars/warn/green.gif)")
