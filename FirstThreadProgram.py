"""
Author: Ralph Giles
Just tinkering with threads in Python. This is a simple example of how to create and run a thread.

This program creates 5 threads, each of which will sleep for a random amount of time, print a message, and then loop 5 times, 
sleeping for a random amount of time and printing a message when the thread finishes.  
The main thread will wait for all threads to finish before exiting if the thread.join() method is called.  If the thread.join() method is not called, 
the main thread will finish before the other threads and print the "All threads have finished." message before the other threads have finished.  
This is not what we want.  We want to wait for all threads to finish before exiting the program.

This program does not try to synchronize the threads in any way.  This is just a simple example of how to create and run threads in Python.  
There are many ways to synchronize threads, but that is beyond the scope of this example. But, I will add an example of how to synchronize threads in a future version of this program.

Page 362 of text was the inspiration for this code. I wanted to see it work!
"""

import random, time
from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        time.sleep(random.uniform(1.0, 3.0))
        print(f"Thread {self.name} is starting")
        for i in range(5): #Loop 5 times
            time.sleep(random.uniform(0.1, 7.0))
            #print(f"Thread {self.name} is Restarting") #You can uncomment this line to see the thread restarting, but it will make the output messy. 
        print(f"Thread {self.name} is finished")


def main():
    threads = [] #This will hold all the threads we create
    for i in range(5): #Create 5 threads.  Hard coded for now, but could be changed to user input.
        thread = MyThread(f"Thread-{i+1}") #Create a new thread with a unique name
        threads.append(thread) #Put the thread into the list of threads
        thread.start() #Start the thread running.  This will call the run() method of the thread.
    for thread in threads:
        """
        The join() method is used to wait for a thread to finish.  This is important because if the main thread finishes before the other threads, the program will exit and the other threads will be killed.  
        If you uncomment the i=5 line below, and comment out the thread.join() line, you will see that the main thread will finish before the other threads, and the program will exit before the other threads have finished.  
        This is not what we want.  We want to wait for all threads to finish before exiting the program.
        """
        #i=5  # This is just a stub to show how the thread.join () method works.
        thread.join() #This will force main to wait for all threads to finish
    print("All threads have finished.")


if __name__ == "__main__":
    main()
