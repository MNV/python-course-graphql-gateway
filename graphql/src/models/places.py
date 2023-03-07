from typing import Optional

from pydantic import BaseModel, Field

from models.mixins import TimeStampMixin


class PlaceModel(TimeStampMixin, BaseModel):
    """
    Модель для описания места.
    """

    id: Optional[int] = Field(title="Идентификатор")
    latitude: float = Field(title="Широта")
    longitude: float = Field(title="Долгота")
    description: str = Field(title="Описание")
    country: Optional[str] = Field(title="ISO Alpha2-код страны")
    city: Optional[str] = Field(title="Название города")
    locality: Optional[str] = Field(title="Местонахождение")


class PlaceSummary(BaseModel):
    """
    Схема данных для обновления любимого места.
    """

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = Field(None, min_length=3, max_length=255)
