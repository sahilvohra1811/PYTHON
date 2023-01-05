import threading
from threading import *

def display():
    for i in range(10):
        print("i am sahil....")
t1 = Thread(target=display())
t1.start()
# for i in range(10):
#     print(i)
# print(threading.active_count())
# print(threading.current_thread())

# def even():
#     print("this is even : ")
#     for i in range(0,20,2):
#         print(i)
# def odd():
#     print("this is odd : ")
#     for i in range(0,20,1):
#         print(i)
# trd1 = threading.Thread(target=even)
# trd2 = threading.Thread(target=odd)
# trd1.start()
# trd2.start()
# trd1.join()
# trd2.join()
# print("end")

