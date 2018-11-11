import os
import sys
import matplotlib.pyplot as plt

data_folder = sys.argv[1:]
data_folder = data_folder[0]

det_line = ['', '', '', '', 'Field', '', '', '', '', '', '', '', '', 'Moment', '', '', '\r\n']
det_line = " ".join(det_line)

color = ['b', 'g', 'r', 'c', 'm', 'y']
marker = ['^', '>', '<', 'v', 'o', 'd', 'p', '*', 's', 'P', 'X', 'H']
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b / gcd(a, b)

data_name_list = os.listdir(data_folder)
labels = []
results = {}
for data_name in data_name_list:
    if data_name[:5] != 'CFB-3':
        print 'Find a useless file in the folder, which named \"%s\".' %(data_name)
        continue
    tag, label1, _, label2 = data_name.split(' ')
#     print tag, label1, _, label2
    key = ' '.join([label1, label2])
#     labels.append(key)
    data_path = os.path.join(data_folder, data_name)
    with open(data_path) as f:
        all_lines = f.readlines()
    FLAG = False
    fields, moments = [], []
    for lines in all_lines[:-1]:
        if lines == det_line:
            FLAG = True
            continue
        elif FLAG == False:
            continue
        elif lines == '\r\n':
    #         print lines
            continue
        field, moment = lines.split('\n')[0].split(',')
        fields.append(float(field))
        moments.append(float(moment))
    results[key] = (fields, moments)
    
for i, key in enumerate(results.keys()):
    if len(results.keys()) <= lcm(len(color), len(marker)):
        plt.plot(results[key][0], results[key][1], ''.join([color[i%len(color)], marker[i%len(marker)]]))
        labels.append(key)
    elif len(results.keys()) <= len(color) * len(marker):
        plt.plot(results[key][0], results[key][1], ''.join([color[i/len(marker)], marker[i%len(marker)]]))
        labels.append(key)
    else:
        print "Too many lines in one plot, the number of line must less than 72"
        
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(labels, loc=0)
plt.xlabel("field")
plt.ylabel("moment")
plt.title("Magnetic Hysteresis Loop")
plt.show()
