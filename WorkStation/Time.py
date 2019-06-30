import time

"""
计时器
"""


def currentTimeMillis():
    """
    和 Java 方法 System.currentTimeMillis() 一样
    :return: 自1970年某时开始的毫秒数
    """
    return int(time.time() * 1000.0)


class Timer:
    __invokeTimes = 0
    __startTime = 0
    __StopTime = 0
    __time = 0

    @classmethod
    def invoke(cls):
        cls.__invokeTimes += 1
        if cls.__invokeTimes % 2 == 1:
            cls.__startTime = currentTimeMillis()
            # print(cls.__startTime)
        else:
            cls.__StopTime = currentTimeMillis()
            # print(cls.__StopTime)
            cls.__time = float(cls.__StopTime - cls.__startTime) / 1000
            print("运行时间{: 0.3f}s".format(cls.__time))

    @classmethod
    def sleep(cls, t):
        time.sleep(t / 1000.0)

    @classmethod
    def help(cls):
        print("调用invoke()开始计时，再次调用返回时长")
        print("调用sleep(t)线程休息t/ms")

    @classmethod
    def text(cls):
        print("进行200ms测试")
        cls.invoke()
        cls.sleep(200)
        cls.invoke()

# 使用示例
# Timer.invoke()
# Timer.sleep(200)
# Timer.invoke()
