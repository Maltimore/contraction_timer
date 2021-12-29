import os
import datetime
import math


def parse_log_file(log_file_name):
    if not os.path.exists(log_file_name):
        state = 'no_contraction'
        last_start = None
        return state, last_start

    with open(log_file_name, 'r') as f:
        log = f.read()

    lines = log.splitlines()
    if len(lines) == 0:
        state = 'no_contraction'
        last_start = None
    elif lines[-2].startswith('START'):
        state = 'contraction'
        last_start = datetime.datetime.fromisoformat(lines[-2][7:])
    elif lines[-2].startswith('END'):
        state = 'no_contraction'
        last_start = datetime.datetime.fromisoformat(lines[-2][5:])
    else:
        raise Exception('Could not parse log file!')

    return state, last_start


def parse_timedelta_to_minutes_string(timedelta):
    minutes = math.floor(timedelta.seconds / 60)
    seconds = timedelta.seconds % 60
    return f'{minutes} minutes {seconds} seconds'


def wait_for_start(log_file, last_start):
    _ = input()
    start = datetime.datetime.now()
    start_string = f'START: {start}'
    print(start_string)
    log_file.write(start_string + '\n')
    if last_start is not None:
        time_between_starts_string = f'TIME BETWEEN STARTS: {parse_timedelta_to_minutes_string(start - last_start)}'
        print(time_between_starts_string)
        log_file.write(time_between_starts_string + '\n')

    wait_for_end(log_file, start)


def wait_for_end(log_file, last_start):
    _ = input()
    end = datetime.datetime.now()
    end_string = f'END: {end}'
    print(end_string)
    log_file.write(end_string + '\n')

    duration_string = f'DURATION: {parse_timedelta_to_minutes_string(end - last_start)}'
    print(duration_string)
    log_file.write(duration_string + '\n')

    wait_for_start(log_file, last_start)


state, last_start = parse_log_file('log.txt')
print(f'You are in {state}, press Enter when the state changes.')
with open('log.txt', 'a') as log_file:
    if state == 'no_contraction':
        wait_for_start(log_file, last_start)
    else:
        wait_for_end(log_file, last_start)
