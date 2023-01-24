from dataclasses import dataclass
from typing import List, TypeVar, Generic, Type, Any


@dataclass
class ModelBase:
    id: int


ModelType = TypeVar("ModelType", bound=ModelBase)


class QueryBase(Generic[ModelType]):
    class NotFoundError(Exception):
        pass

    def __init_subclass__(cls) -> None:
        class MyNotFoundError(QueryBase.NotFoundError):
            pass
        
        cls.NotFoundError = MyNotFoundError #type: ignore

    def __init__(self, models:List[ModelType]) -> None:
        self.models = models

    def all(self) -> List[ModelType]:
        return self.models

    def get(self, id: int) -> ModelType:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()