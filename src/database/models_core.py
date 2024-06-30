import datetime
import enum
from typing import Annotated, Optional

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, str_256

metadata_obj = MetaData()

org_table = Table(
    "organizations",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("address", String),
    Column("phone", String),
    Column("website", String),
)


help_type_table = Table(
    "help_types",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)


user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("phone", String),
    Column("email", String),
)

actions_table = Table(
    "actions",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("organization_id", Integer, ForeignKey("organizations.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("help_type_id", Integer, ForeignKey("help_types.id")),
    Column("amount", Integer),
    CheckConstraint("organization_id IS NOT NULL OR user_id IS NOT NULL"),

)

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]
