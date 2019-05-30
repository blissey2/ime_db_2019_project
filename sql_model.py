from sqlalchemy import Column, String, Integer, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://aws 주소')
Session = sessionmaker(bind=engine)
Base = declarative_base()


# total_info_association = Table(
#     'total_info', Base.metadata,
#     Column('movie_id', Integer, ForeignKey('movies.id')),
#     Column('actor_id', Integer, ForeignKey('actors.id'))
# )


class Region(Base):                                  # 지역 구분
    __tablename__ = 'regions'




class Category(Base):                                # 종목 구분
    __tablename__ = 'categories'



class Information(Base):                            # 종합 정보
    __tablename__ = 'informations'