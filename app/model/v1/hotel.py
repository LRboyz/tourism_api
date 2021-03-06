from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer


class Hotel(Base):
    __tablename__ = "hotel"
    # 有其他后续再添加！
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(500))
    title = Column(String(100))
    hotel_type = Column(String(500))
    room_type = Column(String(500))
    phone = Column(String(200))
    address = Column(String(200))

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])
