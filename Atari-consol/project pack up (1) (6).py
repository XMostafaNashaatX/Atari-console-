import random
import guess_the_flag
from glob import glob
from tkinter import*
from tkinter .ttk import Combobox
from tkinter import messagebox


import tkinter as tk

# Main menu
x1 = Tk()
x1.title('Game Master')
x1.geometry('500x500')
x1.config(bg='#264653')
x1.resizable(FALSE, FALSE)
y1 = Label(x1, text='Select your game', font=('Times 32') ,fg='#E76F51', bg='#264653')
y1.pack(pady=50)
selection1 = Combobox(x1, values=['x o game', 'guess the country', 'random number game','guess the flag'], state='readonly', width=50, justify='center')
selection1.option_add('*TCombobox*Listbox.Justify', 'center')
selection1.pack()

players = ["x", "o"]
player = random.choice(players)



def xogame():
    def next_turn(row, col):
        global player
        if game_btns[row][col]['text'] == "" and check_winner () == False:
            if player == players[0]:
                # Put player 1 sympol
                game_btns[row][col]['text'] = player

                if check_winner () == False:
                    # switch player
                    player = players[1]
                    label.config (text=(players[1] + " turn"))

                elif check_winner () == True:
                    label.config (text=(players[0] + " wins!"))

                elif check_winner () == 'tie':
                    label.config (text=("Tie, No Winner!"))

            elif player == players[1]:
                # Put player 2 sympol
                game_btns[row][col]['text'] = player

                if check_winner () == False:
                    # switch player
                    player = players[0]
                    label.config (text=(players[0] + " turn"))

                elif check_winner () == True:
                    label.config (text=(players[1] + " wins!"))

                elif check_winner () == 'tie':
                    label.config (text=("Tie, No Winner!"))

    def check_winner():
        # check all 3 horizontal conditions
        for row in range (3):
            if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
                game_btns[row][0].config (bg="cyan")
                game_btns[row][1].config (bg="cyan")
                game_btns[row][2].config (bg="cyan")
                return True

        # check all 3 vertical conditions
        for col in range (3):
            if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
                game_btns[0][col].config (bg="cyan")
                game_btns[1][col].config (bg="cyan")
                game_btns[2][col].config (bg="cyan")
                return True

        # check diagonals conditions
        if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
            game_btns[0][0].config (bg="cyan")
            game_btns[1][1].config (bg="cyan")
            game_btns[2][2].config (bg="cyan")
            return True
        elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
            game_btns[0][2].config (bg="cyan")
            game_btns[1][1].config (bg="cyan")
            game_btns[2][0].config (bg="cyan")
            return True

        # if there are no empty spaces left
        if check_empty_spaces () == False:
            for row in range (3):
                for col in range (3):
                    game_btns[row][col].config (bg='red')

            return 'tie'

        else:
            return False

    def check_empty_spaces():
        spaces = 9

        for row in range (3):
            for col in range (3):
                if game_btns[row][col]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def start_new_game():
        global player
        player = random.choice(players)

        label.config (text=(player + " turn"))

        for row in range (3):
            for col in range (3):
                game_btns[row][col].config (text="", bg="#F0F0F0")

    window = Tk()
    window.title("Tic-Tac-Toe Korsat-X-Parmaga")

    players = ["x", "o"]
    player = random.choice(players)

    game_btns = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    label = Label (window,text=(player + " turn"), font=('consolas', 40))
    label.pack (side="top")

    restart_btn = Button (window,text="restart", font=(
        'consolas', 20), command=start_new_game)
    restart_btn.pack (side="top")

    btns_frame = Frame(window)
    btns_frame.pack()

    for row in range(3):
        for col in range(3):
            game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                          command=lambda row=row, col=col: next_turn (row, col))
            game_btns[row][col].grid(row=row, column=col)

    window.mainloop ()
    return


