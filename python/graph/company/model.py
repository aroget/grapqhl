import datetime
from sqlalchemy import Column, Integer, String, DateTime

from graph.database import Base


class CompanyModel(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.now())
    updated_at = Column(DateTime(), default=datetime.datetime.now())

    def __repr__(self):
        return '<CompanyModel %r>' % self.name
