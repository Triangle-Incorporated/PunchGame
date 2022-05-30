# PunchGame
PunchGame is a 2d fighting game made in Python. There's two version for different input types:

1. Keyboard and mouse
2. Our custom made controller

**Installation**

This game depends on Explorerhat for the Raspberry Pi. You can get explorerhat using this command and following the on screen instructions: 

`curl https://get.pimoroni.com/explorerhat | bash`

It also depends on a newer version of Pygame. You can get Pygame using:

`pip3 install pygame==2.0.2.dev4`

Finally, this game uses GUIzero. The source code of GUIzero is included, so you don't have to worry about installing it yourself. GUIzero depends on Tkinter however, so you will need to install tkinter using:

`sudo apt-get python3-tk`
