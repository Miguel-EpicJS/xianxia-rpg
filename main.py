from os import system, name
from time import sleep
from random import choice

from world import World
from player import Player
from menu import Menu

from subprocess import call 


def clear():
    _ = system('clear') if name == 'posix' else system('cls')

if __name__ == "__main__":

    clear()

    print("Xianxia World")
    
    player = Player(input("What is your name fellow daoist? ")) 


    menuController = Menu()
    mainWorld = World()

    mainWorld.create()

    while True:
        clear()

        player.stats()
        mainWorld.show()
        menuController.mainMenu()

        option = (input("> "))

        if option == '0':
            break 
        elif option == '1':
            qi = mainWorld.absorb( player.getAmount() )
            if qi:
                print(f"> You got { player.gather() } qi")
            else:
                print(f"> No qi to gather")
            if player.levelUp():
                print(f"> Congratulations!")
            sleep(0.5)
        elif option == '2':
            print(f"> Moving random direction")
            op = [-1, 0, 1]
            mainWorld.move( ( choice(op), choice(op) ) )


    clear()

