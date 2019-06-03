from sqlalchemy import Column, String, Integer, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://aws 주소')
Session = sessionmaker(bind=engine)
Base = declarative_base()



class Categories_Detail(Base):                    # 카테고리 테이블
    __tablename__ = 'categories_detail'

    category_id = Column(Integer(),primary_key=True)
    category_name = Column(String(32))

    def __init__(self,category_id,category_name):
        self.category_id = category_id
        self.category_name = category_name


class Region(Base):                                  # 지역 구분
    __tablename__ = 'regions'

    GIGU = column(string(32))
    TEL = column(string(32))
    region_id = column(string(32), ForeignKey('regoin_details.region_id'))

    def __init__(self, GIGU, TEL):

        self.GIGU = GIGU
        self.TEL = TEL


class Region_detail(Base):
    __tablename__ = 'region_details'

    region_id = column(Integer(), primary_key=True)
    region_name = column(string(32))

    def __init__(self, region_id, region_name):

        self.region_id = region_id
        self.region_name = region_name



class Category(Base):                                # 종목 구분
    __tablename__ = 'categories'

    FTC = Column(String(32), primary_key=True)                          ## 지형지물코드
    category_id = Column(Integer(), ForeignKey('categories_detail_as.category_id')) ## 카테고리이름
    #지구구분코드 = Column(integer,ForeignKey('Region.지구구분코드') )
    #이 부분은 혹시 지구구분콛 외래키로 연결해야하는지 몰라서 적어둠.

    def __init__(self, FTC, name):
        self.FTC = FTC
        self.name = name

class Information(Base):                            # 종합 정보
    __tablename__ = 'informations'

    unique_num=Column(integer, primary_key=True)
    name=Column(string(200))
    fee=Column(Integer)
    map=folium.Map(location=[X좌표,Y좌표],zoom_start=13)

    def __init__(self,name,fee,map):
        self.name=name
        self.fee=fee
        self.map=map
