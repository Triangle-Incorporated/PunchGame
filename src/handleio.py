# Handle input and output

# |  Comment this out when working on Replit
# V
import explorerhat

import gamelogic

print("I/O handlers loaded")

def sendsignal(sig) :
    """ Send input signal to game loop to handle """
    if gamelogic.trackEvents :
        gamelogic.ioevents.append(sig)

def ledOutput(health) :
    """ Turn on different leds depending on alert type """
    if health <= 70 and health > 40:
        explorerhat.output.one.blink(1, 1)
    elif health <= 40 and health > 20:
        explorerhat.output.one.blink(0.5, 0.5)
    elif health <= 20 and health > 0:
        explorerhat.output.one.blink(0.25, 0.25)
    elif health <= 0:
        explorerhat.output.one.off()
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
            sendsignal("sright")
        else :
            sendsignal("lright")
    elif j_x > 2.6 :
        if j_x < 3.3 :
            sendsignal("sleft")
        else :
            sendsignal("lleft")
    else :
        sendsignal("nop")

    # Actions
    if btn == 1 and j_y > 3.5 :
        sendsignal("downb")
    elif btn == 1 and j_y <= 3.5 and j_y >= 1.5 :
        sendsignal("ntrlb")
    elif btn == 1 and j_y < 1.5 :
        sendsignal("upb")



# 
# End handler code here """
#
