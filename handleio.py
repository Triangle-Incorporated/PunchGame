import explorerhat

# Handle input and output

import gamelogic

def sendsignal(sig) :
	""" Send input signal to game loop to handle """
	if gamelogic.trackEvents :
		gamelogic.iovents.append(sig)

#
# Write handlers here
#



# 
# End handler code here
#
