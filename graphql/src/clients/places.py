from http.client import HTTPException
from typing import Optional
from urllib.parse import urljoin

from clients.base.base import BaseClient
from models.places import PlaceModel, PlaceSummary
from settings import settings


class PlacesClient(BaseClient):
    """
    Реализация функций для получения информации о любимых местах.
    """

    @property
    def base_url(self) -> str:
        return settings.service.favorite_places.base_url

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        endpoint = f"http://favorite-places-app:8000/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)

        if response := self._request(self.GET, url):
            if place_data := response.get("data"):
                return self.__build_model(place_data)

        return None

    def get_list(
        self, page: Optional[int], size: Optional[int]
    ) -> Optional[list[PlaceModel]]:
        """
        Получение списка любимых мест.
        :param page: Номер страницы.
        :para, size: Размер страницы.
        :return:
        """
        if not page:
            page = 1
        if not size:
            size = 50

        endpoint = "http://favorite-places-app:8000/api/v1/places"
        url = urljoin(self.base_url, f"{endpoint}?page={page}&size={size}")
        if response := self._request(self.GET, url):
            return [self.__build_model(place) for place in response.get("items", [])]

        return None

    def create_place(self, place: PlaceModel) -> Optional[PlaceModel]:
        """
        Создание нового объекта любимого места.

        :param place: Объект любимого места для создания.
        :return:
        """

        endpoint = "http://favorite-places-app:8000/api/v1/places"
        url = urljoin(self.base_url, endpoint)
        if response := self._request(self.POST, url, body=place.dict()):
            if place_data := response.get("data"):
                return self.__build_model(place_data)

        return None

    def delete_place(self, place_id: int) -> bool:
        """
        Удаление объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        endpoint = f"http://favorite-places-app:8000/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)
        result = True
        try:
            self._request(self.DELETE, url)
        except HTTPException:
            result = False

        return result

    def update_place(self, place_id: int, place: PlaceSummary) -> Optional[PlaceModel]:
        """
        Создание нового объекта любимого места.

        :param place: Объект любимого места для создания.
        :return:
        """
        endpoint = f"http://favorite-places-app:8000/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)
        if response := self._request(self.PATCH, url, body=place.dict()):
            if place_data := response.get("data"):
                return self.__build_model(place_data)

        return None

    @staticmethod
    def __build_model(data: dict) -> PlaceModel:
        """
        Формирование модели для DTO-объекта любимого места на основе полученных данных.

        :param data: Данные для создания DTO
        :return:
        """

        return PlaceModel(
            id=data.get("id"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            description=data.get("description"),
            country=data.get("country"),
            city=data.get("city"),
            locality=data.get("locality"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
