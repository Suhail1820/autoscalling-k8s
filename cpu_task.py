import math
import time

def cpu_intensive_task():
    # Perform an intensive CPU-bound task
    count = 0  # To track how many times the loop has run
    while True:
        count += 1  # Increment the loop count
        print(f"Iteration {count}: Starting computation...")
        
        # Perform a less resource-intensive task
        result = sum(i * i for i in range(1, 10**6))
        print(f"Iteration {count}: Computation result is {result}.")

        # Sleep to simulate periodic processing
        print(f"Iteration {count}: Sleeping for 0.1 seconds...\n")
        time.sleep(0.1)

if __name__ == "__main__":
    print("Starting the CPU-intensive task...\n")
    cpu_intensive_task()
