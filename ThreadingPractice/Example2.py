import threading
import time # sleep


# done = False

# def worker():
#     counter = 0
#     while not done:
#         time.sleep(1)
#         counter += 1
#         print(counter)

# threading.Thread(target=worker, daemon=True).start()


# input("Press enter to quit")
# done = True


done = False

def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")

threading.Thread(target=worker, daemon=True, args=("ABC",)).start()
threading.Thread(target=worker, daemon=True, args=("XYZ",)).start()


input("Press enter to quit")
done = True
