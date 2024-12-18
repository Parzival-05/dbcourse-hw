from models import BaseModel
from models.all_models import *  # noqa: F403
from models.engine import engine

BaseModel.metadata.create_all(engine)


if __name__ == "__main__":
    0
