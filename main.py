""" Extracts filenames from specified directory and performs ECG analysis on
each dataset.
"""

import file_io
import process_ecg_data


def main():
    dir = './test_data/*.csv'
    filenames_list = file_io.collect_csv_filenames(dir)

    filename_ref = filenames_list[0]
    time, voltage_ref = file_io.read_csv(filename_ref)

    time_unit = input("Time is in min or sec (default = sec)? ")
    if time_unit != "sec" and time_unit != "min":
        print("Warning: Input was neither 'sec' or 'min'. Data saved as "
              "seconds.")

    for filename in filenames_list:
        time, voltage = file_io.read_csv(filename)
        hrm = process_ecg_data.HeartRateMonitor(time, voltage, voltage_ref,
                                                time_unit, filename)

        file_io.write_json(filename, hrm.output())

    print("Finished.")

if __name__ == "__main__":
    main()
