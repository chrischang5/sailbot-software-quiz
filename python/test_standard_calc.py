from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0

def test_bound_basic2():
    assert bound_to_180(135) == 135

def test_bound_basic3():
    assert bound_to_180(200) == -160

def test_bound_basic4():
    assert bound_to_180(360 + 360 + 10) == 10

def test_bound_basic5():
    assert bound_to_180(-200) == 160

def test_bound_basic6():
    assert bound_to_180(360 + 360 + 360 + 190) == -170

def test_bound_basic9():
    assert bound_to_180(-360 - 360 - 360 - 190) == 170

def test_bound_basic10():
    assert bound_to_180(-360 - 360 - 360 - 170) == -170

""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)

def test_between_basic2():
    assert is_angle_between(0, 45, 90)

def test_between_basic3():
    assert is_angle_between(45, 90, 270)