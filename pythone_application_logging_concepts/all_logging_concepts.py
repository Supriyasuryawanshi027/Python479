import logging
from logging.handlers import RotatingFileHandler
#logFormatter = logging.Formatter('%(asctime)s - %(message)s - %(funcName)s - %(lineno)s - %(levelname)s')
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("flipkart1.log")
logFormatter1 = logging.Formatter("%(asctime)s - %(message)s - %(funcName)s - %(lineno)s - %(levelname)s")
fileHandler.setFormatter(logFormatter1)


consoleHandler = logging.StreamHandler()
logFormatter2 = logging.Formatter("%(asctime)s - %(message)s - %(lineno)s - %(levelname)s")
consoleHandler.setFormatter(logFormatter2)


Shandler = RotatingFileHandler('sapp.log',maxBytes = 2048,backupCount = 10)
Shandler.setFormatter(logFormatter1)

thandler = logging.handlers.TimedRotatingFileHandler("tapp.log",when ="M")
thandler.setFormatter(logFormatter1)

rootLogger.addHandler(logFormatter1)
rootLogger.addHandler(consoleHandler)
rootLogger.addHandler(Shandler)
rootLogger.addHandler(thandler)


def addition(num1, num2):
    #print('')
    rootLogger.info(f'Inside addition{num1}, {num2}')
    result = num1+num2
    return result


def division(num1, num2):
    #print('Inside division')
    rootLogger.info(f'Inside division{num1}, {num2}')
    try:
        result = num1/num2
    except BaseException as e:
        rootLogger.error(f'Invalid values for divide {e.args}')
    return result


def launch_applicaion():
    while True:
        try:
            choice = int(input('Enter 1. Addition 2. Division\n'))
            num1 = int(input('Enter number 1 :'))
            num2 = int(input('Enter number 2 :'))
            final = None
            if choice == 1:
                final = addition(num1,num2)
            else:
                final = division(num1,num2)

            if final:
                rootLogger.info(f'Result--->{final}')
        except BaseException as e:
            logging.error(f'Invalid inputs {e.args}')

if __name__ == '__main__':
    launch_applicaion()