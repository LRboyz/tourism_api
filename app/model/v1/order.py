from sqlalchemy import Column, String, Integer, DateTime
from lin.interface import InfoCrud as Base


class Order(Base):
    __tablename__ = "order"
    # 有其他后续再添加！
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_time = Column(DateTime())
    inDate = Column(String())
    outDate = Column(String())
    inTime = Column(DateTime())
    outTime = Column(DateTime())
    room_type = Column(String(100))
    check_name = Column(String(100))
    check_phone = Column(String(100))
    check_num = Column(Integer())
    price = Column(Integer())
    remark = Column(String(100))
    order_status = Column(String(100))
