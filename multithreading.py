# importing the threading module
import threading
import time
 
def print_square(num):
    print('Calculate the square of given number')
    for n in num:
      time.sleep(0.3)
    # function to print cube of given num
      print("Cube:",n*n)
 
 
def print_cube(num):
    print('Calculate the cube of given number')
    for n in num:
      time.sleep(0.3)
    # function to print square of given num
      print("Square:",n*n*n)

arr = [2, 3, 4, 5]

t = time.time()
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(arr,))
    t2 = threading.Thread(target=print_cube, args=(arr,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # both threads completely executed
    print("Done!")

print('Total time taking by threads is:',time.time()-t)
print('Again executing main thread')