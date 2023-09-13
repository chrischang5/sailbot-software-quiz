COMPLETE_ANGLE = 360


def normalize(angle):
    """
    limit angle to [0, 360) range.
    """

    # First, remove any "winding": where the angle spans the circle multiple times.
    normalized_angle = angle % COMPLETE_ANGLE

    if normalized_angle >= 0:
        return normalized_angle

    # For non-winded negative in the range [-359, 0)], we allow it to wind one time to put it within the range of [0, 360)
    return normalized_angle + COMPLETE_ANGLE


def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    # Limit angle to [0, 360) range
    angle_without_winding = normalize(angle)

    # Split range [0, 360) into two ranges: [0, 180) and [180, 360).

    # Map angles [0, 180) to [0, 180)
    if 0 <= angle_without_winding and angle_without_winding < 180:
        return angle_without_winding

    # Map angles [180, 360) to [-180. 0)
    if 180 <= angle_without_winding and angle_without_winding < COMPLETE_ANGLE:
        return angle_without_winding - COMPLETE_ANGLE


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    def non_reflex_angle(angle1, angle2):
        return min(COMPLETE_ANGLE - abs(angle1 - angle2), abs(
            angle1 - angle2))

    # Limit angles to range [0, 360)
    normalized_first_angle = normalize(first_angle)
    normalized_middle_angle = normalize(middle_angle)
    normalized_second_angle = normalize(second_angle)

    # For the middle angle to be "between" the first and second angles, 
    # the middle angle needs to split the non-reflex angle into two sections.

    # The sum of the two split sections should equal
    # the non-reflex angle of the first and second angles.
    first_second_non_reflex_angle = non_reflex_angle(
        normalized_first_angle, normalized_second_angle)

    middle_first_non_reflex_angle = non_reflex_angle(
        normalized_first_angle, normalized_middle_angle)
    middle_second_non_reflex_angle = non_reflex_angle(
        normalized_middle_angle, normalized_second_angle)

    return (middle_first_non_reflex_angle + middle_second_non_reflex_angle) == first_second_non_reflex_angle
