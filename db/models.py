from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Holiday(Base):
    __tablename__ = 'holidays'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    day: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column()

