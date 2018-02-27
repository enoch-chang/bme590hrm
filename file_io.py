import glob
import csv

def collect_csv_filenames():
    """

    Collect all the *.csv files located in the test_data folder
    :return: list containing list of all filenames
    """
    filenames_list = glob.glob('./test_data/*.csv')
    return filenames_list

def read_csv(filename):
    """

    Read csv file and separate time and voltage into respective lists
    :param filename:
    :return:
    """
    csvfile = open(filename, "r")
    time = [ ]
    voltage = [ ]
    temp = csv.reader(csvfile, delimiter=",")
    for row in temp:
        time.append(float(row[0]))
        voltage.append(float(row[1]))
    return time, voltage

def write_json(type = 'json'):
    csvfile = open(filename,"r")
    temp = list(csv.reader(csvfile,delimiter=","))
    json_filename = filename.replace('.csv','.json')
    json_file = open(json_filename, "w")
    json_file.write(",".join(temp[0]))
    json_file.close

    return