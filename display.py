import guizero as gui
app = gui.App("this is an app")
import gamelogic

#
# Put GUI code here
#

playButton = gui.PushButton(app, text = "Play", command = gamelogic.gameLoop)

#
# End GUI code here #
#

def initGui() :
	""" Start displaying the gui """
	app.display()