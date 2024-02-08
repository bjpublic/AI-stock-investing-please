import time

def long_time():
    for i in range(10):
        time.sleep(10)

print('ONE')
long_time()
print("THREE")