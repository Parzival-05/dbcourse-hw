from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseIDModel

if TYPE_CHECKING:
    from models.order.category import CategoryModel
    from models.order.order import OrderModel
    from models.person import CounterAgentModel


class ProductModel(BaseIDModel):
    __tablename__ = "product"
    name = Column(String, nullable=False, unique=True)
    weight = Column(Float, nullable=False)
    size = Column(String, nullable=False)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="CASCADE")
    )
    category: Mapped["CategoryModel"] = relationship(back_populates="products")

    counter_agents: Mapped[list["CounterAgentModel"]] = relationship(
        back_populates="products",
        secondary="product_counter_agent_info",
        cascade="all, delete",
    )
    orders: Mapped[list["OrderModel"]] = relationship(
        back_populates="products",
        secondary="product_in_order",
        cascade="all, delete",
    )
