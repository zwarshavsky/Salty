from flask_sqlalchemy import SQLAlchemy

#import database
DB = SQLAlchemy()


class troll(DB.Model):
    troll_name = DB.Column(DB.String(100), primary_key=True)
    date_created = DB.Column(DB.BigInteger)
    salty_rank = DB.Column(DB.Float, nullable=False)
    salty_comments = DB.Column(DB.Integer, nullable=False)
    comments_total = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return f'<Troll {self.troll_name} --- Salty Ranking {self.salty_rank} >'

class comments(DB.Model):
    comment_uuid = DB.Column(DB.BigInteger, primary_key=True)
    troll_name = DB.Column(DB.String(100), DB.ForeignKey('troll.troll_name'))
    is_salty = DB.Column(DB.Integer)
    text = DB.Column(DB.String(2500))
    date_created = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f'<Troll {self.troll_name} --- Said: {self.text} >'


        
