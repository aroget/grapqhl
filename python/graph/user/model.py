import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from graph.database import Base
from graph.company.model import CompanyModel


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'),
                        nullable=False)
    company = relationship('CompanyModel',
                           backref=backref('users', lazy=True))
    created_at = Column(DateTime(), default=datetime.datetime.now())
    updated_at = Column(DateTime(), default=datetime.datetime.now())

    def __repr__(self):
        return '<User %r>' % self.username
