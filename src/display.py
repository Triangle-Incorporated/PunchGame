# Handle GUI

import guizero as gui
import csv
app = gui.App("this is an app", bg = "blue")

def initGui() :
    """ Start displaying the gui """
    app.show()
    w_signup.hide()
    app.display()

def destGui() :
    """Stop showing gui """
    app.hide()
    w_signup.hide()

import gamelogic

#
# Put GUI code here
#

def sign_window_init() :
    """ Open signup window """
    app.hide()
    w_signup.show()

def sign_window_dest() :
    """ Close signup window """
    w_signup.hide()
    app.show()

def login() :
    """ Check if login is valid """
    name = i_name.value
    passw = i_pass.value
    with open("db/cred.csv", "r") as f :
        db = csv.reader(f)
        for row in db :
            if [name, passw] == row :
                destGui()
                gamelogic.gameLoop()

    app.warn("Incorrect Username or Password", "Your username or password was incorrect.")

def signup() :
    """ Check if signup is valid """

    name = si_name.value
    passw = si_pass.value
    cn_passw = si_conf.value

    print(name, passw, cn_passw)
    
    # Check for issues with submission
    if passw != cn_passw :
        app.warn("Your passwords don't match.", "Your password and confirmation don't match")
        return

    if name == "" or passw == "" or cn_passw == "" :
        app.warn("Blank username or password", "Your username or password was blank, fill in all fields.")
        return

    if len(passw) < 6 :
        app.warn("Password too short", "Your password was too short, it must be atleast 6 characters long")
        return

    # Check if username already exists
    with open("db/cred.csv", "r") as f :
        db = csv.reader(f)
        for row in db :
            if name == row[0] :
                app.warn("Username taken.", "This username has already been taken, please choose another.")
                return

    # Add username
    with open("db/cred.csv", "a") as f :
        db = csv.writer(f)
        db.writerow([name, passw])

    # Start game
    app.info("Account Creation Successful", "Your account was created succesfully! Enjoy playing PunchGame!")
    destGui()
    gamelogic.gameLoop()

#/////////// Main Window /////////////////////

# Title
b_title = gui.Box(app, layout = "grid")
t_title = gui.Text(b_title, text = "Welcome to Punch Game!", grid = [0, 0])
btn_title = gui.PushButton(b_title, text = "Quit", command = app.destroy, grid = [0, 1])
btn_title.bg = ("white")
btn_signup = gui.PushButton(b_title, text = "Sign Up", command = sign_window_init, grid = [1, 1])
btn_signup.bg = "white"

# Login 
b_login = gui.Box(app, layout = "grid")
t_name = gui.Text(b_login, text = "Username: ", grid = [0, 0])
i_name = gui.TextBox(b_login, grid = [1, 0])
t_pass = gui.Text(b_login, text = "Password: ", grid = [0, 1])
i_pass = gui.TextBox(b_login, grid = [1, 1])

# Play button
play_button = gui.PushButton(app, text = "Play", command = login)
play_button.bg = ("#90EE90")

#/////////// Main Window /////////////////////

#// la la la la :)

#/////////// Signup Window /////////////////////
w_signup = gui.Window(app, "Signup")

# Title
st_box = gui.Box(w_signup, layout = "grid")
st_title = gui.Text(st_box, text = "Signup", grid = [0, 0])
st_quit = gui.PushButton(st_box, text = "Menu", grid = [1, 0], command = sign_window_dest)

# Signup
sb_signup = gui.Box(w_signup, layout = "grid")
st_name = gui.Text(sb_signup, text = "Username: ", grid = [0, 0])
si_name = gui.TextBox(sb_signup, grid = [1, 0])
st_pass = gui.Text(sb_signup, text = "Password: ", grid = [0, 1])
si_pass = gui.TextBox(sb_signup, grid = [1, 1])
st_conf = gui.Text(sb_signup, grid = [0, 2], text = "Confirm: ")
si_conf = gui.TextBox(sb_signup, grid = [1, 2])

sbtn_play = gui.PushButton(sb_signup, grid = [0, 3], text = "Signup", command = signup)

#/////////// Signup Window /////////////////////
    
#
# End GUI code here #
#

