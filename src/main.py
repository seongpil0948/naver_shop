from crawler import Crawler
from sys import version_info as v
from sys import exit
import os
import multiprocessing
from math import ceil
if v.major != 3 or v.minor != 9 or v.micro != 1:
    print("Python 3.9.1 is required.")
    exit(1)
else:
    print('success')


def go_crawl(count, code):
    print("PID: ", os.getpid(), "count: ", count, "code: ", code)
    for _ in range(count):
        c = Crawler(code)
        c.go()


if __name__ == "__main__":
    code = abs(int(input("페이지 코드를 입력 하세요: ")))
    total_count = abs(int(input("반복 횟수를 입력 해주세요: ")))
    each_proc_count = 30
    for_proc_count = ceil(total_count / each_proc_count)
    # each_count * total_count
    with multiprocessing.Pool() as pool:
        pool.starmap(
            go_crawl,
            zip(
                [each_proc_count] * for_proc_count,
                [code] * for_proc_count
            )
        )
