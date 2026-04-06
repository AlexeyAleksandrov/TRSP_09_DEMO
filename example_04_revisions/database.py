from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import String
from datetime import datetime

DATABASE_URL = "postgresql://postgres:1111@localhost:5432/demo_revisions_db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

class Book(Base):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    isbn: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=True)
    published_year: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
