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

Copyright (c) 2018 Enoch Chang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.