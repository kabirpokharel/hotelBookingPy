from inputHandler import handleInput
from mainFunctions import *
continueMainMenu = True;

menuOptions = ["Add guest","Add room","Add booking","View bookings","Quit"]
menuFunc = [addGuest,addRoom,addBooking,viewBookings]

def showMainMenu(menuList):
    print("Main Menu - please select an option:")
    for index, option in enumerate(menuList, start = 1):    #using enumerate to print menu list
        print('{}.) {}'.format(index,option));  

def optionProcess(mainMenuInput):
    global continueMainMenu
    if(mainMenuInput == 5):
        print("Thanks for using FedUni Hotel Bookings!")
        continueMainMenu = False
    else:
        menuFunc[mainMenuInput - 1]();  #using list index to call a funciton, corresponding to user choice in main menu

print("----------------------------------------------- \n------ Welcome to FedUni Hotel Bookings -------\n-----------------------------------------------")
while(continueMainMenu):
    showMainMenu(menuOptions)
    mainMenuInput = handleInput("Enter a number: ", "integer", [1,5], None)
    optionProcess(mainMenuInput)
