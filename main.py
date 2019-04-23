from Theatre import Theatre,Movie,Show

# List to store all the theatres 
theatres = []
# List to store all the movies 
movies = []

def createTheatres():
  athreatre = Theatre('A')
  bthreatre = Theatre('B')
  theatres.append(athreatre)
  theatres.append(bthreatre)
  return athreatre,bthreatre

def createShows():
  showMrg = Show("9.30 AM", 20, 500)
  showAft = Show("1.30 PM", 15, 400)
  showEven = Show("6.30 AM", 10, 300)
  show = [showMrg,showAft,showEven]

  newshowMrg = Show("9.30 AM", 20, 500)
  newshowAft = Show("1.30 PM", 15, 400)
  newshowEven = Show("6.30 AM", 10, 300)
  newshow = [newshowMrg,newshowAft,newshowEven]    
  return show, newshow

def createMovies(athreatre,bthreatre,show,newshow):
  movie = Movie("Viswasam", show, athreatre)
  newMovie = Movie("Petta", newshow, bthreatre) 
  movies.append(movie)
  movies.append(newMovie) 

         
def listTheatres():
  for theatre_idx,theatre_val in enumerate(theatres):
    print("{}{}{}{}".format(theatre_idx+1, '.', theatre_val.getTheatreName(), '- theatre'))

def bookTickets(movie):
  show = int(input("Select show : "))       
  if show <= len(movie.getShow()):   
    ticket = int(input("Enter Booking Tickets: "))
    show = movie.getShow()[show-1]
    movieSeat = int(show.getSeat())-ticket
    if movieSeat >= 0:
      show.setSeat(movieSeat) 
      print("total ticket prices: ",int(show.getPrice()) * ticket)
      threatreName = movie.getThreatre()
      print(threatreName.getTheatreName() + " " + "- Threatre")
      print(movie.getMovieName() + " " + "Movie")
      print("{}{}{}{}{} ".format("Booked",   " " , ticket , " ", "tickets"))

    elif movieSeat == 0:
      print("Seats are not available")      
    else:
      print("Seats are not available") 
  else:
    print("Correct input for booking")    

def listShows():
  theatre = int(input("Select threatre: "))
  movie = movies[theatre-1]  
  print(movie.getMovieName())
  for show in movie.getShow():
    print(show.getShowTime() + " - Show " + str(show.getSeat()) + " - Seats " + str(show.getPrice()) + " - Price ")     
  bookTickets(movie) 
    
def listMovies():
    print('All Movies')
    for movie_idx,movie_val in enumerate(movies):
        print("{}{}{}{}".format(movie_idx + 1, '.', movie_val.getMovieName(), '- Movie'))

def printMenu():
    print("Menu")
    print("1. ListTheatre\n2. BookingTickets\n3. ListMovie\n4. Exit")
 
def startApp():
  athreatre,bthreatre = createTheatres()
  show, newshow = createShows()
  createMovies(athreatre,bthreatre,show,newshow)
  while True:
    try:
      printMenu()
      userChoice = int(input("Enter Your choice: "))           
      if userChoice == 1:
          listTheatres()
      elif userChoice == 2:
          listTheatres()
          listShows()
      elif userChoice == 3:
          listMovies()
      elif userChoice == 4:
          exit()            
      else:
          print('Invalid choice')
    except (SyntaxError, ValueError):   
      print("You didn't enter a number") 

def main():
    print("---Theatres---")
    startApp()

if __name__ == "__main__":
    main()
