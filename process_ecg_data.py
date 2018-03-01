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

    def __init__(self, time, voltage, voltage_ref):
        """Initializes instance of HeartRateMonitor based on file input

        :param time:
        :param voltage:
        :param voltage_ref:
        """
        self.time = time
        self.voltage = voltage
        self.voltage_ref = voltage_ref
        self.max_corr = []

        try:
            self.check_input(self.time)
        except ValueError:
            logging.error("There is a ValueError in the list of times. The numbers must be real.")
            print("Time input must be a list containing only of real numbers.")
            quit()
        except TypeError:
            logging.error("There is a TypeError in the list of times. The numbers must be of a numerical type.")
            print("Time input must be a list containing numerical type entries.")
            quit()

        try:
            self.check_input(self.voltage)
        except ValueError:
            logging.error("There is a ValueError in the list of voltages. The numbers must be real.")
            print("Voltage input must be a list containing only of real numbers.")
            quit()
        except TypeError:
            logging.error("There is a TypeError in the list of voltages. The numbers must be of a numerical type.")
            print("Voltage input must be a list containing numerical type entries.")
            quit()

        try:
            import logging
        except ImportError:
            logging.error("No such file")
            print("No Imported file")

        logging.basicConfig(filename='hrm_log.txt',
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)

    def mean_hr_bpm(self):
        """Calculates the mean heart rate in beats per minute.

        :return mean_hr_bpm: mean heart rate
        """
        duration_min = self.duration()/60
        mean_hr_bpm = self.num_beats()/duration_min

        logging.info("Mean heart rate successfully calculated.")

        return mean_hr_bpm

    def voltage_extremes(self):
        """Finds the max and min voltage in the data set

        :return voltage_extremes: tuple containing max and min voltage
        """

        voltage_extremes = []
        voltage_extremes.append(min(self.voltage))
        voltage_extremes.append(max(self.voltage))

        logging.info("Maximum and minimum voltages successfully identified.")

        return voltage_extremes

    def duration(self):
        """Finds the total duration of the data set

        :return duration: duration of the data set
        """

        duration = self.time[len(self.time)-1]

        logging.info("Duration successfully calculated.")

        return duration

    def num_beats(self):
        """Determines the number of beats in the data set

        :return num_beats: number of beats in the data set
        """

        norm_voltage = list(self.voltage - numpy.mean(self.voltage))
        norm_voltage_ref = list(self.voltage_ref - numpy.mean(self.voltage_ref))
        ref_index = norm_voltage.index(max(norm_voltage))
        # corr_voltage = numpy.convolve(norm_voltage, norm_voltage[ref_index-100:ref_index+100], mode='same')
        corr_voltage = numpy.convolve(norm_voltage, norm_voltage_ref[144:504], mode = 'same')

        min_corr = []
        voltage_delta = numpy.sqrt(numpy.mean(corr_voltage**2))*2.5
        print(voltage_delta)
        [self.max_corr, min_corr] = peakdet(corr_voltage, voltage_delta, self.time)
        max_corr_voltage = []
        for i in self.max_corr:
            max_corr_voltage.append(i[0])
        num_beats = len(max_corr_voltage)

        print(corr_voltage)
        plt.plot(corr_voltage)
        plt.show()

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
