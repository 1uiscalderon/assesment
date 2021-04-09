#!/usr/bin/python3
""" holds class Order"""

import models
from models.base_model import Base, BaseModel
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    __tablename__ = "orders"
    id = Column(String(60), primary_key=True)
    date = Column(String(128), nullable=False)
    subtotal = Column(String(128), nullable=False)
    taxes = Column(String(128), nullable=False)
    total = Column(String(128), nullable=False)
    shipping = relationship(
        'Shipping', uselist=False, back_populates='order',
        cascade="all, delete, delete-orphan")
    userid = Column(String(128), ForeignKey("users.id"), nullable=False)
    paid = Column(Boolean, default=False)
    payments = relationship('Payment', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.date = datetime.now()
        super().__init__(*args, **kwargs)
