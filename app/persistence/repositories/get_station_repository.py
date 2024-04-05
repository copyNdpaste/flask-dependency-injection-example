from app.persistence.database import session
from app.persistence.models.station_model import Station


class GetStationRepository:
    @staticmethod
    def get_stations():
        return session.query(Station).all()
