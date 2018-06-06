def get_quadrant_number(x, y):
    qdr_number = 0

    if x == 0 or y == 0:
        raise ValueError
    elif x > 0 and y > 0:
        qdr_number = 1
    elif x < 0 and y > 0:
        qdr_number = 2
    elif x < 0 and y < 0:
        qdr_number = 3
    elif x > 0 and y < 0:
        qdr_number = 4
    return qdr_number
