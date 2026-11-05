from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
class User(Base):
    __tablename__ = "users"
    
    Id : Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(50), nullable=False)
    Email: Mapped[str] = mapped_column(String(100), nullable=False)
    Timezone: Mapped[str] = mapped_column(String(50), nullable=False)
    CreatedAt: Mapped[str] = mapped_column(String(50), nullable=False, default=datetime.utcnow())
    UpdatedAt: Mapped[str] = mapped_column(String(50), nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())