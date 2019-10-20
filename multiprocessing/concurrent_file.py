import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executer:
    secs = [5, 4, 3, 2, 1]
    results = executer.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')