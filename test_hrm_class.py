import file_io
import process_ecg_data
import pytest


def main():

    test_1 = process_ecg_data.HeartRateMonitor()

    # Testing is_float
    output_1 = test_1.is_float("4")
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

    test_1.time = ["6", 7, 8, 9]
    output_3 = test_1.process_input()
    assert output_3 is True

    with pytest.raises(TypeError):
        test_1.time = ["abc", 5, 7, 1]
        test_1.process_input()

    with pytest.raises(TypeError):
        test_1.voltage = ["g", 5.2, 8.7, 1.0]
        test_1.process_input()

    test_1.time = ["6", 7, "bad data", 9]
    output_4 = test_1.process_input()
    assert output_4 is True

    with pytest.raises(InputError):
        test_1.voltage = [2.3, 5.2, 8.7, 1.0]
        test_1.time = [6.7, 2.6, 2.3]
        test_1.process_input()

    # Testing mean_hr_bpm

    test_1.time = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    output_5 = test_1.mean_hr_bpm(130)
    assert output_5 == 97.5

    # Testing voltage_extremes

    test_1.voltage = [-5.0, -2.0, 0.0, 1.0, 7.0]
    output_6 = test_1.voltage_extremes()
    assert output_6[0] == -5.0
    assert output_6[1] == 7.0

    # Testing duration

    output_7 = test_1.duration()
    assert output_7 == 80

    # Testing num_beats

    dir = './test_data/test_data1.csv'
    filename_ref = file_io.collect_csv_filenames(dir)
    time, voltage_ref = file_io.read_csv(filename_ref)

    time, voltage = file_io.read_csv(filename_ref)
    test_2 = process_ecg_data.HeartRateMonitor(time, voltage,
                                               voltage_ref,
                                               time_unit,
                                               filename)

    file_io.write_json(filename, hrm.output())

    output_8 = test_2.num_beats()
    assert output_8 == 37

    # Testing beats

    output_9 = test_2.beats()
    assert output_9 == [1.9191893913559595, 7.2761323220119625,
                        8.6565459574399846, 7.6482131374399929,
                        7.5730977174399916, 6.7617974674399912,
                        7.1781172174399872, 8.2816793474399812,
                        7.4653328274399886, 8.0886570074400019,
                        7.6762159774399912, 7.6119475074399778,
                        7.2119020174399697, 6.909086467439983,
                        8.1515838574399719, 7.8342257474399748,
                        6.8379951274399913, 7.5429494774399979,
                        7.9018576574399813, 7.0560024974399758,
                        9.2008327874399853, 7.583319557439987,
                        8.4643853974399779, 7.7525408974399825,
                        7.3281724674399902, 7.980235497439983,
                        9.8376041674399684, 7.2330221074399823,
                        7.3661933274399978, 8.096641197440011,
                        7.0555914174400272, 6.4831490274400432,
                        7.407749637440034, 1.6182016374400188,
                        9.8078005874400063, 1.4386710174400004,
                        7.2698867174400004]

if __name__ == "__main__":
    main()
