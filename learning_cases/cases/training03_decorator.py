"""
--装饰器的使用
1、实现decorator_info
实现一个装饰器decorator_info,装饰函数decorator_info_test，使被装饰方法执行时decorator_info执行以下功能：
    1>捕获test抛出的异常，当捕获到异常时，忽略其异常信息并打印'assert error has raised',未捕获到异常时打印'run success';
    2>打印test函数的执行时间(tips:执行后的时间戳-执行前时间戳)；
    3>打印被装饰方法的方法名；
2、实现decorator_retry
实现一个装饰器decorator_retry,接收一个参数retry_times,当被装饰方法执行时,decorator_retry：
    1>当被装饰函数执行遇到未处理异常时可以重新执行；
    2>由入参retry_times控制重试，retry_times表示被装饰函数执行遇到异常时最大重试次数(执行无异常则不重试);retry_times默认值为1；
    3>运行前验证retry_times，不是自然数则抛出异常(AssertionError or ValueError或任意Exception均可)；
    4>retry_times耗尽（达到最大重试次数依然抛出异常）时，给出明显提示并退出运行；
    5>捕获每次函数运行时抛出的异常并打印；
    6>执行结束后打印实际重试次数；
"""

import time
import traceback


# -----------------待实现方法1------------------
def decorator_info(func):
    def _deco_info(*args, **kwargs):
        try:
            t_begin = time.time()
            print("%s start at %0.4f" % (func.__name__, t_begin))
            func(*args, **kwargs)
        except:
            print('assert error has raised')
        else:
            print('run success')
        finally:
            t_end = time.time()
            print("%s end at %0.4f" % (func.__name__, t_end))
            print("%s executed in %0.4f ms" % (func.__name__, t_end - t_begin))

    return _deco_info
    pass


# -----------------待实现方法2------------------
def decorator_retry(retry_times=1):
    def _deco_retry(func):
        def __deco_retry(*args, **kwargs):
            assert retry_times >= 0 and isinstance(retry_times, int), 'retry_times inserted is not natural number.'
            ret = False
            attemp = 0
            try:
                ret = func(*args, **kwargs)
            except:
                while attemp < retry_times:
                    try:
                        ret = func(*args, **kwargs)
                    except:
                        traceback.print_exc()
                        attemp += 1
                        try:
                            assert attemp < retry_times, 'retry times useless. exit.'
                        except:
                            continue
                    else:
                        break
            print("Total retry times：%s" % (attemp))
            return ret
            pass

        return __deco_retry

    return _deco_retry
    pass


class Solution:
    # ------------------BASE-----------------------
    @staticmethod
    def test():
        time.sleep(5)
        now_time = int(time.time())
        print(now_time)
        # assert now_time % 2, 'assert error has not raised'
        assert True, 'assert error has raised'
        pass

    # -------------------被测方法1-------------------
    @staticmethod
    @decorator_info
    def decorator_info_test():
        return Solution.test()

    # -------------------被测方法2-------------------
    @staticmethod
    @decorator_retry(2)
    def decorator_retry_test():
        return Solution.test()


if __name__ == '__main__':
    # Solution.decorator_info_test()
    Solution.decorator_retry_test()
