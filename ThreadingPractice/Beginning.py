import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(0.85)
    print("now done")

# Turn into thread and run
x = threading.Thread(target=func)
x.start()

print(threading.active_count())
time.sleep(0.9)
print("finally")

# ran
# 2
# finally
# done
# now done
