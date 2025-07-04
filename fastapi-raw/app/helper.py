from collections.abc import Sequence
from typing import TypeVar, Optional

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class Mapper:
    @staticmethod
    def to_dicts(rows: Sequence[tuple], field_sequence: list[str]) -> list[dict[str, any]]:
        """
        Convert a sequence of row tuples to a list of dictionaries using the provided field sequence.
        """
        return [Mapper.to_dict(row, field_sequence) for row in rows] if rows else []

    @staticmethod
    def to_dict(row: Optional[tuple], field_sequence: list[str]) -> Optional[dict[str, any]]:
        """
        Convert a single row tuple to a dictionary using the provided field sequence.
        """
        return {field_name: value for field_name, value in zip(field_sequence, row)} if row else None
    
    @staticmethod
    def to_schema(row: Optional[tuple], schema: type[T]) -> Optional[T]:
        """
        Convert a single row tuple to a Pydantic model.
        """
        return schema(**Mapper.to_dict(row, list(schema.model_fields.keys()))) if row else None
    
    @staticmethod
    def to_schemas(rows: Sequence[tuple], schema: type[T]) -> list[T]:
        """
        Convert a sequence of row tuples to a list of Pydantic models.
        """
        return [Mapper.to_schema(row, schema) for row in rows] if rows else []