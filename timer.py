import datetime


previous_start = None
with open('log.txt', 'a') as f:
    while True:
        _ = input()
        start = datetime.datetime.now()
        start_string = f'START: {start}'
        print(start_string)
        f.write(start_string + '\n')
        if previous_start is not None:
            time_between_starts = start - previous_start
            time_between_starts_string = f'TIME BETWEEN STARTS: {time_between_starts.seconds} seconds'
            print(time_between_starts_string)
            f.write(time_between_starts_string + '\n')
        previous_start = start

        _ = input()
        end = datetime.datetime.now()
        end_string = f'END: {end}'
        print(end_string)
        f.write(end_string + '\n')

        duration = (end - start).seconds
        duration_string = f'DURATION: {duration} seconds'
        print(duration_string)
        f.write(duration_string + '\n')
