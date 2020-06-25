from flask import Flask , render_template , request 
import requests
import json
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String, VARCHAR
from sqlalchemy.orm import sessionmaker
import csv

app = Flask(__name__)
engine = create_engine('sqlite:///temp.db' , echo=True , connect_args={'check_same_thread':False})
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Storage(Base):
    __tablename__ = "Storage"

    id = Column(VARCHAR, primary_key=True)
    name = Column(VARCHAR(100) , nullable=False)

    def __repr__(self):
        return f"{self.name} has commented {self.comment_text}"
    
Base.metadata.create_all(engine)

@app.route("/")
def index():
    with open('books.csv','r') as fin:
        dr = csv.DictReader(fin)
        for i in dr:
            obj = Storage(id=i["id"], name=i["name "])
            session.add(obj)
            session.commit()
    return render_template("index.html")

if __name__ == "__main__":
    session = Session()
    app.run(debug=True)