#!/usr/bin/python3
""" holds class Shipping"""

import models
from models.base_model import Base, BaseModel
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Shipping(BaseModel, Base):
    __tablename__ = "shippings"
    id = Column(String(60), primary_key=True)
    adress = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False)
    cost = Column(Float, nullable=False)
    order_id = Column(String(128), ForeignKey("orders.id"))
    order = relationship("Order", back_populates="shipping")

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        super().__init__(*args, **kwargs)
