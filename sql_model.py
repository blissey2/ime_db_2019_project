from sqlalchemy import Column, String, Integer, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://aws 주소')
Session = sessionmaker(bind=engine)
Base = declarative_base()

info_association = Table(
    'total_information', Base.metadata,
    Column('RegionID', String(32), ForeignKey('regions.Code')),
    Column('CategoryID', String(32), ForeignKey('categories.Code')),
    Column('InfoID', Integer, ForeignKey('informations.ID'))
)


class Region(Base):                                  # 지역 구분
    __tablename__ = 'regions'

    Code = Column(String(32), primary_key=True)
    Latitude = Column(Integer)
    Longitude = Column(Integer)

    def __init__(self, Code, Latitude, Longitude):

        self.Code = Code
        self.Latitude = Latitude
        self.Longitude = Longitude



class Category(Base):                                # 종목 구분
    __tablename__ = 'categories'

    Code = Column(String(32), primary_key=True)
    name = Column(String(32))

    def __init__(self, Code, name):
        self.Code = Code
        self.name = name


class Information(Base):                            # 종합 정보
    __tablename__ = 'informations'

    ID = Column(Integer, primary_key=True)
    name = Column(String(64))
    TEL = Column(String(64))
    fare = Column(String(256))

    def __init__(self, ID, name, TEL, fare):
        self.ID = ID
        self.name = name
        self.TEL = TEL
        self.fare = fare
