from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseModel

if TYPE_CHECKING:
    from models.person import CounterAgentModel


class ProductCounterAgentInfo(BaseModel):
    __tablename__ = "product_counter_agent_info"
    product_id: Mapped[Integer] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"), primary_key=True
    )
    counter_agent_id: Mapped[Integer] = mapped_column(
        ForeignKey("counter_agent.id", ondelete="CASCADE"), primary_key=True
    )

    price = Column(Float, nullable=False)

    # product: Mapped["ProductModel"] = relationship(back_populates="counter_agents")
    # counter_agent: Mapped["CounterAgentModel"] = relationship(back_populates="products")


class ProductInOrder(BaseModel):
    __tablename__ = "product_in_order"
    product_id: Mapped[Integer] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"), primary_key=True
    )
    order_id: Mapped[Integer] = mapped_column(
        ForeignKey("order.id", ondelete="CASCADE"), primary_key=True
    )
    counter_agent_id: Mapped[Integer] = mapped_column(
        ForeignKey("counter_agent.id", ondelete="CASCADE")
    )
    counter_agent: Mapped["CounterAgentModel"] = relationship(
        back_populates="products_in_order"
    )

    price = Column(Float, nullable=False)
    count = Column(Integer, nullable=False)

    # product: Mapped["ProductModel"] = relationship(back_populates="orders")
    # order: Mapped["OrderModel"] = relationship(back_populates="products")
