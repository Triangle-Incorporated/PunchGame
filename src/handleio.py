# Handle input and output

# |  Comment this out when working on Replit
# V
dimport explorerhat

import gamelogic

def sendsignal(sig) :
	""" Send input signal to game loop to handle """
	if gamelogic.trackEvents :
		gamelogic.iovents.append(sig)

def ledOutput(health) :
	""" Turn on different leds depending on alert type """
	if health <= 50 and health > 20:
		explorerhat.output.one.blink(1, 1)
	elif heatlh <= 20 and health > 10:
		explorerhat.output.one.blink(0.5, 0.5)
	elif health <= 10:
		explorerhat.output.one.blink(0.25, 0.25)
	else:
		explorerhat.output.one.on()
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
	elif j_x > 2.6 :
		if j_x < 3.3 :
			sendsignal("sright")
		else :
			sendsignal("lright")
	else :
		sendsignal("nop")

	# Actions
	if btn == 1 and j_y > 3.5 :
		sendsignal("downb")
	elif btn == 1 and j_y <= 3.5 and j_y >= 1.5 :
		sendsignal("ntrlb")
	elif btn == 1 and j_y < 1.5 :
		sendsignal("upb")
"""
	if btn == 1 and j_x > 3.5:
		sendsignal("leftb")
	if btn == 1 and j_x < 1.5:
		sendsignal("rightb")
"""

# 
# End handler code here
#
