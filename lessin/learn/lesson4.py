def consumer():
    print('init consumer')
    r = ''

    while True:
        n = yield r
        print('yield 接收消息 %s' % n)
        if not n:
            return
        print('[consumer] consuming %s' % n)
        r = '200 Ok'


def product(c):
    print('init product')
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close


c = consumer()
product(c)
