#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import Base, BaseModel
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    gov_id = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    company = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    orders = relationship("Order", cascade="all, delete-orphan")
    username = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        super().__init__(*args, **kwargs)
