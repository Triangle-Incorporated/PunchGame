# Handle input and output

# |  Comment this out when working on Replit
# V
#import explorerhat

import gamelogic

def sendsignal(sig) :
	""" Send input signal to game loop to handle """
	if gamelogic.trackEvents :
		gamelogic.iovents.append(sig)

def ledOutput(alertType) :
	""" Turn on different leds depending on alert type """

	
#
# Write handlers here
#

def checkInputs() :
	""" Check joystick and buttons for input """
	j_x = explorerhat.analog.two.read()
	j_y = explorerhat.analog.one.read()

	btn = explorerhat.input.one.read()

	# Walking
	if j_x < 2.4 :
		if j_x > 1.7 :
			sendsignal("sleft")
		else :
			sendsignal("lleft")
	if j_x > 2.6 :
		if j_x < 3.3 :
			sendsignal("sright")
		else :
			sendsignal("lright")

	# Actions
	if btn == 1 and j_y > 3.5:
		sendsignal("downb")
	if btn == 1 and j_y < 3.5 and j_y > 1.5 and j_x < 3.5 and j_x > 1.5:
		sendsignal("ntrlb"')
	if btn == 1 and j_y < 1.5:
		sendsignal("upb")
#	if btn == 1 and j_x > 3.5:
#		sendsignal("leftb")
#	if btn == 1 and j_x < 1.5:
#		sendsignal("rightb")

# 
# End handler code here
#
