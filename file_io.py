import glob
import csv
import json


def collect_csv_filenames(dir):
    """Collect all the *.csv files located in the test_data folder

    :return: list containing list of all filenames
    """
    filenames_list = glob.glob(dir)
    if len(filenames_list) == 0:
        print("No files found in specified directory.")
    return filenames_list


def read_csv(filename):
    """Read csv file and separate time and voltage into respective lists

    :param filename:
    :return:
    """
    csvfile = open(filename, "r")
    time = []
    voltage = []
    temp = csv.reader(csvfile, delimiter=",")
    for row in temp:
        time.append(row[0])
        voltage.append(row[1])

    return time, voltage


def write_json(filename, info):
    """Write data to .json file

    :param filename: Output filename
    :param info: Dictionary containing data to write
    :return:
    """
    json_filename = filename.replace('.csv', '.json')
    json_file = open(json_filename, "w")
    json.dump(info, json_file)
    json_file.close

    return
