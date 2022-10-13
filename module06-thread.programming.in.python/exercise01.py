from threading import Thread, Lock

data = 0
lock = Lock()


def task(name):
    global data
    print(f"Task ({name}) has just started!")
    for i in range(0, 100000):
        with lock:
            local = data
            local += 1
            print(f"{name} -> {local}")
            data = local
    print(f"Task ({name}) has completed: {data}")


t1 = Thread(target=task, args=("Thread A",))
t2 = Thread(target=task, args=("Thread B",))

t1.start()
t2.start()

t1.join()
print("t1 completed!")
t2.join()
print("t2 completed!")
print(f"application is done: {data}")
