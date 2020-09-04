import random
import time


class Random_Game():

    def __init__(self):
        print("Willkommen bei ---The DEVIL get your SOUL Random Game!---")
        time.sleep(4)
        print("\n Du kannst 1.000.000 EUR gewinnen! Schaffst du es aber nicht, ist deine Seele verkauft!wohahaha")
        time.sleep(4)
        print("\n Du musst die richtige Zahl zwischen 1 & 25 erraten. Du hast 5 Versuche je Runde.")
        print(" Insgesamt hast du 5 Runden Zeit zu gewinnen!")
        time.sleep(4)
        print("\n ++ACHTUNG! Die Zufallszahl ändert sich pro Runde++")
        time.sleep(4)
        print("\n Die erste Runde startet gleich. Viel Glück - Du wirst es brauchen!")
        time.sleep(3)
        return

    def play_rounds(self):
        for i in range(5):
            print("\n\n++++Die Runde startet. Einen Moment bitte!++++")
            time.sleep(3)
            if (self.play_logic()):
                print("Gratulation! Du hast das Spiel gewonnen. Dein Preis 1.000.000,- EUR!")
                return
        print("\n+++Game Over, du hast alle 5 Runden verloren.+++")
        return

    def play_logic(self):
        n = random.randint(1, 25)
        for i in range(5):
            time.sleep(1)
            print("\n" + "Gib eine Zahl ein:")
            guess = input()
            guess = int(guess)
            if n < guess:
                print(" Deine Schätzung ist zu hoch")
            elif n > guess:
                print("Deine Schätzung ist zu niedrig")
            else:
                return True
        if n != guess:
            print("\n---Du hast leider nicht die richtige Zahl erraten!---")
        return False


a = Random_Game()
a.play_rounds()


from tkinter import *
root = Tk()
theLabel= Label(root, text='Invest')
theLabel.pack()
root.mainloop()
