import datetime
import sys
import logging


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


# def truefalse(x):
#     if x == True:
#         print(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54,
#               56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100)
#     elif x == False:
#         print(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
#               57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99)
value=0
def truefalse(x):
    if x == "True":
        for value in range(100):
            if value % 2 == 0:
                print(value)
                value=value+1
    if x == "False":
        for value in range(100):
            if value % 2 == 1:
                print(value)
                value=value+1

def functionWithError():
    n = ("String")
    try:
        n = int(n)
        logging.info("all is ok")
    except:
        logging.error("nothing is not ok")

