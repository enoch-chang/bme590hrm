import matplotlib.pyplot as plt
import numpy

class HeartRateMonitor:

    def __init__(self, time, voltage):
        self.time = time
        self.voltage = voltage

    def mean_hr_bpm(self):
        """

        Calculates the mean heart rate in beats per minute.
        :return mean_hr_bpm: mean heart rate
        """

        mean_hr_bpm = self.num_beats()/self.duration()

        return mean_hr_bpm

    def voltage_extremes(self):
        """

        Finds the max and min voltage in the data set
        :return voltage_extremes: tuple containing max and min voltage
        """

        voltage_extremes = []
        voltage_extremes[0] = min(self.voltage)
        voltage_extremes[1] = max(self.voltage)

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
        corr_voltage = numpy.correlate(self.voltage, self.voltage, mode = 'valid')
        print(corr_voltage)
        plt.plot(corr_voltage)
        plt.show()

        return

    def beats(self):
        """

        Finds the times corresponding to a heart beat
        :return beats: a list containing the times for each beat
        """

        return beats
