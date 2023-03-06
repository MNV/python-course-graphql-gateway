"""
Базовые функции для клиентов внешних сервисов.
"""

from abc import ABC, abstractmethod
from http import HTTPStatus
from http.client import HTTPException
from json import JSONDecodeError
from typing import Optional

import httpx


class BaseClient(ABC):
    """
    Базовый класс, реализующий интерфейс для клиентов.
    """

    GET = "get"
    POST = "post"
    PATCH = "patch"
    DELETE = "delete"

    @property
    @abstractmethod
    def base_url(self) -> str:
        """
        Получение базового URL для запросов.

        :return:
        """

    def _request(
        self, method: str, url: str, body: Optional[dict] = None
    ) -> Optional[dict]:
        """
        Формирование и выполнение запроса.

        :param method: Метод HTTP-запроса
        :param url: URL для выполнения запроса.
        :param body: Тело запроса.
        :return:
        """

        with httpx.Client() as client:
            # формирование запроса
            request = client.build_request(
                method,
                url,
                json=body,
            )
            # получение ответа
            response = client.send(request)
            # проверка статус-кода ответа от сервера
            if response.status_code in (
                HTTPStatus.OK,
                HTTPStatus.CREATED,
                HTTPStatus.ACCEPTED,
                HTTPStatus.NO_CONTENT,
            ):
                try:
                    # преобразование ответа из JSON в словарь
                    result = response.json()
                except JSONDecodeError:
                    result = None

                return result

            raise HTTPException(
                f"Сервер не смог успешно обработать запрос: {response.text}"
            )
