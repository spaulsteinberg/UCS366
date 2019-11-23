#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Samuel Steinberg"
__date__ = "November 13th, 2019"
import numpy as np
import ChartAttacks as ch
import filefolders as ff
#NOV 15 ADJUST THIS FOR CATEGORIES

#load in data and write counts to file
def loadAndWrite():
    # maybe make a loading option here?
    statistics = np.load(str(ff.PATHS['DICT_PATH'] + "stats_week4.npy"), allow_pickle=True).item()
    # Write results to file
    with open(str(ff.PATHS['TEXT_PATH'] + "resultsweek4.txt"), "w") as f:
        for element in statistics:
            if statistics[element] != 0:
                f.write(element)
                f.write(": ")
                f.write(str(statistics[element]))
                f.write("\n")
    return statistics

if __name__ == '__main__':
    statistics = loadAndWrite()
    print(statistics)
    size_list = []
    attack_list = []
    other_total = 0
    # -- Put smaller data into "Other" category, manually clean here each time
    statistics['DDoS'] = statistics['DDoS'] + statistics['DoS']
    statistics['theft/fraud'] = statistics['theft'] + statistics['fraud']
    statistics['nation state'] = statistics['state-sponsored'] + statistics['nation-state']
    statistics['SQL'] = statistics['SQL'] + statistics['sql'] + statistics['injection']
    statistics['XSS'] = statistics['XSS'] + statistics['xss'] + statistics['injection']
    statistics['Servers'] = statistics['server']
    del statistics['DoS']
    del statistics['theft']
    del statistics['fraud']
    del statistics['state-sponsored']
    del statistics['nation-state']
    del statistics['sql']
    del statistics['xss']
    del statistics['injection']
    del statistics['server']

    for element in statistics:
        if statistics[element] != 0 and statistics[element] > 150:
            size_list.append(statistics[element])
            attack_list.append(element)
        else:
            other_total += statistics[element]
    attack_list.append("Other")
    size_list.append(other_total)
    print(size_list, attack_list)

    # simply setting copy=original makes a reference to the original list. must use [:] to copy!!
    ch.generatePieChart(size_list[:], attack_list[:])
    ch.generateBarChart(size_list[:], attack_list[:])