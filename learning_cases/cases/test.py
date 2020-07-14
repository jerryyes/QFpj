import time


def decorator_info(func):
    def _deco_info():
        try:
            t_begin = time.time()
            print("%s start at %0.4f" % (func.__name__, t_begin))
            func()
        except:
            print('assert error has raised')
        else:
            print('run success')
        finally:
            t_end = time.time()
            print("%s end at %0.4f" % (func.__name__, t_end))
            print("%s executed in %0.4f ms" % (func.__name__, t_end - t_begin))

    return _deco_info


def test():
    time.sleep(5)
    now_time = int(time.time())
    print(now_time)
    assert now_time % 2, 'assert error has not raised'
    pass


# -------------------被测方法1-------------------
@decorator_info
def decorator_info_test():
    return test()

decorator_info_test()
