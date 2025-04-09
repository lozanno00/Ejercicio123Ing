from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Database connection
engine = create_engine("sqlite:///games.db")
Session = sessionmaker(bind=engine)
session = Session()

# Models
class HanoiResult(Base):
    __tablename__ = "hanoi_results"
    id = Column(Integer, primary_key=True)
    num_disks = Column(Integer, nullable=False)
    result = Column(Text, nullable=False)

class KnightTourResult(Base):
    __tablename__ = "knight_tour_results"
    id = Column(Integer, primary_key=True)
    board_size = Column(Integer, nullable=False)
    result = Column(Text, nullable=False)

class NQueensResult(Base):
    __tablename__ = "nqueens_results"
    id = Column(Integer, primary_key=True)
    board_size = Column(Integer, nullable=False)
    result = Column(Text, nullable=False)

# Create tables
Base.metadata.create_all(engine)
