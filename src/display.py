# Handle GUI

import guizero as gui
app = gui.App("this is an app", bg = "blue")

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

# Title
b_title = gui.Box(app, layout = "grid")
t_title = gui.Text(b_title, text = "Welcome to Punch Game!", grid = [0, 0])
btn_title = gui.PushButton(b_title, text = "Quit", command = app.destroy, grid = [0, 1])
btn_title.bg = ("white")


# Play
playButton = gui.PushButton(app, text = "Play", command = gamelogic.gameLoop)
playButton.bg = ("#90EE90")

def login() :
    

#
# End GUI code here #
#

