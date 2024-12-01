import threading
import time

#added a timer for lols#

# Shared counter and lock
counter = 0
counter_lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000_000 // 10):
        with counter_lock:
            counter += 1

def decrement():
    global counter
    for _ in range(100_000_000 // 10):
        with counter_lock:
            counter -= 1

def main():
    global counter

    # Incrementing
    print("Incrementing counter from 0 to 1000000000 using 10 threads")
    threads = []
    start_time = time.time()  # Start the timer

    # Create and start increment threads
    for _ in range(10):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()  # End the timer
    print(f"Final value is {counter}")
    print(f"Time taken to increment: {end_time - start_time:.2f} seconds")

    # Decrementing
    print("Decrementing counter from 1000000000 to 0 using 10 threads")
    threads = []
    start_time = time.time()  # Start the timer

    # Create and start decrement threads
    for _ in range(10):
        thread = threading.Thread(target=decrement)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()  # End the timer
    print(f"Final value is {counter}")
    print(f"Time taken to decrement: {end_time - start_time:.2f} seconds")
    print(f"I added a timer for funsies")
if __name__ == "__main__":
    main()
