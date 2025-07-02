import datetime
from .errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from typing import Dict


class Cafe:
    """Cafe class for managing visitor access during pandemic."""

    def __init__(self, name: str) -> None:
        """Initialize cafe with a name."""
        self.name = name

    def visit_cafe(self, visitor: Dict) -> str:
        """
        Check if visitor can enter the cafe.

        Returns welcome message if visitor passes all checks.
        Raises appropriate exceptions if visitor fails checks.
        """
        # Check if visitor is vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor must be vaccinated to enter")

        # Check if vaccine is not expired
        vaccine_expiration = visitor["vaccine"]["expiration_date"]
        current_date = datetime.date.today()

        if vaccine_expiration < current_date:
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask to enter")

        return f"Welcome to {self.name}"
