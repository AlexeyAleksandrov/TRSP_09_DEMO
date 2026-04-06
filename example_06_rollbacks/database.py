from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String, Numeric
from datetime import datetime

DATABASE_URL = "postgresql://postgres:1111@localhost:5432/demo_rollbacks_db"

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employees'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    position: Mapped[str] = mapped_column(String(100), nullable=True)
    salary: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)
    hire_date: Mapped[datetime] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
