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
    FULL_ANGLE = 360
    # First, remove any "winding": where the angle spans the circle multiple times.
    
    angle_without_winding = angle % FULL_ANGLE 

    # Limit angle to [0, 360) range
    # For non-winded negative in the range [-359, 0)], we allow it to wind one time to put it within the range of [0, 360)
    if angle_without_winding < 0:
        angle_without_winding = angle + FULL_ANGLE

    # Split range [0, 360) into two ranges [0, 180) and [180, 360):

    # Map angles [0, 180) to [0, 180)
    if 0 <= angle_without_winding and angle_without_winding < 180:
        return angle_without_winding
    
    # Map angles [180, 360) to [-180. 0) 
    if 180 <= angle_without_winding and angle_without_winding < FULL_ANGLE:
        return angle_without_winding - FULL_ANGLE


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
