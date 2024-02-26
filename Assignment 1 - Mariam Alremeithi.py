from enum import Enum
from datetime import datetime


# Enum representing the gender of a passenger (male or female)
class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


# Enum representing the nationality of a passenger
class Nationality(Enum):
    EMARATI = "Emarati"
    SAUDI = "Saudi"
    KUWAITI = "Kuwaiti"
    OTHER = "Other"


# Enum representing the type of aircraft
class AircraftType(Enum):
    BOEING = "Boeing"
    AIRBUS = "Airbus"
    EMBRAER = "Embraer"


# Enum representing the class of the passenger flight
class ClassType(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST = "First"


class User:
    # initialize the Users class attributes
    def __init__(self, firstName, lastName, gender, dateOfBirth, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber

    # getters and setters
    # getters retrieve attribute.
    def getFirstName(self):
        return self.firstName

    # setter sets the value
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getDateOfBirth(self):
        return self.dateOfBirth

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    # returns a string representation of the User object
    def __str__(self):
        return f"User: {self.firstName} {self.lastName}, Gender: {self.gender.value}, Date of Birth: {self.dateOfBirth}, Phone Number: {self.phoneNumber}"


# The Passenger class inherits from the User class
class Passenger(User):
    # initialize the Passenger class attributes
    def __init__(self, firstName, lastName, gender, dateOfBirth, phoneNumber, passportNum, nationality,
                 frequentFlyerNumber, dietaryRestrictions, preferredAirline):
        # The super function is used to call the __init__ method of the User parent class which initializes its attributes
        super().__init__(firstName, lastName, gender, dateOfBirth, phoneNumber)
        # attributes specific to the Passenger class
        self.passportNum = passportNum
        self.nationality = nationality
        self.frequentFlyerNumber = frequentFlyerNumber
        self.dietaryRestrictions = dietaryRestrictions
        self.preferredAirline = preferredAirline

    #  Getter and Setter for passportNum attribute
    def getPassportNum(self):
        return self.passportNum

    def setPassportNum(self, passportNum):
        self.passportNum = passportNum

    # Getter and Setter for nationality attribute
    def getNationality(self):
        return self.nationality

    def setNationality(self, nationality):
        self.nationality = nationality

    # Getter and Setter for frequentFlyerNumber attribute
    def getFrequentFlyerNumber(self):
        return self.frequentFlyerNumber

    def setFrequentFlyerNumber(self, frequentFlyerNumber):
        self.frequentFlyerNumber = frequentFlyerNumber

    # Getter and Setter for dietaryRestrictions attribute
    def getDietaryRestrictions(self):
        return self.dietaryRestrictions

    def setDietaryRestrictions(self, dietaryRestrictions):
        self.dietaryRestrictions = dietaryRestrictions

    # Getter and Setter for preferredAirline attribute
    def getPreferredAirline(self):
        return self.preferredAirline

    def setPreferredAirline(self, preferredAirline):
        self.preferredAirline = preferredAirline

    def __str__(self):
        return f"Passenger: {self.firstName} {self.lastName}, Passport: {self.passportNum}, Nationality: {self.nationality.value}, Frequent Flyer Number: {self.frequentFlyerNumber}, Dietary Restrictions: {self.dietaryRestrictions}, Preferred Airline: {self.preferredAirline}"


class AirlineSystem:
    def __init__(self, airlineName, aircraftType, flight_Number, passenger_capacity, baggageAllowance):
        self.airlineName = airlineName
        self.aircraftType = aircraftType
        self.flight_Number = flight_Number
        self.passenger_capacity = passenger_capacity
        self.baggageAllowance = baggageAllowance

    def getAirlineName(self):
        # when implemented: it would return the airline name
        pass

    def setAirlineName(self, airlineName):
        # when implemented: it would set the airline name
        pass

    def getAircraftType(self):
        # when implemented: it would return the aircraft type
        pass

    def setAircraftType(self, aircraftType):
        # when implemented: it would set the aircraft type
        pass

    def getFlight_Number(self):
        return self.flight_Number

    def setFlight_Number(self, flight_Number):
        self.flight_Number = flight_Number

    def getPassengerCapacity(self):
        # when implemented: it would return the passenger capacity
        pass

    def setPassengerCapacity(self, passenger_capacity):
        # when implemented: it would set the passenger capacity
        pass

    def getBaggageAllowance(self):
        # when implemented: it would return the baggage allowance
        pass

    def setBaggageAllowance(self, baggageAllowance):
        # when implemented: it would set the baggage allowance
        pass

    # a method that returns a string representation of the Passenger object
    def __str__(self):
        return f"Airline System: {self.airlineName}, Aircraft Type: {self.aircraftType}, Flight Number: {self.flight_Number}, Passenger Capacity: {self.passenger_capacity}, Baggage Allowance: {self.baggageAllowance}"
        pass


class Ticket:
    # initialize the Ticket class attributes
    def __init__(self, passengerName, destinationTo, destinationFrom, departureDate, classType, seat_num, flightPrice):
        self.passengerName = passengerName
        self.destinationTo = destinationTo
        self.destinationFrom = destinationFrom
        self.departureDate = departureDate
        self.classType = classType
        self.seat_num = seat_num
        self.flightPrice = flightPrice

    # Getter and Setter for setting values and retrieving attributes.
    def getPassportNum(self):
        return self.passportNum

    def setPassportNum(self, passportNum):
        self.passportNum = passportNum

    def getNationality(self):
        return self.nationality

    def setNationality(self, nationality):
        self.nationality = nationality

    def getFrequentFlyerNumber(self):
        return self.frequentFlyerNumber

    def setFrequentFlyerNumber(self, frequentFlyerNumber):
        self.frequentFlyerNumber = frequentFlyerNumber

    def getDietaryRestrictions(self):
        return self.dietaryRestrictions

    def setDietaryRestrictions(self, dietaryRestrictions):
        self.dietaryRestrictions = dietaryRestrictions

    def getPreferredAirline(self):
        return self.preferredAirline

    def setPreferredAirline(self, preferredAirline):
        self.preferredAirline = preferredAirline

    # a method that returns a string representation of the ticket object
    def __str__(self):
        return f"Ticket: Passenger Name: {self.passengerName}, Destination: {self.destinationTo} to {self.destinationFrom}, Departure Date: {self.departureDate}, Class: {self.classType}, Seat Number: {self.seat_num}, Price: {self.flightPrice}"
        pass


class BoardingPass(Ticket):
    # Initializing the attributes of the BoardingPass class
    def __init__(self, passengerName, destinationTo, destinationFrom, departureDate, classType, seat_num, flightPrice,
                 seatNumber, gateNumber, boardingTime, terminal, flightNumber):
        # used to call the __init__ method of the Ticket parent class which initializes its attributes
        super().__init__(passengerName, destinationTo, destinationFrom, departureDate, classType, seat_num, flightPrice)
        self.seatNumber = seatNumber
        self.gateNumber = gateNumber
        self.boardingTime = boardingTime
        self.terminal = terminal
        self.flightNumber = flightNumber

    # getters and setters
    def getSeatNumber(self):
        return self.seatNumber

    def setSeatNumber(self, seatNumber):
        self.seatNumber = seatNumber

    def getGateNumber(self):
        return self.gateNumber

    def setGateNumber(self, gateNumber):
        self.gateNumber = gateNumber

    def getBoardingTime(self):
        return self.boardingTime

    def setBoardingTime(self, boardingTime):
        self.boardingTime = boardingTime

    def getTerminal(self):
        return self.terminal

    def setTerminal(self, terminal):
        self.terminal = terminal

    def getFlightNumber(self):
        return self.flightNumber

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    # a method that returns a string representation of the boarding pass object
    def __str__(self):
        return f"Boarding Pass: Passenger Name: {self.passengerName}, Destination: {self.destinationTo} to {self.destinationFrom}, Departure Date: {self.departureDate}, Class: {self.classType.value}, Seat Number: {self.seat_num}, Price: {self.flightPrice}, Seat: {self.seatNumber}, Gate: {self.gateNumber}, Boarding Time: {self.boardingTime}, Terminal: {self.terminal}, Flight Number: {self.flightNumber}"


# Instance for Passenger class
passenger = Passenger("James", "Smith", Gender.MALE, datetime.now(), "1234567890", "P1234567", Nationality.EMARATI,
                      "FF123456", "None", "NATIONAL AIRLINE")
print(passenger)

# Instance for BoardingPass
boarding_pass = BoardingPass("James Smith", "CHICAGO, ORD ", "NEW YORK, JFK", datetime(2022, 12, 1), ClassType.FIRST,
                             "09A", 500.0, "09A", "03", datetime(2022, 12, 1, 11, 40, 0), "T2", "NA4321")
print(boarding_pass)
