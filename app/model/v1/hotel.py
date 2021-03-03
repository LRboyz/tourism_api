from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer


class Hotel(Base):
    # 有其他后续再添加！
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(500))
    title = Column(String(100))
    type = Column(String(500))
    house_type = Column(String(500))
    phone = Column(Integer())
    address = Column(String(200))
