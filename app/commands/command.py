from flask.cli import AppGroup
from app.services.update_station_service import UpdateStationService

staiton_cli = AppGroup("station")


@staiton_cli.command("update")
def update_station():
    UpdateStationService().update()
