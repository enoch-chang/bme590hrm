import file_io
import process_ecg_data
import pytest
import math


def main():

    test_1 = process_ecg_data.HeartRateMonitor()

    # Testing is_float
    output_1 = test_1.is_float("abc")
    assert output_1 is False

    output_2 = test_1.is_float(4)
    assert output_2 is True

    # Testing process_input

    with pytest.raises(ValueError):
        test_1.voltage = [0.1, -0.2, math.sqrt(2),
                          math.sqrt(-5), -(math.sqrt(8))]
        test_1.process_input()

    with pytest.raises(ValueError):
        test_1.time = [6, 7, math.sqrt(-2)]
        test_1.process_input()

    test_1.voltage = []
    test_1.time = []
    test_1.time_input = ["6", 7, 8, 9]
    test_1.voltage_input = [5, 7, 3, 4]
    output_3 = test_1.process_input()
    assert output_3 is True

    with pytest.raises(TypeError):
        test_1.time_input = tuple("abc", 5, 7, 1)
        test_1.process_input()

    with pytest.raises(TypeError):
        test_1.voltage_input = tuple("g", 5.2, 8.7, 1.0)
        test_1.process_input()

    test_1.time_input = ["6", 7, "bad data", 9]
    output_4 = test_1.process_input()
    assert output_4 is True

    test_1.voltage = []
    test_1.time = []
    test_1.voltage_input = [2.3, 5.2, 8.7, 1.0]
    test_1.time_input = [6.7, 2.6, 2.3]
    assert test_1.process_input() is False

    # Testing mean_hr_bpm

    test_1.voltage = []
    test_1.time = []
    test_1.time_input = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    test_1.voltage_input = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_1.process_input()
    output_5 = test_1.mean_hr_bpm(130)
    assert output_5 == 97.5

    # Testing voltage_extremes

    test_1.voltage = []
    test_1.time = []
    test_1.voltage_input = [-5.0, -2.0, 0.0, 1.0, 7.0]
    test_1.time_input = [1, 2, 3, 4, 5]
    test_1.process_input()
    output_6 = test_1.voltage_extremes()
    assert output_6[0] == -5.0
    assert output_6[1] == 7.0

    # Testing duration

    test_1.time = []
    test_1.time_input = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    test_1.process_input()
    output_7 = test_1.duration()
    assert output_7 == 80

    # Testing num_beats

    dir = "./test_data/test_data1.csv"
    time, voltage_ref = file_io.read_csv("./test_data/test_data1.csv")

    time, voltage = file_io.read_csv("./test_data/test_data1.csv")
    test_2 = process_ecg_data.HeartRateMonitor(time, voltage,
                                               voltage_ref,
                                               "sec",
                                               "./test_data/test_data1.csv")
    output_8 = test_2.num_beats()
    assert output_8 == 37

    # Testing beats

    output_9 = test_2.beats()
    assert round(output_9[0], 5) == [1.91919]
    assert round(output_9[1], 5) == [7.27613]

if __name__ == "__main__":
    main()
