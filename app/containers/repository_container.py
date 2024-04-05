from dependency_injector import containers, providers

from app.persistence.repositories.get_station_repository import GetStationRepository
from app.persistence.repositories.update_station_repository import (
    UpdateStationRepository,
)


class RepositoryContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.services.update_station_service",
        ]
    )

    get_station_repository = providers.Singleton(GetStationRepository)
    update_station_repository = providers.Singleton(UpdateStationRepository)
