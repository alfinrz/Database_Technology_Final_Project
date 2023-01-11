import main
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = main.engine)
session = Session()

# Data All

for s in session.query(main.organizers).all():
    print(s.id, s.Name )

# Data with ID less than 15
for s in session.query(main.organizers).filter(main.organizers.id<15):
    print(s.id, s.Name)