from sqlalchemy import Column, String, Integer, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://aws 주소')
Session = sessionmaker(bind=engine)
Base = declarative_base()


categories_detail_as = Table(                         # 카테고리 정보 테이블
    'categories_detail', Base.metadata,
    Column('category_id', Integer),
    Column('category_name', String(32))
)


class Region(Base):                                  # 지역 구분
    __tablename__ = 'regions'




class Category(Base):                                # 종목 구분
    __tablename__ = 'categories'

    FTC = Column(String(32))                          ## 지형지물코드
    category_id = Column(Integer, ForeignKey('categories_detail_as.category.id')) ## 카테고리이름
    #지구구분코드 = Column(integer,ForeignKey('Region.지구구분코드') )
    #이 부분은 혹시 지구구분콛 외래키로 연결해야하는지 몰라서 적어둠.

    def __init__(self, FTC, name):
        self.FTC = FTC
        self.name = name

class Information(Base):                            # 종합 정보
    __tablename__ = 'informations'
