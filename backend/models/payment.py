#!/usr/bin/python3
""" holds class Order"""

import models
from models.base_model import Base, BaseModel
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    __tablename__ = 'payments'
    payment_type = Column(String(128), nullable=False)
    txn_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(128), nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String(128), default='Pending')
    order_id = Column(String(128), ForeignKey('orders.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.date = datetime.now()
        super().__init__(*args, **kwargs)
