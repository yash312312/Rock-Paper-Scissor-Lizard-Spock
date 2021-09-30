# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()
root.config(background="white")
# Set geometry
root.geometry("800x480")
root.minsize(800, 480)

# Set title
root.title("Rock Paper Scissor Lizard Spock Game")

# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor",
    "3": "Lizard",
    "4": "Spock"
}

com_score = 0
player_score = 0


# Reset The Game
def reset_game():
    global com_score
    global player_score
    l1.config(text="Player\t")
    l3.config(text="Computer")
    l4.config(text="")
    com_score = 0
    player_score = 0

    lp.config(text="Player Score - " + str(player_score) + "\t")
    lc.config(text="Computer Score - " + str(com_score))


# Update Score
def update_score():
    global com_score
    global player_score

    print("Player ", player_score)
    print("Computer ", com_score)
    print()

    lp.config(text="Player Score - " + str(player_score) + "\t")
    lc.config(text="Computer Score - " + str(com_score))


def inc_score(c):
    global com_score
    global player_score
    if c:
        com_score = com_score + 1
    else:
        player_score = player_score + 1


# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0, 4))]
    col = "black"
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Paper":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Lizard":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"

    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Rock\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# If player selected paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 4))]
    col = "black"
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v == "Scissor":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Rock":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Lizard":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    else:
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Paper\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# If player selected scissor
def isscissor():
    c_v = computer_value[str(random.randint(0, 4))]
    col = "black"
    if c_v == "Scissor":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Rock":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Lizard":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Scissor\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


def islizard():
    c_v = computer_value[str(random.randint(0, 4))]
    col = "black"
    if c_v == "Lizard":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Rock":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Scissor":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    else:
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Lizard\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


def isspock():
    c_v = computer_value[str(random.randint(0, 4))]
    col = "black"
    if c_v == "Spock":
        match_result = "Match Draw"
    elif c_v == "Paper":
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    elif c_v == "Rock":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    elif c_v == "Scissor":
        match_result = "Player Wins"
        inc_score(False)
        col = "green"
    else:
        match_result = "Computer Wins"
        inc_score(True)
        col = "red"
    l4.config(text=match_result, fg=col)
    l1.config(text="Player chose - Spock\t")
    l3.config(text="Computer chose - " + c_v)
    update_score()


# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor Lizard Spock",
      font="normal 20 bold",
      fg="blue", bg="white").pack(pady=20)

frame = Frame(root, bg="white")
frame.pack()

l1 = Label(frame,
           text="Player\t", fg="green",
           font="normal 20 bold", bg="white")

l2 = Label(frame,
           text="VS\t",
           font="normal 10 bold", bg="white")

l3 = Label(frame, text="Computer", fg="red", font="normal 20 bold", bg="white")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="white",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)

frame1 = Frame(root, bg="white")
frame1.pack()

ro = PhotoImage(file="images/rock.png")
ro = ro.subsample(3, 3)

pa = PhotoImage(file="images/paper.png")
pa = pa.subsample(3, 3)

sc = PhotoImage(file="images/scissor.png")
sc = sc.subsample(3, 3)

li = PhotoImage(file="images/lizard.png")
li = li.subsample(3, 3)

sp = PhotoImage(file="images/spock.png")
sp = sp.subsample(3, 3)

b1 = Button(frame1, text="Rock", image=ro,
            font=10,
            command=isrock, compound=TOP, bg="white")

b2 = Button(frame1, text="Paper ", image=pa,
            font=10,
            command=ispaper, compound=TOP, bg="white")

b3 = Button(frame1, text="Scissor", image=sc,
            font=10,
            command=isscissor, compound=TOP, bg="white")

b4 = Button(frame1, text="Lizard", image=li,
            font=10,
            command=islizard, compound=TOP, bg="white")

b5 = Button(frame1, text="Spock", image=sp,
            font=10,
            command=isspock, compound=TOP, bg="white")

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
b5.pack(padx=10)

Button(root, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)

frame2 = Frame(root)
frame2.pack()
lp = Label(frame2,
           text="Player Score - " + str(player_score) + "\t",
           font="normal 15 bold", fg="green", bg="white")

lc = Label(frame2,
           text="Computer Score - " + str(com_score),
           font="normal 15 bold", fg="red", bg="white")
lp.pack(side=LEFT)
lc.pack(side=LEFT)
# Execute Tkinter
root.mainloop()
