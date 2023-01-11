import main
from sqlalchemy.orm import sessionmaker
import random
import randomname

Session = sessionmaker(bind = main.engine)
session = Session()

Name_random = randomname.get_name(noun = ('automobiles'))
Event_randomize = ["spring festival", "farewell Dinner", "Orientation", 
"Summer Festival", "camp"]


for t in range (10,20):
    id = random.randint(0,500)
    Events = random.choice(Event_randomize)
    Name_random = randomname.get_name(noun = ('automobiles'))
    org = main.organizers(t, Name_random, Events)
    
    session.add(org)

session.commit()