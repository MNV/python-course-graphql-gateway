from pydantic import BaseModel, BaseSettings, Field


class Project(BaseModel):
    """
    Описание проекта.
    """

    #: название проекта
    title: str = "GraphQL API Gateway"
    #: описание проекта
    description: str = "Шлюз для взаимодействия с микросервисами."
    #: версия релиза
    release_version: str = Field(default="0.1.0")


class ServiceDetails(BaseModel):
    """
    Конфигурация микросервиса.
    """

    #: базовый адрес сервиса
    base_url: str


class ServiceConfig(BaseModel):
    """
    Микросервисы для конфигурирования.
    """

    favorite_places: ServiceDetails
    countries_informer: ServiceDetails


class Settings(BaseSettings):
    """
    Настройки проекта.
    """

    #: режим отладки
    debug: bool = Field(default=False)
    #: описание проекта
    project: Project
    #: базовый адрес приложения
    base_url: str = Field(default="http://0.0.0.0:8000")
    #: конфигурация для взаимодействия с микросервисами
    service: ServiceConfig

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"


# инициализация настроек приложения
settings = Settings()
