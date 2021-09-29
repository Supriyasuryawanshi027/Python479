import logging
logger = logging.basicConfig(filename='flipkart.log', filemode='a', level=logging.INFO, format= '%(asctime)s - %(message)s - %(funcName)s - %(lineno)s - %(levelname)s' )


logging.debug(f'This is debug msg')
logging.info(f'This is info msg')
logging.error(f'This is error msg')
logging.critical(f'This is critical msg')
logging.warning(f'This is warning msg')


def addition(num1, num2):
    #print('')
    logging.info(f'Inside addition{num1}, {num2}')
    result = num1+num2
    return result


def division(num1, num2):
    #print('Inside division')
    logging.info(f'Inside division{num1}, {num2}')
    try:
        result = num1/num2
    except BaseException as e:
        logging.error(f'Invalid values for divide {e.args}' )
    return result


def launch_applicaion():
    while True:
        try:
            choice =int(input('Enter 1. Addition 2. Division\n'))
            num1 = int(input('Enter number 1 :'))
            num2 = int(input('Enter number 2 :'))
            final = None
            if choice == 1:
                final = addition(num1,num2)
            else:
                final = division(num1,num2)

            if final:
                logging.info(f'Result--->{final}')
        except BaseException as e:
            logging.error(f'Invalid inputs {e.args}')

if __name__ == '__main__':
    launch_applicaion()
