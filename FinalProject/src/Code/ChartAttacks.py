#!usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Samuel Steinberg"
__date__ = "November 13th, 2019"
import numpy as np
import matplotlib.pyplot as plt
import filefolders as ff
#generate a pie chart
def generatePieChart(size_list, attack_list):
    total = 0
    for i in size_list:
        total += i
    for i in range(len(size_list)):
        size_list[i] = round((size_list[i]/total)*100, 2)
        attack_list[i] = attack_list[i] + " - " + str(size_list[i]) + "%"
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    if len(size_list) > 10:
        colors = ['blue', 'red', 'purple', 'green', 'yellow', 'orange', 'pink', 'teal', 'navy', 'violet', 'springgreen']
        if len(size_list) > 11:
            for c in range(len(size_list)):
                colors.append(np.random.rand(3, ))
        patches, texts = ax.pie(size_list, shadow=True, startangle=90, colors=colors)
    else:
        patches, texts = ax.pie(size_list, shadow=True, startangle=90)
    plt.legend(patches, attack_list, loc="best")
    plt.title("Trending Cybersecurity Topics on Twitter (per 50,000 tweets)")
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(str(ff.PATHS['CHART_PATH'] + "PieChartRepNew4.PNG"))
    #plt.show()
    plt.close()

# generate a bar chart
def generateBarChart(size_list, attack_list):
    y_pos = np.arange(len(attack_list))
    colors = []
    for c in range(len(size_list)):
        colors.append(np.random.rand(3, ))
    fig = plt.figure()
    
    plt.gcf().subplots_adjust(bottom=0.30)
    ax = fig.add_subplot(111)
    #plt.ylim([0,3500])
    bar_list = ax.bar(y_pos, size_list, align='center')
    for i in range(len(colors)):
        bar_list[i].set_color(colors[i])
    plt.xticks(y_pos, attack_list, rotation='vertical')
    plt.ylabel('Occurrences')
    plt.title('Trending Cybersecurity Topics on Twitter (per 50,000 tweets)')
    plt.xlabel('Vulnerability or Threat')
    #
    rects = ax.patches

    labels = [i for i in size_list]
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 2, label,
            ha='center', va='bottom')
    #
    #plt.show()
    plt.savefig(str(ff.PATHS['CHART_PATH'] + "BarChartRepNew4.PNG"))
    plt.close()