from typing import Optional

from clients.places import PlacesClient
from models.places import PlaceModel


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение объекта любимого места по его идентификатору.

        :return:
        """

        return PlacesClient().get_place(place_id)

    def get_places(self) -> Optional[list[PlaceModel]]:
        """
        Получение списка любимых мест.

        :return:
        """

        return PlacesClient().get_list()

    def create_place(self, place: PlaceModel) -> Optional[PlaceModel]:
        """
        Создание нового объекта любимого места.

        :param place: Объект любимого места для создания.
        :return:
        """

        return PlacesClient().create_place(place)

    def delete_place(self, place_id: int) -> bool:
        """
        Удаление объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        return PlacesClient().delete_place(place_id)
