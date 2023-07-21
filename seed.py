from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()


# Add pets
whiskey = Pet(name='Whiskey',
                species="dog",
                age='10',
                notes='likes to be cuddled',
                avb=True)
bowser = Pet(name='Bowser', 
              species="cat",
              age='4',
              notes='tends to pee everywhere',
              avb=True)
spike = Pet(name='Spike', 
             species="porcupine",
             age='2',
             notes='kinda prickly',
             avb=True)
wiskers = Pet(name='Wiskers', 
             species="cat",
             age='60',
             notes='Very cute and cuddle',
             avb=False)




# Add new objects to session and commit
db.session.add_all([whiskey,bowser,spike, wiskers])
db.session.commit()