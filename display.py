# Handle GUI

import guizero as gui
app = gui.App("this is an app")

def initGui() :
	""" Start displaying the gui """
	app.show()
	app.display()

def destGui() :
	"""Stop showing gui """
	app.hide()

import gamelogic

#
# Put GUI code here
#



playButton = gui.PushButton(app, text = "Play", command = gamelogic.gameLoop)

#
# End GUI code here #
#

