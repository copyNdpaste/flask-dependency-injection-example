import logging

from typing import List
from app.persistence.database import session
from app.persistence.models.station_model import Station


class UpdateStationRepository:
    @staticmethod
    def update_stations(stations: List[Station]):
        try:
            session.bulk_update_mappings(Station, stations)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f"update_stations e {e}")
