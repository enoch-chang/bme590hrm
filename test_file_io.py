import file_io
import process_ecg_data
import pytest


def test_collect_csv_filenames():
    dir = './test_data/test_data1*.csv'
    filenames_list = file_io.collect_csv_filenames(dir)
    print(filenames_list)
    assert filenames_list == ['./test_data/test_data1.csv',
                              './test_data/test_data10.csv',
                              './test_data/test_data11.csv',
                              './test_data/test_data12.csv',
                              './test_data/test_data13.csv',
                              './test_data/test_data14.csv',
                              './test_data/test_data15.csv',
                              './test_data/test_data16.csv',
                              './test_data/test_data17.csv',
                              './test_data/test_data18.csv',
                              './test_data/test_data19.csv']


def test_read_csv():
    filename = './test_data/test_data1.csv'
    time, voltage = file_io.read_csv(filename)
    assert float(time[0]) == 0
    assert float(voltage[0]) == -0.145
    assert float(time[1]) == 0.003
    assert float(voltage[1]) == -0.145

    filename = './test_data/test_data2.csv'
    time, voltage = file_io.read_csv(filename)
    assert float(time[0]) == 0
    assert float(voltage[0]) == -0.345
    assert float(time[1]) == 0.003
    assert float(voltage[1]) == -0.345


def test_write_json():
    import json
    output_1 = {"Favorite Food": "Cheese",
                "Favorite Movie": "Back to the Future",
                "Favorite Number": 6}
    filename = "Test Output.csv"
    file_io.write_json(filename, output_1)

    read_file = json.load(open('Test Output.json'))
    assert read_file == {"Favorite Food": "Cheese",
                         "Favorite Movie": "Back to the Future",
                         "Favorite Number": 6}
