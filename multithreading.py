import threading
import time

def task1():
    for i in range(100):
        print("Task 1 running")
        time.sleep(1)

def task2():
    for i in range(100):
        print("Task 2 running")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both tasks completed")
