import logging
from typing import List

from app.containers.repository_container import RepositoryContainer
from app.persistence.models.station_model import Station
from app.persistence.repositories.update_station_repository import (
    UpdateStationRepository,
)
from app.persistence.repositories.get_station_repository import GetStationRepository

from dependency_injector.wiring import inject, Provide


class UpdateStationService:
    @inject
    def __init__(
        self,
        get_station_repository: GetStationRepository = Provide[
            RepositoryContainer.get_station_repository
        ],
        update_station_repository: UpdateStationRepository = Provide[
            RepositoryContainer.update_station_repository
        ],
    ) -> None:
        self.get_station_repository = get_station_repository
        self.update_station_repository = update_station_repository

    def update(self):
        stations = self.get_station_repository.get_stations()
        self.update_stations(stations=stations)

    def update_stations(self, stations: List[Station]):
        stations = []
        for station in stations:
            id = station.id
            detail_address = "blah-blah-blah"
            stations.append(dict(id=id, detail_address=detail_address))
            logging.debug(
                f"update_stations id : {id} detail_address : {detail_address}"
            )
        self.update_station_repository.update_stations(stations=stations)
