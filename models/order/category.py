from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from models import BaseIDModel

if TYPE_CHECKING:
    from models.order.product import ProductModel
    from models.person import CounterAgentModel


class CategoryModel(BaseIDModel):
    __tablename__ = "category"
    name = Column(String, nullable=False)

    counter_agents: Mapped[list["CounterAgentModel"]] = relationship(
        back_populates="category", cascade="all, delete"
    )
    products: Mapped[list["ProductModel"]] = relationship(
        back_populates="category", cascade="all, delete"
    )
