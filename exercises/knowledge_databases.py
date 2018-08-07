from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wikipage, topic, rating):
	    knowledge_object = Knowledge(
	    	wikipage = wikipage,
	    	topic = topic,
	    	rating = rating)
	    session.add(knowledge_object)
	    session.commit()
add_article("123", "blah blah blah", 10)

	

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
print(query_all_articles())



def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		wikipage=topic).first()
	return article
print(query_article_by_topic("blah blah blah"))

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
