from dataclasses import dataclass
from datetime import datetime

from flask_login import UserMixin
from safrs import SAFRSBase
from sqlalchemy import UniqueConstraint

from app import db, swagger


class User(SAFRSBase, db.Model, UserMixin):
    """
        description: Работа с пользователем
    """
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

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'year_of_admission': self.year_of_admission,
            'university': self.university,
            'rating': self.rating,
            'speciality': self.speciality,
            'verified': self.verified,
            'role': self.role
        }


class Question(SAFRSBase, db.Model):
    """
        description: Взаимодействие с вопросами
    """
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

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'header': self.header,
            'description': self.description,
            'date_time': self.date_time,
            'rate': self.rate,
            'subject_tag': self.subject_tag,
            'attachment_path': self.attachment_path
        }


class Answer(SAFRSBase, db.Model):
    """
    description: Взаимодействие с ответами
    """
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

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'question_id': self.question_id,
            'description': self.description,
            'date_time': self.date_time,
            'rate': self.rate,
            'attachment_path': self.attachment_path
        }


class Verification(SAFRSBase, db.Model):
    """
    description: Заявки на верификацию
    """
    __tablename__ = "verification"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    attachment_path = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return "Verification %r" % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'attachment_path': self.attachment_path
        }


class Leaderboard(SAFRSBase, db.Model):
    """
    description: Описание таблицы лидеров
    """
    __tablename__ = "leaderboard"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    rating_increase = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer)

    def __repr__(self):
        return "Leaderboard %r" % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'rating_increase': self.rating_increase,
            'points': self.points
        }


class LeaderboardTimestamp(SAFRSBase, db.Model):
    """
    description: Описание снимка таблицы лидеров
    """
    __tablename__ = "leaderboard_timestamp"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)
    user_rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "LeaderboardTimestamp %r" % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_rating': self.user_rating
        }


class UserAndQuestion(SAFRSBase, db.Model):
    """
    description: Взаимодействие пользователь -> вопрос
    """
    __tablename__ = "user_and_question"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    is_vote_up = db.Column(db.BOOLEAN, nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'question_id', name='user_and_question_uc'),)

    def __repr__(self):
        return "UserAndQuestion %r" % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'question_id': self.question_id,
            'is_vote_up': self.is_vote_up
        }


class UserAndAnswer(SAFRSBase, db.Model):
    """
    description: Взаимодействие пользователь -> ответ
    """
    __tablename__ = "user_and_answer"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    answer_id = db.Column(db.Integer, nullable=False)
    is_vote_up = db.Column(db.BOOLEAN, nullable=False)
    __table_args__ = (UniqueConstraint('user_id', 'answer_id', name='user_and_answer_uc'),)

    def __repr__(self):
        return "UserAndAnswer %r" % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'answer_id': self.answer_id,
            'is_vote_up': self.is_vote_up
        }


swagger.expose_object(User)
swagger.expose_object(Question)
swagger.expose_object(Answer)
swagger.expose_object(Verification)
swagger.expose_object(Leaderboard)
swagger.expose_object(LeaderboardTimestamp)
swagger.expose_object(UserAndQuestion)
swagger.expose_object(UserAndAnswer)


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
