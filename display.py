import guizero as gui
app = gui.App("this is an app")
import gamelogic

playButton = gui.PushButton(app, text = "Play", command = gamelogic.gameLoop)
print("Gui works")

def initGui() :
	""" Start displaying the gui """
	app.display()