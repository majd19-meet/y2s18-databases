from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'Orginization'
    Orginization_id = Column(Integer, primary_key=True)
    wikipage = Column(String)
    topic = Column(String)
    rating = Column(Integer)

    def __repr__(self):
        return("the organization id: {}\n"
                "wikipage: {}\n"
                "topic: {}\n"
                "rating: {}\n").format(self.Orginization_id, self.wikipage, self.topic, self.rating)

x= Knowledge(Orginization_id=1, wikipage="123", topic="blah blah blah", rating=10)
print(x)






    # Create a table with 4 columns
    # The first column will be the primary key
    # The second column should be a string representing
    # the name of the Wiki article that you're referencing
    # The third column will be a string representing the 
    # topic of the article. The last column will be
    # an integer, representing your rating of the article.

