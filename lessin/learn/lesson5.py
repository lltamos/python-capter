class IterOrNext(object):
    @staticmethod
    def test_one():
        ls = ['数据一', '数据二', '数据三', '数据四', '数据五']
        print(len(ls))
        it = iter(ls)
        for i in ls:
            print(i, end=" ")
        print(next(it))


# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发
# StopIteration 异常来结束迭代。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            print('MyNumbers 超过限界')
            raise StopIteration


if __name__ == '__main__':
    IterOrNext.test_one()
