import uuid
from datetime import datetime
from sqlalchemy import UUID
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Float, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Annotated

uuid_pk = Annotated[uuid.UUID, mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )]

created_at = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=func.now(), 
    nullable=False,

)]
updated_at = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=func.now(), 
    nullable=False,

)]

class BaseDBModel(DeclarativeBase):
    __tablename__: str
    __table_args__: dict[str, str] | tuple = {'schema': 'db_schema'}

    @classmethod
    def group_by_fields(cls, exclude: list[str] | None = None) -> list:
        payload = []
        if not exclude:
            exclude = []

        for column in cls.__table__.columns:
            if column.key in exclude:
                continue

            payload.append(column)

        return payload

class UserModel(BaseDBModel):
    __tablename__ = 'users'
    id: Mapped[uuid_pk]
    first_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        default='Гость'
    )
    last_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        default='Гость'
    )
    middle_name: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        default=None
    )
    phone: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class CategoriesModel(BaseDBModel):
    __tablename__ = "categories"
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class ColorsModel(BaseDBModel):
    __tablename__ = "colors"
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class ColorsModel(BaseDBModel):
    __tablename__ = "colors"
    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class CatalogModel(BaseDBModel):
    __tablename__ = 'catalog'
    id: Mapped[uuid_pk]
    id_categories: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey('db_schema.categories.id'),
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    discount: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]