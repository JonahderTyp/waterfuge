from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import List, Type, TypeVar

from flask import current_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql.expression import and_

from .exceptions import ElementAlreadyExists, ElementDoesNotExsist

db = SQLAlchemy()

T = TypeVar('T', bound='BaseTable')


class BaseTable(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_via_id(cls: Type[T], id: int) -> T:
        item = cls.query.get(id)
        if not item:
            raise ElementDoesNotExsist(
                f"{str(cls.__name__)} mit der ID \"{id}\" existiert nicht")
        return item

    @classmethod
    def get_all(cls: Type[T]) -> List[T]:
        return cls.query.all()


class Sensor(BaseTable):
    __tablename__ = "sensors"

    name = Column(String(50), nullable=False)
    flow = Column(Integer, default=0)
    rpm = Column(Integer, default=0)
    last_online = Column(DateTime, default=datetime.now)

    def is_online(self):
        # If the latest date is not older than 10 seconds
        timediff: timedelta = (datetime.now() - self.last_online)
        return timediff.total_seconds() < 10

    def update_values(self, flow: int, rpm: int):
        self.flow = int(flow)
        self.rpm = int(rpm)
        self.last_online = datetime.now()
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "online": self.is_online(),
            "name": self.name,
            "flow": self.flow,
            "rpm": self.rpm
        }

    @staticmethod
    def create_sensor(name: str) -> Sensor:
        sensor = Sensor(name=name)
        db.session.add(sensor)
        db.session.commit()
        return sensor
