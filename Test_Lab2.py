import temp


def test_find_min_max():
    # Test with a list of temperatures
    assert temp.find_min_max([5.0, 10.0, 2.0, 8.0, 3.0]) == [2.0, 10.0]

    # Test with an empty list
    assert temp.find_min_max([]) == [None, None]


def test_calc_average():
    # Test with a list of temperatures
    assert temp.calc_avg(5.0, 10.0, 2.0, 8.0, 3.0) == 5.6

    # Test with another list of temperatures
    assert temp.calc_avg(15.0, 20.0, 10.0, 25.0, 30.0) == 20.0


def test_calc_median_temperature():
    # Test with an odd number of temperatures
    assert temp.calc_median_temperature([5.0, 10.0, 2.0, 8.0, 3.0]) == 5.0

    # Test with an even number of temperatures
    assert temp.calc_median_temperature([15.0, 20.0, 10.0, 25.0]) == 17.5


if __name__ == "__main__":
    test_find_min_max()
    test_calc_average()
    test_calc_median_temperature()
