from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


# example given in spec
def test_bound_pos_angle_in_upper_bound():
    assert bound_to_180(135) == 135

# example given in spec


def test_bound_pos_angle_in_lower_bound():
    assert bound_to_180(200) == -160


def test_bound_pos_angle_in_upper_bound_winded():
    assert bound_to_180(360 + 360 + 10) == 10


def test_bound_pos_angle_in_lower_bound_winded():
    assert bound_to_180(360 + 360 + 360 + 190) == -170


def test_bound_negative_angle_in_upper_bound():
    assert bound_to_180(-200) == 160


def test_bound_negative_angle_in_lower_bound():
    assert bound_to_180(-160) == -160


def test_bound_negative_angle_in_upper_bound_winded():
    assert bound_to_180(-360 - 360 - 360 - 190) == 170


def test_bound_negative_angle_in_lower_bound_winded():
    assert bound_to_180(-360 - 360 - 360 - 170) == -170

# Edge cases


def test_bound_180_not_exclusive():
    assert bound_to_180(180) == -180


def test_bound_negative_180_inclusive():
    assert bound_to_180(-180) == -180


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_180_not_exclusive_winded():
    assert bound_to_180(360 + 180) == -180


def test_bound_negative_180_inclusive_winded():
    assert bound_to_180(360 + -180) == -180


def test_bound_negative_almost_180():
    assert bound_to_180(-179.9) == -179.9


def test_bound_negative_just_over_180():
    assert bound_to_180(-180.1) == 179.9


def test_bound_positive_almost_180():
    assert bound_to_180(179.9) == 179.9


def test_bound_positive_just_over_180():
    assert bound_to_180(180.1) == -179.9


def test_bound_pos_360():
    assert bound_to_180(360) == 0


def test_bound_negative_360():
    assert bound_to_180(-360) == 0


def test_bound_negative_almost_360():
    assert bound_to_180(-359) == 1


def test_bound_positive_almost_360():
    assert bound_to_180(359) == -1


def test_bound_positive_just_more_than_360():
    assert bound_to_180(361) == 1


def test_bound_negative_just_more_than_360():
    assert bound_to_180(-361) == -1


""" Tests for is_angle_between() """


def test_between_given_test():
    assert is_angle_between(0, 1, 2)


def test_between_given_ex1():
    assert is_angle_between(0, 45, 90)


def test_between_given_ex2():
    assert ~is_angle_between(45, 90, 270)


def test_between_acute_angle_pass():
    assert is_angle_between(0, 30, 60)


def test_between_acute_angle_fail():
    assert ~is_angle_between(0, 90, 60)


def test_between_acute_winded_pass():
    assert is_angle_between(360 + 0, -360 + 30, 360 + 360 + 60)


def test_between_acute_winded_fail():
    assert ~is_angle_between(-360 + 0, 360 + 90, 360 + 60)


def test_between_right_angle_pass():
    assert is_angle_between(180, 200, 270)


def test_between_right_angle_fail():
    assert ~is_angle_between(-270, -260, 0)


def test_between_right_winded_pass():
    assert is_angle_between(360 + 180, 200, -360 + 270)


def test_between_right_winded_fail():
    assert ~is_angle_between(-360 + -180, 360 + 45, -360 + -270)


def test_between_obtuse_pass():
    assert is_angle_between(0, 120, 130)


def test_between_obtuse_fail():
    assert ~is_angle_between(60, 260, 230)


def test_between_obtuse_winded_pass():
    assert is_angle_between(-360 + 0, 360 + 120, 360 + 360 + 130)


def test_between_obtuse_winded_fail():
    assert ~is_angle_between(-360 + 0, -360 + -90, 360 + 360 + 130)


def test_between_straight_angle1():
    assert is_angle_between(0, 90, 180)


def test_between_straight_angle2():
    assert is_angle_between(0, -90, 180)


def test_between_straight_angle3():
    assert is_angle_between(-180, 100, 0)


def test_between_straight_winded_angle():
    assert is_angle_between(-360 + -180, 10, 360 + 0)


def test_between_complete_angle_pass():
    assert is_angle_between(0, 0, 360)


def test_between_complete_angle_fail():
    assert ~is_angle_between(0, 10, 360)


def test_between_complete_winded_pass():
    assert is_angle_between(0, -360, 360)


def test_between_complete_winded_fail():
    assert ~is_angle_between(0, 360 + 10, 360)


def test_between_reflex_angle_pass():
    assert is_angle_between(0, -55, 270)


def test_between_reflex_angle_fail():
    assert ~is_angle_between(0, 55, 270)
