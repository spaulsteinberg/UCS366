#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Samuel Steinberg"
__date__ = "November 13th, 2019"
import numpy as np
import ChartCategories as ch
import filefolders as ff
#NOV 15 ADJUST THIS FOR CATEGORIES

#load in data and write counts to file
def loadAndWrite():
    # maybe make a loading option here?
    statistics = np.load(str(ff.PATHS['DICT_PATH'] + "categorystats_week4.npy"), allow_pickle=True).item()
    # Write results to file
    with open(str(ff.PATHS['TEXT_PATH'] + "category_resultsweek4.txt"), "w+") as f:
        for element in statistics:
            if statistics[element] != 0:
                f.write(element)
                f.write(": ")
                f.write(str(statistics[element]))
                f.write("\n")
    return statistics

def CleanData(statistics):
    statistics['Education'] = statistics['schools'] + statistics['school'] + statistics['university'] +statistics['college']
    statistics['Hospitals'] = statistics['hospitals'] + statistics['hospital']
    statistics['Finance/Banking'] = statistics['finance'] + statistics['financial'] + statistics['banks'] + statistics['ATM'] \
                                    + statistics['banking']
    statistics['Governments'] = statistics['nations'] + statistics['state'] + statistics['government'] + statistics['nation']
    statistics['Water/Energy'] = statistics['water'] + statistics['energy'] + statistics['electricity'] + \
                                  statistics['dam'] + statistics['dams'] + statistics['oil']
    statistics['Automobiles'] = statistics['cars']
    del statistics['schools']
    del statistics['school']
    del statistics['university']
    del statistics['hospitals']
    del statistics['hospital']
    del statistics['finance']
    del statistics['financial']
    del statistics['banks']
    del statistics['nations']
    del statistics['state']
    del statistics['government']
    del statistics['nation']
    del statistics['water']
    del statistics['energy']
    del statistics['dam']
    del statistics['dams']
    del statistics['ATM']
    del statistics['banking']
    del statistics['oil']
    del statistics['college']
    del statistics['cars']
    return statistics

if __name__ == '__main__':
    statistics = loadAndWrite()
    size_list = []
    attack_list = []
    other_total = 0
    # -- Put smaller data into "Other" category, combined similar dict entries
    statistics = CleanData(statistics)
    print(statistics)
    for element in statistics:
        if statistics[element] != 0 and statistics[element] > 80:
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