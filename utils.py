import numpy as np


def read_calib(filename):
    data = np.genfromtxt(filename, delimiter=': ',dtype='S8,f8')
    d = {}
    for i in range(3):
        d[data[i][0].tostring().decode('utf-8')] = data[i][1]
    p1, p2, a1, a2 = data[3][1], data[4][1], float(data[3][0].tostring().decode('utf-8')), float(data[4][0].tostring().decode('utf-8'))
    m = (p2-p1)/(a2-a1)
    c = p1-m*a1
    d['m'] = m
    d['c'] = c
    d['max_deg'] = (d['max'] - c) / m
    d['min_deg'] = (d['min'] - c) / m
    return d

if __name__=='__main__':
    print("Testing utils...")
    d = read_calib('servo_calib/0')
    print(d)
