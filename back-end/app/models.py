from datetime import datetime

from sqlalchemy import UniqueConstraint

from app import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    USER = 1
    MODERATOR = 2
    ADMINISTRATOR = 3

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), unique=True, nullable=False)
    year_of_admission = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Integer, default=0)
    speciality = db.Column(db.String(100))
    verified = db.Column(db.BOOLEAN, default=False)
    role = db.Column(db.Integer, default=USER)

    def is_administrator(self):
        return self.role == self.ADMINISTRATOR

    def is_moderator(self):
        return self.role == self.MODERATOR

    def __repr__(self):
        return "User %r" % self.id


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    header = db.Column(db.String(100), nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    rate = db.Column(db.Integer, default=0)
    subject_tag = db.Column(db.String(20), nullable=False)
    attachment_path = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "Question %r" % self.id


class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    rate = db.Column(db.Integer, default=0)
    attachment_path = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "Answer %r" % self.id


class Verification(db.Model):
    __tablename__ = "verification"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    attachment_path = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return "Verification %r" % self.id


class Leaderboard(db.Model):
    __tablename__ = "leaderboard"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    rating_increase = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer)

    def __repr__(self):
        return "Leaderboard %r" % self.id


class LeaderboardTimestamp(db.Model):
    __tablename__ = "leaderboard_timestamp"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    user_rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "LeaderboardTimestamp %r" % self.id


class UserAndQuestion(db.Model):
    __tablename__ = "user_and_question"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    is_vote_up = db.Column(db.BOOLEAN, nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'question_id', name='user_and_question_uc'),)

    def __repr__(self):
        return "UserAndQuestion %r" % self.id


class UserAndAnswer(db.Model):
    __tablename__ = "user_and_answer"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)
    is_vote_up = db.Column(db.BOOLEAN, nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'answer_id', name='user_and_answer_uc'),)

    def __repr__(self):
        return "UserAndAnswer %r" % self.id


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
