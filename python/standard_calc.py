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

    LOWER_BOUND = -180
    UPPER_BOUND = 180
    FULL_ANGLE = 360

    if LOWER_BOUND <= angle and angle < UPPER_BOUND:
        return angle

    print(angle)
    # remove any "winding" first: where the angle spans the circle multiple times.
    angle_without_winding = angle % FULL_ANGLE
    print(angle_without_winding)

    # Cases: Angle is over upper bound or angle is under lower bound

    if angle_without_winding > UPPER_BOUND:
        # We wandered into the 0 to -180 region
        return LOWER_BOUND + (angle_without_winding % UPPER_BOUND)
    elif angle_without_winding < LOWER_BOUND:
        # we wandered into the 0 to 180 region
        return UPPER_BOUND - (angle_without_winding % LOWER_BOUND)
    else:
        # otherwise
        return angle_without_winding


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
    return first_angle <= middle_angle and middle_angle <= second_angle
