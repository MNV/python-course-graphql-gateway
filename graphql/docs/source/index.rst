GraphQL API Gateway
===================

GraphQL API шлюз для взаимодействия с микросервисами.

Зависимости
===========
Установите соответствующее программное обеспечение:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (опционально).


Установка
=========
Клонируйте репозиторий на свой компьютер:

.. code-block::console
    git clone https://github.com/mnv/python-course-graphql-gateway

1. Для настройки приложения скопируйте `.env.sample` в файл `.env`:
.. code-block::console
    cp .env.sample .env

Этот файл содержит переменные окружения, значения которых будут общими для всего приложения.
Файл-образец (`.env.sample`) содержит набор переменных со значениями по умолчанию.
Поэтому он может быть настроен в зависимости от окружения.

2. Соберите контейнер с помощью Docker Compose:
.. code-block::console
    docker compose build

Эта команда должна быть запущена из корневого каталога, в котором находится `Dockerfile`.
Вам также необходимо собрать docker-контейнер заново в случае, если вы обновили `requirements.txt`.

3. Чтобы запустить проект внутри контейнера Docker:
.. code-block::console
    docker compose up

4. Выполните миграции внутри БД:

   Выполните миграции БД любимых мест:
    .. code-block::console
    docker compose run favorite-places-app alembic upgrade head
   Выполните миграции БД справочника по странам:
    .. code-block::console
    docker compose run countries-informer-app bash

   Запуск внутри контейнера:
    .. code-block::console
    ./manage.py migrate

Когда контейнеры подняты, сервер запускается по адресу [http://0.0.0.0:8000/graphql](http://0.0.0.0:8000/graphql). Вы можете открыть его в браузере.


Использование
=============
Пример запроса для запроса списка любимых мест с пагинацией:
.. code-block::graphql
query {
  places (page: 1, size: 2) {
    latitude
    longitude
    description
    city
    locality
  }
}

Пример запроса для получения списка любимых мест с информацией о странах:
.. code-block::graphql
query {
  places {
    latitude
    longitude
    description
    city
    locality
    country {
      name
      capital
      alpha2code
      alpha3code
      capital
      region
      subregion
      population
      latitude
      longitude
      demonym
      area
      numericCode
      flag
      currencies
      languages
    }
  }
}

Пример запроса для получения конкретного любимого места:
.. code-block::graphql
{
  place(placeId:1) {
    id
    latitude
    longitude
    description
    city
    locality
  }
}

Пример запроса для создания нового любимого места:
.. code-block::graphql
mutation {
  createPlace (
    latitude: 25.20485,
    longitude: 55.27078,
    description: "Nice food."
  ) {
    place {
      id
      latitude
      longitude
      description
      city
      locality
    }
    result
  }
}

Пример запроса для удаления определенного любимого места:
.. code-block::graphql
mutation {
  deletePlace(placeId: 1) {
    result
  }
}

Пример запроса для обновления избранного места:
.. code-block::graphql
mutation {
  updatePlace (
  	placeId: 1
    latitude: 25,
    longitude: 55,
    description: "Awesome!"
  ) {
    place {
      id
      latitude
      longitude
      description
      city
      locality
    }
    result
  }
}

Автоматизация
=============
Проект содержит специальный `Makefile`, который предоставляет ярлыки для набора команд:

1. Создайте контейнер Docker:
.. code-block::console
    make build

2. Сгенерируйте документацию Sphinx:
.. code-block::console
    make docs-html

3. Автоформатирование исходного кода:
.. code-block::console
    make format

4. Статический анализ (линтеры):
.. code-block::console
    make lint

5. Автотесты:
.. code-block::console
    make test

6. Запуск автоформата, линтеров и тестов одной командой:
.. code-block::console
    make all


Документация
=============

Проект интегрирован с движком документации [Sphinx](https://www.sphinx-doc.org/en/master/).
Он позволяет создавать документацию из исходного кода.
Таким образом, исходный код должен содержать документацию в формате [reStructuredText](https://docutils.sourceforge.io/rst.html).

Для создания HTML документации выполните эту команду из каталога исходников, где находится `Makefile`:
.. code-block::console
make docs-html


После генерации документацию можно открыть из файла `docs/build/html/index.html`.

Модели
------

.. automodule:: models.places
    :members:

.. automodule:: models.countries
    :members:

Сервисы
-------

.. automodule:: services.places
    :members:

.. automodule:: services.countries
    :members:

Клиенты
------
.. automodule:: clients.places
    :members:

.. automodule:: clients.countries
    :members:

Схема
-----

.. automodule:: schema
    :members:

Контекст
-------

.. automodule:: context
    :members:

Data loaders
------------

.. automodule:: dataloaders
    :members:

Настройки
---------

.. automodule:: settings
    :members:



