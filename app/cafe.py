import datetime

from app.errors import (OutdatedVaccineError,
                        NotVaccinatedError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor.keys():
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError("Vaccine is expired")
        else:
            raise NotVaccinatedError("Visitor has no vaccine")

        if (
            visitor["wearing_a_mask"] is False
            or visitor["wearing_a_mask"] is None
            or "wearing_a_mask" not in visitor.keys()
        ):
            raise NotWearingMaskError("A mask is required")

        return f"Welcome to {self.name}"
