from pybo import db

# 질문 model
class Question(db.Model): # db.Model을 상속
    id = db.Column(db.Integer, primary_key=True) # 고유 번호
    subject = db.Column(db.String(200), nullable=False) # 제목
    content = db.Column(db.Text(), nullable=False) # 내용
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일시

# 답변 model
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer,
                            db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', )) # 참조, 역참조
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)