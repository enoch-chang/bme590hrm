import glob
import csv
import json

def collect_csv_filenames():
    """Collect all the *.csv files located in the test_data folder

    :return: list containing list of all filenames
    """
    filenames_list = glob.glob('./test_data/*.csv')
    if len(filenames_list) == 0:
        print("No files found in specified directory.")
    return filenames_list

def read_csv(filename, time_unit="sec"):
    """Read csv file and separate time and voltage into respective lists

    :param filename:
    :param time_unit: users can input unit for timescale, if none specified, unit is assumed to be seconds
    :return:
    """
    csvfile = open(filename, "r")
    time = [ ]
    voltage = [ ]
    temp = csv.reader(csvfile, delimiter=",")
    if time_unit != "sec" and time_unit != "min":
        print("Warning: Input was neither 'sec' or 'min'. Data saved as seconds.")
    for row in temp:
        if time_unit == "min":
            time.append(floar(row[0])*60)
        else:
            time.append(float(row[0]))
        voltage.append(float(row[1]))
    return time, voltage

def write_json(filename, info, type = 'json'):
    """

    :param filename:
    :param type:
    :return:
    """
    json_filename = filename.replace('.csv','.json')
    json_file = open(json_filename, "w")
    json.dump(info, json_file)
    #json_file.write(info)
    json_file.close

    return