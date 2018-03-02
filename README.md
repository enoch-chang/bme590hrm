This README details the information for the file input/output, ECG processing and related scripts found in this folder.

## Sources
All .py scripts are written by Enoch Chang (GitHub: enoch-chang) except for **peakdetect.py** which was written by Eli Billauer and was obtained online where it is released for the public domain.

## Script Description
* **file_io.py** includes three functions to collect filenames, read csv files and to write json files.
* **test_file_io.py** includes unit testing for functions in file_io.py 
* **process_ecg_data.py** includes functions to process the raw ECG data, including obtaining its mean heart rate, total beats, the corresponding times, duration of the ECG test and average heart rate.
* **test_hrm_class.py** includes unit testing associated to functions found in process_ecg_data.py
* **main.py** is the executable file to process the ECG data found in /test_data
* **peakdetect.py** identifies peaks in a waveform based on a specified tolerance (delta)

##Travis CI Status
[![Build Status](https://travis-ci.org/enoch-chang/bme590hrm.svg?branch=master)](https://travis-ci.org/enoch-chang/bme590hrm)
