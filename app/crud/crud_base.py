"""
    BASE CRUD FILE
"""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from motor.core import AgnosticDatabase
from odmantic import AIOEngine
from pydantic import BaseModel

from app.core.database import get_engine
from app.models.models_base import CustomBaseModel

ModelType = TypeVar("ModelType", bound=CustomBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    CRUD CLASS - BASE CRUD
    """

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.engine: AIOEngine = get_engine()

    def get(self, id_value: Any) -> Optional[ModelType]:
        """
        Method to retrieve a single object by id
        """
        return self.engine.find_one(self.model, self.model.id == id_value)

    def get_multi(self, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Method to retrieve multiple objects
        """
        offset = {"skip": skip, "limit": limit}
        return self.engine.find(self.model, **offset)

    def get_multi_without_limit(self) -> List[ModelType]:
        """
        Method to retrieve all objects without limit
        """
        return self.engine.find(self.model)

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Method to Create a new object
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        return self.engine.save(db_obj)

    # def update(
    #     self,
    #     db_session: AgnosticDatabase,
    #     *,
    #     db_obj: ModelType,
    #     obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    # ) -> ModelType:
    #     """
    #     Method to update an object
    #     """
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj

    def remove(self, *, id_value: str) -> ModelType:
        """
        Method to Remove an object
        """
        obj = self.model.get(id_value)
        if obj:
            self.engine.delete(obj)
        return obj
