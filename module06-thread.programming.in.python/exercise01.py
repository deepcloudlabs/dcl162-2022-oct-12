from threading import Thread


def task(name):
    print(f"Task ({name}) has just started!")
    for i in range(0, 1000):
        print(f"{name}: {i}")
    print(f"Task ({name}) has completed!")


t1 = Thread(target=task, args=("Thread A",))
t2 = Thread(target=task, args=("Thread B",))

t1.start()
t2.start()

t1.join()
print("t1 completed!")
t2.join()
print("t2 completed!")
print("application is done.")
