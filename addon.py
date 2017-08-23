import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "This is a simple example of OK dialog"
swedenBtn = xbmcgui.ControlButton(0, 0, 200, 200, "Sweden")

xbmcgui.Window(self).addControl(swedenBtn)
xbmcgui.Dialog().ok(addonname, line1)
