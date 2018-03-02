""" Analyzes ECG data

An instance of this class is created based on input parameters of the ECG data and a reference waveform.
The functions in this class allows for the computation of the mean HR, max/min voltages, duration,
number beats and corresponding times for each beat.
"""

import matplotlib.pyplot as plt
import numpy
from peakdetect import peakdet
import logging

class HeartRateMonitor:

    def __init__(self, time, voltage, voltage_ref, time_unit="sec", filename=""):
        """Initializes instance of HeartRateMonitor based on file input and sets up logging

        :param time:
        :param voltage:
        :param voltage_ref:
        :param time_unit: users can input unit for timescale, if none specified, unit is assumed to be seconds
        """
        self.time_input = time
        self.time = []
        self.voltage_input = voltage
        self.voltage = []
        self.voltage_ref = []
        self.filename = filename

        for k in voltage_ref:
            self.voltage_ref.append(float(k))

        self.max_corr = []
        self.time_unit = time_unit

        try:
            import logging
        except ImportError:
            logging.error("No such file")
            print("No Imported file")

        logging.basicConfig(filename='hrm_log.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)



        logging.info("%s%s", "Opened ", self.filename)

        self.process_input()

    def is_float(self, input):
        """ Checks if entry is a numerical value

        :param input: from raw data
        :return: boolean
        """
        try:
            float(input)
            return True
        except ValueError:
            return False

    def process_input(self):
        """Checks that the input is the right type and that the time and voltage vectors are of equal length

        :return:
        """

        for idx, i in enumerate(self.time_input):
            if self.is_float(i):
                if self.time_unit == "min":
                    self.time.append(floar(i) * 60)
                else:
                    self.time.append(float(i))
            else:
                if self.is_float(self.time_input[idx-1]) and self.is_float(self.time_input[idx+1]):
                    fill_in = (float(self.time_input[idx-1]) + float(self.time_input[idx+1]))/2
                else:
                    fill_in = self.time[len(self.time) - 1]
                self.time.append(fill_in)
                logging.warning("Time gap detected. Interpolation completed.")
        for idx, j in enumerate(self.voltage_input):
            if self.is_float(j):
                self.voltage.append(float(j))
            else:
                if self.is_float(self.voltage_input[idx-1]) and self.is_float(self.voltage_input[idx+1]):
                    fill_in = (float(self.voltage_input[idx-1]) + float(self.voltage_input[idx+1]))/2
                else:
                    fill_in = self.voltage[len(self.voltage) - 1]
                self.voltage.append(fill_in)
                logging.warning("Bad data in voltage detected. Interpolation completed.")

        try:
            if numpy.isreal(self.time) is False:
                raise ValueError
        except ValueError:
            logging.error("There is a ValueError in the list of times. The numbers must be real.")
            print("Time input must be a list containing only of real numbers.")

        try:
            if numpy.isreal(self.voltage) is False:
                raise ValueError
        except ValueError:
            logging.error("There is a ValueError in the list of voltages. The numbers must be real.")
            print("Voltage input must be a list containing only of real numbers.")


        if len(self.voltage) != len(self.time):
            logging.error("You must have the same number of voltage and time entries.")
            raise InputError

        return None


    def mean_hr_bpm(self):
        """Calculates the mean heart rate in beats per minute.

        :return mean_hr_bpm: mean heart rate
        """
        duration_min = self.duration()/60
        mean_hr_bpm = self.num_beats()/duration_min

        logging.info("Mean heart rate successfully calculated.")
        if mean_hr_bpm > 180:
            logging.warning("Warning: Mean heart rate detected to be more than 180 bpm.")
        if mean_hr_bpm < 40:
            logging.warning("Warning: Mean heart rate detected to be less than 40 bpm.")

        return mean_hr_bpm

    def voltage_extremes(self):
        """Finds the max and min voltage in the data set

        :return voltage_extremes: tuple containing max and min voltage
        """

        voltage_extremes = []
        voltage_extremes.append(min(self.voltage))
        voltage_extremes.append(max(self.voltage))

        logging.info("Maximum and minimum voltages successfully identified.")

        if abs(voltage_extremes[0]) > 300 or abs(voltage_extremes[1]) > 300:
            logging.warning("Warning: Voltage is out of ECG range (300V)")

        return voltage_extremes

    def duration(self):
        """Finds the total duration of the data set

        :return duration: duration of the data set
        """

        duration = self.time[len(self.time)-1]

        logging.info("Duration successfully calculated.")

        if duration < 5:
            logging.info("Warning: Duration is less than 5 seconds. Calculation accuracy may be affected.")

        return duration

    def num_beats(self):
        """Determines the number of beats in the data set

        :return num_beats: number of beats in the data set
        """

        norm_voltage = list(self.voltage - numpy.mean(self.voltage))
        norm_voltage_ref = list(self.voltage_ref - numpy.mean(self.voltage_ref))
        corr_voltage = numpy.convolve(norm_voltage, norm_voltage_ref[144:504], mode = 'same')

        voltage_delta = numpy.sqrt(numpy.mean(corr_voltage**2))*2.5
        [self.max_corr, min_corr] = peakdet(corr_voltage, voltage_delta, self.time)
        max_corr_voltage = []
        for i in self.max_corr:
            max_corr_voltage.append(i[0])
        num_beats = len(max_corr_voltage)

        logging.info("Number of beats successfully counted.")

        return num_beats

    def beats(self):
        """ Finds the times corresponding to a heart beat

        :return beats: a list containing the times for each beat
        """
        beats = []

        for i in self.max_corr:
            beats.append(i[1])

        logging.info("Times corresponding to each heartbeat successfully identified.")

        return beats

    def output(self):
        """Summarizes calculated outputs from the functions of this class.

        :return hrm_info: a dictionary containing all the object attributes
        """

        hrm_info = {'Mean Heart Rate: ': self.mean_hr_bpm(),
                    'Voltage Extremes: ': self.voltage_extremes(),
                    'Duration: ': self.duration(),
                    'Number of Beats: ': self.num_beats(),
                    'Times when beats occurred: ': self.beats()
                    }

        logging.info("%s%s", "Completed ", self.filename)

        return hrm_info