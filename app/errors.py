class VaccineError(Exception):
    """parent class for problems with the vaccine"""


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Visitor's vaccine is outdated") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor needs a mask") -> None:
        super().__init__(message)
