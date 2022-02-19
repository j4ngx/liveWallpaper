from datetime import datetime
import os

now = datetime.now()

hour = now.strftime("%H")

print(hour)


hours = ["00","03","07","08","09","10","11","12","13","14","16","17","18","19","20","22"]

for hoursAux in hours:
    if hour == hoursAux:
        #command = 'qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file:///home/j/Projects/liveWallpaper/mojave/'+hour+'.jpg")}"'
        command = "qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "+"'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "+'"org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file:///home/j/Projects/liveWallpaper/mojave/'+hour+'.jpg")}'+"'"
        os.system(command)
        print(command)
