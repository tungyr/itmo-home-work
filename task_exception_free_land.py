def get_free_land(square_rate, dimens):
    if square_rate[0] == 0:
        raise ValueError('Не задана площадь участка')
    if dimens[1] == 0:
        raise ValueError('Не задана площадь грядки')

    area_sqre = square_rate[0] * 100
    rate = square_rate[1]
    a = (square_rate[0] * 10) / int(rate[0])
    b = (square_rate[0] * 10) / int(rate[2])

    if a < dimens[0] or b < dimens[1]:
        raise ValueError('Размер грядки больше размера участка')

    bed_sqre = dimens[0] * dimens[1]
    bed_qtty = area_sqre // bed_sqre
    rest_sqre = area_sqre - (bed_qtty * bed_sqre)
    return rest_sqre

