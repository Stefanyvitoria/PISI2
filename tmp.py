import time

a1 =time.process_time() 
b = int(input()) + 2
a = time.process_time()



#b = time.process_time_ns()

print(a1,a)
print(a-a1)