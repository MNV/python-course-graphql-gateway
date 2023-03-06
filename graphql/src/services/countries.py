from typing import Optional

from clients.countries import CountriesClient
from models.countries import CountryModel


class CountriesService:
    """
    Сервис для работы с данными о странах.
    """

    def get_countries(self, alpha2codes: list[str]) -> Optional[list[CountryModel]]:
        """
        Получение списка стран.

        :param alpha2codes: Список ISO Alpha2-кодов стран
        :return:
        """

        codes = {code.lower() for code in alpha2codes if len(code) == 2}


        return CountriesClient().get_list_by_codes(codes)
