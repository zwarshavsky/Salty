from flask_sqlalchemy import SQLAlchemy

#import database
DB = SQLAlchemy()


class Troll(DB.Model):
    troll_name = DB.Column(DB.String(100), primary_key=True)
    date_created = DB.Column(DB.BigInteger)
    salty_rank = DB.Column(DB.Float, nullable=False)
    salty_comments = DB.Column(DB.Integer, nullable=False)
    comments_total = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return f'<Troll {self.troll_name} --- Salty Ranking {self.salty_rank} >'

    
    def serialize_troll(self):
        """ serialize object to return JSON format """
        return {
            "troll_name" : self.troll_name,
            "date_created" : self.date_created, 
            "salty_rank" : self.salty_rank, 
            "salty_comments" : self.salty_comments, 
            "comments_total" : self.comments_total
        }

class Comments(DB.Model):
    comment_uuid = DB.Column(DB.BigInteger, primary_key=True)
    troll_name = DB.Column(DB.String(100), DB.ForeignKey('troll.troll_name'))
    is_salty = DB.Column(DB.Integer)
    text = DB.Column(DB.String(2500))
    date_created = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f'<Troll {self.troll_name} --- Said: {self.text} >'


    def serialize_comments(self):
        """ serialize object to return JSON format """
        return {
            "comment_uuid" : self.comment_uuid, 
            "troll_name" : self.troll_name, 
            "is_salty" : self.is_salty, 
            "text" : self.text, 
            "date_created" : self.date_created
        }


        
