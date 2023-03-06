from typing import Any, Optional

import graphene
from graphql import ResolveInfo

from models.places import PlaceModel
from schema.query import Place
from services.places import PlacesService


class CreatePlace(graphene.Mutation):
    """
    Функции для создания объекта любимого места.
    """

    class Arguments:
        latitude = graphene.Float()
        longitude = graphene.Float()
        description = graphene.String()

    result = graphene.Boolean()
    place = graphene.Field(Place)

    @staticmethod
    def mutate(
        parent: Optional[dict], info: ResolveInfo, **kwargs: dict[str, Any]
    ) -> "CreatePlace":
        """
        Обработка запроса для создания нового объекта.

        :param parent: Информация о родительском объекте (при наличии).
        :param info: Объект с метаинформацией и данных о контексте запроса.
        :param kwargs: Атрибуты со значениями для создания нового объекта.
        :return:
        """

        # pylint: disable=unused-argument

        # получение результата создания объекта
        place = PlacesService().create_place(
            PlaceModel(
                latitude=kwargs.get("latitude"),
                longitude=kwargs.get("longitude"),
                description=kwargs.get("description"),
            )
        )

        return CreatePlace(place=place, result=bool(place))


class DeletePlace(graphene.Mutation):
    """
    Функции для удаления объекта любимого места.
    """

    class Arguments:
        place_id = graphene.Int()

    result = graphene.Boolean()

    @staticmethod
    def mutate(
        parent: Optional[dict], info: ResolveInfo, place_id: int
    ) -> "DeletePlace":
        """
        Обработка запроса для удаления объекта по его идентификатору.

        :param parent: Информация о родительском объекте (при наличии).
        :param info: Объект с метаинформацией и данных о контексте запроса.
        :param place_id: Идентификатор объекта для удаления.
        :return:
        """

        # pylint: disable=unused-argument

        # получение результата удаления объекта
        result = PlacesService().delete_place(place_id)

        return DeletePlace(result=result)


class Mutation(graphene.ObjectType):
    """
    Общий тип для запроса изменения данных.
    """

    #: метод создания нового объекта любимого места
    create_place = CreatePlace.Field()

    #: метод удаления объекта любимого места
    delete_place = DeletePlace.Field()
