from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseIDModel

if TYPE_CHECKING:
    from models.order.product import ProductModel
    from models.person import CustomerModel


class OrderModel(BaseIDModel):
    __tablename__ = "order"

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer.id", ondelete="CASCADE")
    )
    customer: Mapped["CustomerModel"] = relationship(back_populates="orders")

    time_stamp = Column(DateTime, nullable=False)

    products: Mapped[list["ProductModel"]] = relationship(
        back_populates="orders",
        secondary="product_in_order",
        cascade="all, delete",
    )
