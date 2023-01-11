from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, CHAR, BOOLEAN
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo = True)
Base = declarative_base()

"""
Organizer
    id int
    Name str
    Events str

"""

class organizers(Base):
    __tablename__ = 'organizers'
    id = Column(Integer(), primary_key = True)
    Name = Column(String(40))
    Events = Column(String(150), unique = False)

    def __init__(self, id, Name, Events):
        self.id = id
        self.Name = Name
        self.Events = Events

class Events(Base):
    __tablename__ = 'Event'
    Eventid = Column(Integer(), ForeignKey('organizers.Events'))
    EventName = Column(String())
    Booking = Column(Integer())
    Venues = Column(String())
    TotalSales = Column(Integer())

    def __init__(self, Eventid, EventName, Booking, Venues, TotalSales):
        self.Eventid = Eventid
        self.Eventid = EventName
        self.Booking = Booking
        self.Venues = Venues
        self.TotalSales = TotalSales

class Venue(Base):
    __tablename__ = 'Venue'
    VenueId = Column(Integer(), primary_key = True)
    EventId = Column(Integer())
    Capacity = Column(Integer())
    numAvailable = Column(Integer())
    isFull = Column(BOOLEAN())
    TicketPrice = Column(Integer())
    TicketsSold = Column(Integer())
    BookingSales = Column(Integer())

    def __init__(self, VenueId, EventId, Capacity, numAvailable, isFull, TicketPrice, TicketsSold, BookingSales):
        self.VenueId = VenueId
        self.EventId = EventId
        self.Capacity = Capacity
        self.numAvailable = numAvailable
        self.isFull = isFull
        self.TicketPrice = TicketPrice
        self.TicketsSold = TicketsSold
        self.BookingSales = BookingSales

class Booking(Base):
    __tablename__ = 'Booking'
    Datestart = Column(DateTime())
    DateEnd = Column(DateTime())
    TimeStart = Column(DateTime())
    TimeEnd = Column(DateTime())

    def __init__(self, Datestart, DateEnd, TimeStart, TimeEnd):
        self.Datestart = Datestart
        self.DateEnd = DateEnd
        self.TimeStart = TimeStart
        self.TimeEnd = TimeEnd

class Ticket_Order(Base):
    __tablename__ = 'Ticket_order'
    OrderId = Column(Integer(), primary_key = True)
    TicketsOrdered = Column(Integer())
    OrderDate = Column(DateTime())
    TotalPrice = Column(Integer())

    def __init__(self, OrderId, TicketsOrdered, OrderDate, TotalPrice):
        self.OrderId = OrderId
        self.TicketsOrdered = TicketsOrdered
        self.OrderDate = OrderDate
        self.TotalPrice = TotalPrice

class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer(), primary_key = True)
    CustomerOrder = Column(Integer()) 




Base.metadata.create_all(engine)

# new_user_1 = Organizer (id = 1, Name = "Kezia", Events = "Spring Festival")

# print (new_user_1)