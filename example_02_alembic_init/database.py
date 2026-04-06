from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String

DATABASE_URL = "postgresql+pg8000://postgres:1111@localhost:5432/demo_alembic_db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
