from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import BaseIDModel

if TYPE_CHECKING:
    from models.person import CounterAgentModel


class DeliveryInfoModel(BaseIDModel):
    __tablename__ = "delivery_info"
    counter_agent_id: Mapped[int] = mapped_column(
        ForeignKey("counter_agent.id", ondelete="CASCADE")
    )
    counter_agent: Mapped["CounterAgentModel"] = relationship(
        back_populates="delivery_infos"
    )
    free_delivery_price = Column(Integer, nullable=False)
    delivery_price = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
