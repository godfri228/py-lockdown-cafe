from .cafe import Cafe
from .errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    """
    Function to check if friends can go to cafe together.

    Args:
        friends (list): List of dictionaries with friend information
        cafe (Cafe): Cafe instance

    Returns:
        str: Message about whether friends can go to cafe
    """
    masks_needed = 0
    vaccination_issues = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccination_issues = True
        except NotWearingMaskError:
            masks_needed += 1

    if vaccination_issues:
        return "All friends should be vaccinated"

    if masks_needed > 0:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"
