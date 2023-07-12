""" Write a Python program to create multiple
threads and print their names."""

import threading

def print_thread_names():
    print("Current thread name: ", threading.current_thread().name)

# Create multiple threads
threads = []
for i in range(7):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

# Wait for all the threads to complete
for thread in threads:
    thread.join()

"""The "print_thread_names()" function is defined, which simply prints the current thread name using threading.current_thread().name.
We create a list of threads to store thread objects.
Using a loop, we create 7 threads and add them to the threads list. Each thread is assigned by the "print_thread_names()" function as the target.
We start each thread by calling its start method.
After starting all the threads, we use another loop to call the join method on each thread. Prior to exiting, the program waits for all threads to complete."""
