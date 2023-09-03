import multiprocessing
import random
import time
from datetime import datetime

def process_function(id):
    sleep_time = random.randint(1, 5)
    print(f"Process {id} will sleep for {sleep_time} seconds.")
    time.sleep(sleep_time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {id} woke up at {current_time} and is now exiting.")

if __name__ == "__main__":
    processes = []
    num_processes = 3

    for i in range(num_processes):
        process = multiprocessing.Process(target=process_function, args=(i,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All processes have exited.")