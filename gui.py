import guizero as gui
import gamelogic

app = gui.App("this is an app")

playButton = gui.PushButton("Play", command = gamelogic.gameLoop)
print("Gui works")

def initGui() :
	""" Start displaying the gui """
	app.display()