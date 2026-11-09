from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.base import Base

from middleware.utc_time_middleware import utc_timestamp



class User(Base):
    __tablename__ = "users"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(50), nullable=False)
    Email: Mapped[str] = mapped_column(String(100), nullable=False)
    Timezone: Mapped[str] = mapped_column(String(50), nullable=False)
    CreatedAt: Mapped[str] = mapped_column(String(50), default=utc_timestamp)
    UpdatedAt: Mapped[str | None] = mapped_column(String(50), nullable=True, onupdate=utc_timestamp)

