import Lab2 as lab

def test_find_min_max():
    correct = [39.9, 78]
    float_list = [45.6, 78, 39.9]
    result = lab.find_min_max(float_list)
    assert (result == correct)

def test_calc_average():
    float_list = [60, 62]
    correct = 61
    result = lab.calc_average(float_list)
    assert(result == correct)

def test_median_temperature():
    float_list = [45, 92, 100]
    correct = 92
    result = lab.calc_median_temperature(float_list)
    assert (result == correct)
