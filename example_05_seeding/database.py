from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String, Text

DATABASE_URL = "postgresql://postgres:1111@localhost:5432/demo_seeding_db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Country(Base):
    __tablename__ = 'countries'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    code: Mapped[str] = mapped_column(String(3), nullable=False, unique=True)
    capital: Mapped[str] = mapped_column(String(100), nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)

class City(Base):
    __tablename__ = 'cities'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    country_code: Mapped[str] = mapped_column(String(3), nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
