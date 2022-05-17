# Handle input and output

# |  Comment this out when working on Replit
# V
#import explorerhat

import gamelogic

def sendsignal(sig) :
	""" Send input signal to game loop to handle """
	if gamelogic.trackEvents :
		gamelogic.iovents.append(sig)

#
# Write handlers here
#

def checkInputs() :
	""" Check joystick and buttons for input """


# 
# End handler code here
#
