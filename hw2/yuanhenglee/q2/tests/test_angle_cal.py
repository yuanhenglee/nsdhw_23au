from angle_cal import calculate_angle
import math

rel_tol = 1e-5

def test_zero_length():
    x1, y1, x2, y2 = 0, 0, 0, 0

    angle = calculate_angle(x1, y1, x2, y2)

    assert math.isnan(angle)

def test_zero_angle():
    x1, y1, x2, y2 = 1, 0, 2, 0

    angle = calculate_angle(x1, y1, x2, y2)

    assert math.isclose(angle, 0, rel_tol=rel_tol)

def test_90_angle():
    x1, y1, x2, y2 = 1, 0, 0, 1

    angle = calculate_angle(x1, y1, x2, y2)

    assert math.isclose(angle, math.pi/2, rel_tol=rel_tol)

def test_arbitrary_angle():
    x1, y1, x2, y2 = 1, 1, 2, 3

    angle = calculate_angle(x1, y1, x2, y2)

    answer = math.atan2(y2, x2) - math.atan2(y1, x1)
    if answer < 0:
        answer += 2*math.pi

    assert math.isclose(angle, answer, rel_tol=rel_tol)


    

