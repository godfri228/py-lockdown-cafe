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
        if "vaccine" not in visitor or not isinstance(visitor["vaccine"], dict):
            raise NotVaccinatedError("Visitor must be vaccinated to enter")

        vaccine_data = visitor["vaccine"]

        # Check if expiration_date exists and is a valid date
        expiration_date = vaccine_data.get("expiration_date")
        if not isinstance(expiration_date, datetime.date):
            raise OutdatedVaccineError(
                "Invalid or missing expiration date"
            )

        # Check if vaccine is not expired
        current_date = datetime.date.today()
        if expiration_date < current_date:
            raise OutdatedVaccineError("Visitor's vaccine is expired")

        # Check if visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Visitor must wear a mask to enter")

        return f"Welcome to {self.name}"
