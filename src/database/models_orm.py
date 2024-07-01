import datetime
from typing import Annotated, Optional

from sqlalchemy import (
    ForeignKey,
    String,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[intpk]
    name: Mapped[str]
    address: Mapped[Optional[str]] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(30))
    website: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    needs: Mapped[list["OrgNeeds"]] = relationship(
        back_populates="organization",
    )
    # org_actions: Mapped[list["Actions"]] = relationship(
    #     back_populates="organization",
    # )

    def __repr__(self) -> str:
        return f"Organization(id={self.id}, name={self.name}, phone={self.phone})"
    

class Helptype(Base):
    __tablename__ = "help_types"

    id: Mapped[intpk]
    name: Mapped[str]
    # actions: Mapped[list["Actions"]] = relationship(
    #     back_populates="help_type",
    # )


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    # user_actions: Mapped[list["Actions"]] = relationship(
    #     back_populates="user",
    # )



class Actions(Base):
    __tablename__ = "actions"

    id: Mapped[intpk]
    description: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    help_type_id: Mapped[int] = mapped_column(ForeignKey("help_types.id", ondelete="CASCADE"))
    amount: Mapped[int]
    action_date: Mapped[datetime.datetime]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    organization: Mapped["Organization"] = relationship(backref="org_actions",  foreign_keys=[organization_id])
    user: Mapped["User"] = relationship(backref="user_actions",  foreign_keys=[user_id])

    def __repr__(self):
        return f"Action(id={self.id}, organization={self.organization_id}, amount={self.amount}, action_date={self.action_date})"
    

class OrgNeeds(Base):
    __tablename__ = "org_needs"

    id: Mapped[intpk]
    description: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"))
    help_type_id: Mapped[int] = mapped_column(ForeignKey("help_types.id", ondelete="CASCADE"))
    amount: Mapped[int]
    organization: Mapped["Organization"] = relationship(
        back_populates="needs",
    )


class UserСapability(Base):
    __tablename__ = "user_capabilities"

    id: Mapped[intpk]
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    help_type_id: Mapped[int] = mapped_column(ForeignKey("help_types.id", ondelete="CASCADE"))
    amount: Mapped[int]

