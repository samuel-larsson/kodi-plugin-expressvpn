import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "This is a simple example of OK dialog"

xbmcgui.Dialog().ok(addonname, line1)
