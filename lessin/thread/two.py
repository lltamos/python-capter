from time import ctime, sleep
import string
import threading


def music():
    for i in range(3):
        print('我听了%d音乐 %s\n' % (i, ctime()))
        sleep(1)


def move(args):
    for i in range(3):
        print('我听了%d %s %s\n' % (i, args, ctime()))
        sleep(1)


if __name__ == '__main__':
    thread = []
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=move, args=('move',))
    thread.append(t1)
    thread.append(t2)
    for t in thread:
        t.setDaemon(True)
        t.start()

    t.join()
    print("all over %s" % ctime())
