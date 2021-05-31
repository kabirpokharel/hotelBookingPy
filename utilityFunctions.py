from inputHandler import handleInput

def validateGuestId(guestObjList):
    while(True):
        enteredGuestId = handleInput("Please enter guest ID:", "integer", None, None)
        guestIdExists = listMatchedProperty(guestObjList,"guestId", enteredGuestId) 
        if(guestIdExists):
            return enteredGuestId
        else: 
            print("Guest does not exist.")    

def listMatchedProperty(objectList, propertyName, newPropertyValue):
    matchedPropertyList = []
    for index, property in enumerate(objectList):
        if(newPropertyValue == getattr(property,propertyName)):
            matchedPropertyList.append(index)
    return matchedPropertyList


def dateToDayNumber(month, day):
    if (month == 1 ) :return day;
    if (month == 2 ) :return 31 + day;
    if (month == 3 ) :return 59 + day;
    if (month == 4 ) :return 90 + day;
    if (month == 5 ) :return 120 + day;
    if (month == 6 ) :return 151 + day;
    if (month == 7 ) :return 181 + day;
    if (month == 8 ) :return 212 + day;
    if (month == 9 ) :return 243 + day;
    if (month == 10) :return 273 + day;
    if (month == 11) :return 304 + day;
    return 334 + day;

def dayNumber_to_MonthAndDay(dayNumber):
    if (dayNumber <= 31 ): return [1,dayNumber]; 
    if (dayNumber <= 59 ): return [2,dayNumber - 31]; 
    if (dayNumber <= 90 ): return [3,dayNumber - 59]; 
    if (dayNumber <= 120): return [4,dayNumber - 90]; 
    if (dayNumber <= 151): return [5,dayNumber - 120]; 
    if (dayNumber <= 181): return [6,dayNumber - 151]; 
    if (dayNumber <= 212): return [7,dayNumber - 181]; 
    if (dayNumber <= 243): return [8,dayNumber - 212]; 
    if (dayNumber <= 273): return [9,dayNumber - 243]; 
    if (dayNumber <= 304): return [10,dayNumber - 273]; 
    if (dayNumber <= 334): return [11,dayNumber - 304]; 
    return [12,dayNumber - 334];

def dateFormatter(dayOfYear):
    dateArray = dayNumber_to_MonthAndDay(dayOfYear)
    return str(dateArray[0]) + "/" + str(dateArray[1])

def bookingAvailable(newChekinDay, newCheckoutDay, enteredRoomId,bookingObj):
    selectedRoomIndex = listMatchedProperty(bookingObj,"roomNum",enteredRoomId);
    if (len(selectedRoomIndex) == 0): #if room has never been booked it is available for booking hence returned without furthur operation
        return True
    else:
        for i in selectedRoomIndex: # going though list of booking made for that perticular room, comparing with entered booking and old bookings
            currentCinDay = bookingObj[i].checkinDay
            currentCoutDay = bookingObj[i].checkoutDay
            isBookingAvailable = bookingDoNotOverlap(newChekinDay, newCheckoutDay,currentCinDay,currentCoutDay)
            if(isBookingAvailable == False):
                return False
        return True


def bookingDoNotOverlap(cin_new,cout_new,cin_old,cout_old):
    if((cin_new < cin_old and cout_new < cin_old) or (cin_new > cout_old and cout_new > cout_old)):
        return True
    else: return False


def showBooking(matchingBookingList,bookingObjList,searchParam):
    for i in matchingBookingList:   #extracting all rooms from list of object, of class Room
        obj = bookingObjList[i]
        checkInDate = dateFormatter(obj.checkinDay)
        checkoutDate = dateFormatter(obj.checkoutDay)
        if(searchParam == "guestId"):
            print("Guest {} : {}".format(obj.guestId,obj.guestName))
            print("Booking : Room {}, {} guest(s) from {} to {}.".format(obj.roomNum,obj.guestNum,checkInDate,checkoutDate))
        if(searchParam == "roomNum"):
            print("Room {} bookings:".format(obj.roomNum))
            print("Guest {} – {}, {} guest(s) from {} to {}.".format(obj.guestId,obj.guestName,obj.guestNum,checkInDate,checkoutDate))
        return 