def guess_the_country():
    from random import choice

    from random import choice
    from random import shuffle
    root = Tk()
    root.title('arrange the words')
    root.geometry('400x400')

    my_label = Label(root, text='', font=('Helvetica', 40))
    my_label.pack(pady=20)

    def suffler():
        my_answerbox.delete(0, END)


        Egypt_states = ['Mansora', 'Cairo', 'Alexandria', 'Aswan', 'Asyut', 'Beheira', 'Beni Suef', 'Dakahlia',
                        'Domiatt', 'Faiyum', 'Gharbia', 'Giza', 'Ismailia', 'Kafr El Sheikh', 'Luxor', 'Matruh',
                        'Minya', 'Monufia', 'New Valley', 'North Sinai', 'Port Said', 'Qalyubia', 'Qena', 'Red Sea',
                        'Sharqia', 'Sohag', 'South Sinai', 'Suez']

        global word
        word = choice(Egypt_states)
        break_word_into_letters = list(word)
        shuffle(break_word_into_letters)

        global suffled_word
        suffled_word = ''
        for letter in break_word_into_letters:
            suffled_word += letter

        my_label.config(text=suffled_word)
        return True


    def answer():
        if word == my_answerbox.get():
            below_answerbox.config(text='Correct Answer!!',fg="green")

        else:
            below_answerbox.config(text='Incorrect Answer!!',fg="red")

    my_answerbox = Entry(root, font=('Helvetica', 30), justify = 'center')
    my_answerbox.pack(pady=20)

    answer_button = Button(root, text='answer', command=answer)
    answer_button.pack(pady=20)

    below_answerbox = Label(root, text='', font=('Helvetica', 20))
    below_answerbox.pack(pady=20)

    button_frame = Frame(root)
    button_frame.pack(pady=20)
    my_button = Button(button_frame, text='pick another word', command=suffler)
    my_button.grid(row=0, column=0, padx=10)

    suffler()
    root.mainloop()
    return


def randomNumberGame():
    from random import randint
    x4=Tk()
    x4.title('random number game')
    x4.geometry('500x500')
    num_label = Label(x4,text = 'pick a number\n between 1 and 10', font= 32)
    num_label.pack(pady=20)

    def guesser():
        if guess_box.get().isdigit():
            if int(guess_box.get()) <= 10:
                num_label.config(text='pick a number\n between 1 and 10')
                dif = abs( num - int(guess_box.get()))

                if int(guess_box.get()) == num:
                    num_label.config(text='correct!')
                    bc = 'Green'
                elif  dif == 5:
                   bc = 'white'
                elif dif < 5:
                    bc = f'#ff{dif}{dif}{dif}{dif}'
                else:
                    bc = f'#{dif}{dif}{dif}{dif}ff'

                x4.config(bg=bc)
                num_label.config(bg=bc)
            else:
                messagebox.showwarning(title='warning', message='The number should be less than or equal 10')
        else:
            guess_box.delete(0,END)
            num_label.config(text='sorry!\n that is not a number!')


    def rando():
        global num
        num = randint(1,10)
        guess_box.delete(0,END)

    guess_box = Entry(x4,font= ('Helvetica',100) , width=2,justify='center')
    guess_box.pack(pady=50,padx=50)

    guess_button = Button(x4 , text='submit', command=guesser)
    guess_button.pack(pady=20)

    rand_button = Button(x4, text='new number' , command= rando)
    rand_button.pack(pady=20)



    rando()
    x4.mainloop()
    return


def flaggame():
    guess_the_flag.check_guess()
    guess_the_flag.reset_game()






def open_window():
    option = selection1.get()
    if option == 'x o game':
        xogame()
    elif option == 'guess the country':
        guess_the_country()
    elif option == 'guess the flag':
        flaggame()
    else:
        randomNumberGame()


button1 = Button(x1, text='open the game', command=open_window,bg='#E76F51', width=15, height=2, bd=0, fg='#264653')
button1.pack(pady=20)

button2 = Button(x1, text='EXIT', command=x1.destroy,bg='#E76F51', fg='#264653', bd=0)
button2.pack(pady=10)

x1.mainloop()