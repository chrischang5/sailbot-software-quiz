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


def test_bound_360_CW():
    assert bound_to_180(360) == 0


def test_bound_360_CCW():
    assert bound_to_180(-360) == 0


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_between_basic2():
    assert is_angle_between(0, 45, 90)


def test_between_basic3():
    assert is_angle_between(45, 90, 270)
