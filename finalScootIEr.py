# Home page
import datetime

# message that pops up when the user opens the app
def welcome():
    print("Welcome to ScootIEr. Relax, don't stress, and enjoy the ride!")


#Username and Password Mechanism
class Login():
    print("To get started, register your username and password or login into an existing account.")
    def __init__(self, file_path):
        self.file_path = file_path
        self.username = str(input("Enter username: "))
        self.password = str(input("Enter password: "))

        usernametruthvalue = False
        passwordtruthvalue = False
        with open(self.file_path, 'r') as file:
                # read all content of a file
            content = file.read()
                # check if string present in a file
            if self.username in content and self.password in content:
                    usernametruthvalue = True
                    passwordtruthvalue = True
            else:
                    print("This username doesn't exist. Please try again")
            if usernametruthvalue == True and passwordtruthvalue == True:
                print("All good! Ready to start scootIEring?")
Login('/Users/nathanz/PyCharmProjects/ADSProject/username.txt')



class Scooter_Positions():
    list_scooters = []
    def _init_(self, scooters_file):
        self.begona = 0
        self.tower = 0
        self.file = scooters_file

    def count_scooters(self):
        with open(self.file, 'r') as file:
            # read all content of a file
            content = file.read()
            # check if scooter is in begona or the tower
            # the arguments of the list are tupples containing the scooterID number and the location
            for scooters in content:
                self.begona = content.count("Begoña")
                self.tower = content.count("Tower")

Scooter_Positions()

class Ride():
    print("Press the start ride button to scan the scooter's QR")
    def _init_(self):
        self.scooter = None
        self.location = None
    def scan(self, scooterID):
        # here the user opens the camera and scans the qr code
        self.scooter = scooterID
    def start(self, location):
        while self.scooter != None:
            self.location = location
        # user presses start ride button
            time = datetime.time.minute
        # users can only use the scooters 5 minutes max to go between the tower and begona station
            print("Your ride has started.")
            time.sleep(180)
            print("Two minutes remaining")
            time.sleep(120)
            print("Your ride is over")
            break

    def end(self):
        # user presses end ride button
        if self.location == 'Tower' or self.location == 'Begona':
        #check if scooter is in a parking space
            self.scooter = None
        print("Thank you so much for riding with us, hope you had a pleasant ride.")
        print("As always, your ride was only 1 Euro. See you soon!")

Ride()
# goes back to home screen
