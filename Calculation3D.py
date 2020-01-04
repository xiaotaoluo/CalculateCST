import math


class Calculation3D(object):
    def __init__(self, *, freq_coefficient, cap_coefficient, ind_coefficient):
        self.freq_coefficient = freq_coefficient
        self.cap_coefficient = cap_coefficient
        self.ind_coefficient = ind_coefficient

    def cal_freq(self, *, freq_extra, freq_ideal):
        """计算频率变化"""
        c = []
        f1 = []
        f2 = []
        for i in freq_extra:
            f1.append(i)
        for i in freq_ideal:
            f2.append(i)
        if len(f1) == len(f2):
            for i in range(len(f1)):
                c.append(round((float(f1[i]) - float(f2[i])) / float(self.freq_coefficient), 6))
        else:
            pass
        return c

    def cal_coupling(self, *, negative_index, coupling_extra, coupling_ideal):
        """计算耦合变化"""
        coupling1 = []
        coupling2 = []
        coupling_change = []

        for i in coupling_extra:
            coupling1.append(i)
        for i in coupling_ideal:
            coupling2.append(i)

        if len(coupling1) == len(coupling2):
            for i in range(len(coupling1)):
                coupling_change.append(
                    round((math.fabs(float(coupling2[i])) - math.fabs(float(coupling1[i])))
                          / float(self.ind_coefficient), 5))
        for i in negative_index:
            coupling_change[i] = round((math.fabs(float(coupling1[i])) - math.fabs(float(coupling2[i])))
                                       / float(self.cap_coefficient), 5)
        return coupling_change

    def get_coefficient(self):
        """返回斜率设置值"""
        return self.freq_coefficient, self.cap_coefficient, self.cap_coefficient

    def set_coefficient(self, *, freq_coefficient, cap_coefficient, ind_coefficient):
        """设置斜率值"""
        self.freq_coefficient = freq_coefficient
        self.cap_coefficient = cap_coefficient
        self.ind_coefficient = ind_coefficient
