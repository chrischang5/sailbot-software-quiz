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


def test_between_winded_first_angle():
    assert is_angle_between(360 + 0, 45, 90)


def test_between_winded_middle_angle():
    assert is_angle_between(0, 360 + 45, 90)


def test_between_winded_second_angle():
    assert is_angle_between(0, 45, 360 + 90)


def test_between_winded_first_second_angle():
    assert is_angle_between(0 + 360, 45, 360 + 90)


def test_between_winded_middle_second_angle():
    assert is_angle_between(0, 360 + 45, 360 + 90)


def test_between_winded_first_middle_angle():
    assert is_angle_between(360 + 0, 360 + 45, 90)


def test_between_all_winded():
    assert is_angle_between(360 + 0, 360 + 45, 360 + 90)


def test_between_all_same():
    assert is_angle_between(90, 90, 90)


def test_between_all_negative():
    assert is_angle_between(-20, -10, -6)


def test_between_negative_first_angle():
    assert is_angle_between(-90, 0, 90)


def test_between_negative_second_angle():
    assert is_angle_between(90, 0, -90)


def test_between_negative_middle_angle():
    assert is_angle_between(-2, -1, 2)


def test_between_negative_winded1():
    assert is_angle_between(-360 + 0, 45, 90)


def test_between_winded_different_ways():
    assert is_angle_between(-360 + -20, 360 + -10, 360 + -6)
