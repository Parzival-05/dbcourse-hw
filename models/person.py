from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseIDModel

if TYPE_CHECKING:
    from models.association import ProductInOrder
    from models.delivery_info import DeliveryInfoModel
    from models.order.category import CategoryModel
    from models.order.order import OrderModel
    from models.order.product import ProductModel


class PersonModel(BaseIDModel):
    __tablename__ = "person"
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    counter_agents: Mapped[list["CounterAgentModel"]] = relationship(
        back_populates="person", cascade="all, delete"
    )
    customers: Mapped[list["CustomerModel"]] = relationship(
        back_populates="person", cascade="all, delete"
    )


class CounterAgentModel(BaseIDModel):
    __tablename__ = "counter_agent"
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="CASCADE")
    )

    person: Mapped["PersonModel"] = relationship(back_populates="counter_agents")
    category: Mapped["CategoryModel"] = relationship(back_populates="counter_agents")

    delivery_infos: Mapped[list["DeliveryInfoModel"]] = relationship(
        back_populates="counter_agent", cascade="all, delete"
    )

    products: Mapped[list["ProductModel"]] = relationship(
        back_populates="counter_agents",
        secondary="product_counter_agent_info",
        cascade="all, delete",
    )
    products_in_order: Mapped[list["ProductInOrder"]] = relationship(
        back_populates="counter_agent", cascade="all, delete"
    )


class CustomerModel(BaseIDModel):
    __tablename__ = "customer"
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
    person: Mapped["PersonModel"] = relationship(
        back_populates="customers",
        cascade="all, delete",
    )

    orders: Mapped[list["OrderModel"]] = relationship(
        back_populates="customer", cascade="all, delete"
    )
