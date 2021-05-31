from Room import Room
from Guest import Guest
from Booking import Booking
from inputHandler import handleInput
from utilityFunctions import *

guestObjList = [];
roomObjList = [];
bookingObjList = [];

def addGuest():
    while(True):
        guestName = handleInput("Please enter guest name:", "string", [1,1], None)
        newGuestId = len(guestObjList) + 1
        guestObjList.append(Guest(guestName,newGuestId)) 
        print("Guest {} has been created with guest ID: {}".format(guestName,newGuestId))
        multiChoice = handleInput("Would you like to [A]dd a new guest or [R]eturn to the previous menu? ", "string", [1,1],["A","R"])
        if(multiChoice == 'R'): return

def addRoom():
    while(True):
        while(True):
            enteredRoomNumber = handleInput("Please enter room number:", "integer", None, None)
            roomNumberRepeated = listMatchedProperty(roomObjList,"roomNum", enteredRoomNumber) #checks for duplicate property arguments(object, getterFunction, newPropertyValue)
            if(len(roomNumberRepeated) > 0):
                print("Room already exists.", end =" ")
            else: break
        roomCapacity = handleInput("Please enter room capacity:", "integer", None, None)
        roomObjList.append(Room(enteredRoomNumber,roomCapacity))
        multiChoice = handleInput("Would you like to [A]dd a new room or [R]eturn to the previous menu? ", "string", [1,1],["A","R"])
        if(multiChoice == 'R'): return

def addBooking():
    while(True):
        enteredGuestId = validateGuestId(guestObjList) # validate if entered guestId exists or not
        while(True): #this loop continues if user enters existing room number which does not exceed guest number
            enteredRoomNumber = handleInput("Please enter room number:", "integer", None, None)
            roomNumExists = listMatchedProperty(roomObjList,"roomNum", enteredRoomNumber) 
            if(roomNumExists):
                selectedRoomObj = roomObjList[roomNumExists[0]]  
                roomCapacity = getattr(selectedRoomObj,"roomCapacity")
                enteredGuestNumber = handleInput("Please enter number of guests: ", "integer", [1,None], None) 
                if(roomCapacity < enteredGuestNumber): 
                    print("Guest count exceeds room capacity of: {}".format(roomCapacity))
                    # Optional for suggesting rooms, if it exceeds capacity of accomodation (S_1)
                    accessableRooms = roomThatCanAccomodate(roomObjList,enteredGuestNumber)
                    if(accessableRooms):
                        print("Room(s) that can accomodate here can accomodate current group of {} guests : ".format(enteredGuestNumber))
                        for i in accessableRooms:
                            print(i,", ", end =" ")
                        print("")
                    else:
                        print("No rooms here can accomodate current group {}".format(enteredGuestNumber))
                        return
                    # Optional for suggesting rooms, if it exceeds capacity of accomodation (E_1)
                    while(True): #loop continues until user enters the room that has capacity to accomodate all guests
                        enteredRoomNumber = handleInput("Please enter room number:", "integer", None, None)
                        roomNumExists = listMatchedProperty(roomObjList,"roomNum", enteredRoomNumber) 
                        if(roomNumExists):
                            selectedRoomObj = roomObjList[roomNumExists[0]]  
                            roomCapacity = getattr(selectedRoomObj,"roomCapacity")
                            if(roomCapacity >= enteredGuestNumber): break
                            else: print("Guest count exceeds room capacity of: {}".format(roomCapacity))
                        else:  print("Room does not exist.")
                break # this break statement gets program control out of nested while loop after room to accomodate all guest is found
            else: 
                print("Room does not exist.")
        checkInMonth = handleInput("Please enter check-in month: ", "integer", [1,12], None)
        checkInDay = handleInput("Please enter check-in day: ", "integer", [1,31], None)
        checkOutMonth = handleInput("Please enter check-out month: ", "integer", [checkInMonth,12], None) #input is invalid for checkout month before checkin month
        coutDayLowerLimit = checkInDay  if(checkInMonth == checkOutMonth) else 1  #getting limit for checkout day, for same month checkout day cant be before check in day 
        checkOutDay = handleInput("Please enter check-out day: ", "integer", [coutDayLowerLimit,31], None) #input is invalid for checkout day before checkin day
        checkinDOY = dateToDayNumber(checkInMonth,checkInDay) #checkin day of year
        checkoutDOY = dateToDayNumber(checkOutMonth,checkOutDay) #checkout day of year
        isBookingAvailable = bookingAvailable(checkinDOY,checkoutDOY,enteredRoomNumber,bookingObjList)
        if(isBookingAvailable):
            guestName = getattr(guestObjList[enteredGuestId-1],"name")  
            bookingObjList.append(Booking(guestName,enteredRoomNumber,enteredGuestId,enteredGuestNumber,checkinDOY,checkoutDOY))
            print("*** Booking successful! ***")
        else: 
            while(True): #this loop continues if user enter exixting room number and does not exceed
                enteredRoomNumber = handleInput("Room is not available during that period. Please enter new room number:", "integer", None, None)
                roomNumExists = listMatchedProperty(roomObjList,"roomNum", enteredRoomNumber) 
                isBookingAvailable = bookingAvailable(checkinDOY,checkoutDOY,enteredRoomNumber,bookingObjList)
                if(isBookingAvailable):
                    guestName = getattr(guestObjList[enteredGuestId-1],"name")  
                    bookingObjList.append(Booking(guestName,enteredRoomNumber,enteredGuestId,enteredGuestNumber,checkinDOY,checkoutDOY))
                    print("*** Booking successful! ***")
                    break
        multiChoice = handleInput("Would you like to [A]dd a new booking or [R]eturn to the previous menu? ", "string", [1,1],["A","R"])
        if(multiChoice == 'R'): return 
        
def viewBookings():
    multiChoice = handleInput("Would you like to view [G]uest bookings, [R]oom booking, or e[X]it? ", "string", [1,1],["G","R","X"])
    if(multiChoice == "G"):
        enteredGuestId = validateGuestId(guestObjList)
        matchingBookingList = listMatchedProperty(bookingObjList,"guestId", enteredGuestId)
        showBooking(matchingBookingList,bookingObjList,"guestId") # shows booking according to guest Id
    if(multiChoice == "R"):
        while(True): #this loop continues if user enter existing room number
            enteredRoomNumber = handleInput("Please enter room number:", "integer", None, None)
            roomExists = listMatchedProperty(roomObjList,"roomNum", enteredRoomNumber) 
            if(roomExists):
                break
            else: 
                print("Room does not exist.")
        matchingBookingList = listMatchedProperty(bookingObjList,"roomNum", enteredRoomNumber)
        showBooking(matchingBookingList,bookingObjList,"roomNum") # shows booking according to guest Id
    if(multiChoice == "X"): return 