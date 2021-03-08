from sqlalchemy import Column, String, Integer, DateTime, Boolean
from lin.interface import InfoCrud as Base


class CheckInInfo(Base):
    __tablename__ = "check_in_info"
    # 有其他后续再添加！
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer())
    check_name = Column(String(30))
    check_phone = Column(String(30))
    check_price = Column(Integer())
    room_type = Column(String())
    check_num = Column(Integer())
    price = Column(Integer())
    isCheck = Column(Boolean())
    remark = Column(String(30))
