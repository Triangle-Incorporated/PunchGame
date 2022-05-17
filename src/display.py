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

b_title = gui.Box(app, layout = "grid")
t_title = gui.Text(b_title, text = "Welcome to Punch Game!", grid = [0, 0])
button_title = gui.PushButton(b_title, text = "Quit", command = app.destroy, grid = [1, 0])

playButton = gui.PushButton(app, text = "Play", command = gamelogic.gameLoop)

#
# End GUI code here #
#

