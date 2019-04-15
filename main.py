from Theatre import TheatreA,TheatreB 

# List to store all the contacts 
theatresA = []
theatresB = []

def createTheatre():
    aTheatreMrn = TheatreA("A", "Viswasam", "9.30",20,"500")
    aTheatreAft = TheatreA("A", "Viswasam", "1.30",20,"500")
    aTheatreEven = TheatreA("A", "Viswasam", "6.30",20,"500")

    bTheatreMrn = TheatreB("B", "petta", "9.30",4,"400")   
    bTheatreAft = TheatreB("B", "petta", "1.30",3,"400")
    bTheatreEven = TheatreB("B", "petta", "6.30",2,"400") 

    theatresA.append(aTheatreMrn)
    theatresA.append(aTheatreAft)
    theatresA.append(aTheatreEven)

    theatresB.append(bTheatreMrn)
    theatresB.append(bTheatreAft)
    theatresB.append(bTheatreEven)

def displayTheatresName(theatres,theatreName,i):   
    for theatre in theatres:                   
        if theatre.getTheatreName() not in theatreName:
            theatreName.append(theatre.getTheatreName())    

    for x,y in enumerate(theatreName):  
        print("{}{}{}{}".format(x+i,'.',y, '- Theatre show'))
           
def listTheatres():

    aTheatreName = []
    aTheatre = displayTheatresName(theatresA,aTheatreName,1)
    bTheatreName = []
    bTheatre = displayTheatresName(theatresB,bTheatreName,2)
 
def getTheatreDetails(theatreList):
    for theatre_idx,theatre_val in enumerate(theatreList):               
        print(str(theatre_idx + 1) + '.' + theatre_val.getMovieName() + ' ' + theatre_val.getShowTime() + ' ' + str(theatre_val.getSeat()) + ' ' + theatre_val.getPrice())

    choice = int(input("Enter choice: "))        
    if choice <= len(theatreList):    
        book = int(input("Enter Booking Tickets: "))
        theatre = theatreList[choice-1]
        seat = int(theatre.getSeat()) - book
        if seat > 0:           
            theatre.setSeat(seat) 
            print("total ticket prices: ",int(theatre.getPrice()) * book)
            print("Seats are available: ", theatre.getSeat())
        elif seat == 0:
            print("Seats are not available")
            
        else:
            print("Seats are not available")        
    else:
        print("Correct input for booking")       
        

def bookTickets():
    print('Tickets Booking')   
    userInput = int(input("Enter number: ")) 
    if userInput == 1:       
        theatreA = getTheatreDetails(theatresA)

    elif userInput == 2:
        theatreB = getTheatreDetails(theatresB)    
            
    else:
        print("Correct input for select theatre")    


def displayMovies(theatres,theatreMovie,i):   
    for theatre in theatres:                   
        if theatre.getMovieName() not in theatreMovie:
            theatreMovie.append(theatre.getMovieName())    

    for x,y in enumerate(theatreMovie):  
        print("{}{}{}{}".format(x+i,'.',y,'- Movie'))
      

def listMovies():        
    print('All Movies')
    aTheatreMovie = []    
    aTheatre = displayMovies(theatresA, aTheatreMovie,1)        
    bTheatreMovie = []        
    bTheatre = displayMovies(theatresB,bTheatreMovie,2)

def printMenu():
    print("Menu")
    print("1. ListTheatre\n2. BookingTickets\n3. ListMovie\n4. Exit")

  
def startApp():
    createTheatre()
    while True:
        printMenu()
        userChoice = int(input("Enter Your choice: "))           
        if userChoice == 1:
            listTheatres()
        elif userChoice == 2:
            listTheatres()
            bookTickets()
        elif userChoice == 3:
            listMovies()
        elif userChoice == 4:
            exit()            
        else:
            print('Invalid choice')

def main():
    print("---Theatres---")
    startApp()

if __name__ == "__main__":
    main()
