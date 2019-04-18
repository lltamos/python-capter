from time import ctime, sleep
import string


def music():
    for i in range(3):
        print('我听了%d音乐 %s' % (i, ctime()))
        sleep(1)


def move(agrs):
    for i in range(3):
        print('我听了%d %s %s' % (i, agrs, ctime()))
        sleep(1)


if __name__ == '__main__':
    music()
    move('movie')
    print("all over %s" % ctime())
