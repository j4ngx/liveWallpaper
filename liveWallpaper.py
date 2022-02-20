from datetime import datetime
import os

# Get the actual date
now = datetime.now()
# Format the date with only the hours
hour = now.strftime("%H")

hours = ["00","03","07","08","09","10","11","12","13","14","16","17","18","19","20","22"]

# This function change the wallpaper in function of param that pass as argument
def changeWallpaper(hour):
    command = "qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript "+"'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "+'"org.kde.image";d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");d.writeConfig("Image", "file:///home/j/Projects/liveWallpaper/mojave/'+hour+'.jpg")}'+"'"
    os.system(command)

for hoursAux in range(16):
# If hour is the same in the array use that variable as argument
    if hour == hours[hoursAux]:
        changeWallpaper(hours[hoursAux])
# If the hour arent in the array compare the after position and the actual position 
# and if the hour is between us, change the wallpaper with the value of anterior position in the array and exit 
    elif int(hours[hoursAux]) > int(hour) and int(hours[hoursAux-1]) < int(hour):
        changeWallpaper(hours[hoursAux-1])
        break

