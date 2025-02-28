"""
 Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.
"""


import random 
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in the train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in the train no: {self.trainNo} from {fro} to {to} is {random.randint(222, 1200)}")


GIMB = Train(123499)
GIMB.book("Surat", "Bhubaneshwar")
GIMB.getFare("Surat", "Bhubaneshwar")
GIMB.getStatus()