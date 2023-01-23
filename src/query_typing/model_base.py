from dataclasses import dataclass
from typing import List, TypeVar, Generic, Type


@dataclass
class ModelBase:
    id: int


ModelType = TypeVar("ModelType", bound=ModelBase)


class QueryBase(Generic[ModelType]):
    class NotFoundError(Exception):
        pass

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()

        class NotFoundError(QueryBase.NotFoundError):
            pass

        cls.NotFoundError: Type["QueryBase.NotFoundError"] = NotFoundError

    def __init__(self, models:List[ModelType]) -> None:
        self.models = models

    def all(self) -> List[ModelType]:
        return self.models

    def get(self, id: int) -> ModelType:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()