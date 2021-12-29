import datetime
import math

import numpy as np
import matplotlib.pyplot as plt


def parse_log_file(log_file):
    with open(log_file_name, 'r') as f:
        log = f.read()

    lines = log.splitlines()

    if lines[0].startswith('END'):
        lines = lines[2:]

    start_lines = [line for line in lines if line.startswith('START')]
    end_lines = [line for line in lines if line.startswith('END')]
    starts = [datetime.datetime.fromisoformat(line[7:]) for line in start_lines]
    ends = [datetime.datetime.fromisoformat(line[5:]) for line in end_lines]

    start_intervals = []
    for i in range(1, len(starts)):
        start_intervals.append(math.floor((starts[i] - starts[i - 1]).seconds / 60))

    durations = []
    for i in range(len(starts)):
        durations.append((ends[i] - starts[i]).seconds)

    return np.array(starts[1:]), np.array(start_intervals), np.array(durations[:-1])


log_file_name = 'log.txt'
starts, start_intervals, durations = parse_log_file(log_file_name)

fig, ax = plt.subplots()
ax.plot(starts, start_intervals, color='blue')
ax.set_ylabel('intervals [minutes]', color='blue')
ax2 = ax.twinx()
ax2.plot(starts, durations, color='red')
ax2.set_ylabel('durations [seconds]', color='red')
plt.show()
