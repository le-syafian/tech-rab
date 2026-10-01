from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RabItem(Base):
    __tablename__ = 'rab_items'
    id = Column(Integer, primary_key=True, index=True)
    uraian = Column(String)
    satuan = Column(String)
    volume = Column(Float)
    harga_satuan = Column(Float)
    total = Column(Float)
