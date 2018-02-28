import matplotlib.pyplot as plt
import numpy
from peakdetect import peakdet

class HeartRateMonitor:

    def __init__(self, time, voltage, voltage_ref):
        self.time = time
        self.voltage = voltage
        self.voltage_ref = voltage_ref
        self.max_corr = []

    def mean_hr_bpm(self):
        """

        Calculates the mean heart rate in beats per minute.
        :return mean_hr_bpm: mean heart rate
        """
        duration_min = self.duration()/60
        mean_hr_bpm = self.num_beats()/duration_min

        return mean_hr_bpm

    def voltage_extremes(self):
        """

        Finds the max and min voltage in the data set
        :return voltage_extremes: tuple containing max and min voltage
        """

        voltage_extremes = []
        voltage_extremes.append(min(self.voltage))
        voltage_extremes.append(max(self.voltage))

        return voltage_extremes

    def duration(self):
        """

        Finds the total duration of the data set
        :return duration: duration of the data set
        """

        duration = self.time[len(self.time)-1]

        return duration

    def num_beats(self):
        """

        Determines the number of beats in the data set
        :return num_beats: number of beats in the data set
        """
        norm_voltage = self.voltage - numpy.mean(self.voltage)
        norm_voltage_ref = list(self.voltage_ref - numpy.mean(self.voltage_ref))
        ref_index = norm_voltage_ref.index(max(norm_voltage_ref))
        corr_voltage = numpy.convolve(norm_voltage, norm_voltage_ref[ref_index-30:ref_index+30], mode='same')
        # corr_voltage = numpy.convolve(norm_voltage, norm_voltage_ref[144:504], mode = 'same')

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

        return num_beats

    def beats(self):
        """

        Finds the times corresponding to a heart beat
        :return beats: a list containing the times for each beat
        """
        beats = []

        for i in self.max_corr:
            beats.append(i[1])

        return beats
