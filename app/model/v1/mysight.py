from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, String


class MySight(Base):
    __tablename__ = "mysight"
    sight_id = Column(Integer, primary_key=True)
    sight_name = Column(String(100))
    sight_address = Column(String(200))
    sight_intro = Column(String(200))
    sight_point = Column(Integer)
    sight_dist = Column(String(100))
    sight_img = Column(String(1000))
