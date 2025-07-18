import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
    )

logger = logging.getLogger('ArithmaticApp')


def add(a,b):
    logger.debug(f'Adding {a}+{b}: {a+b}')
    return a+b

def subtract(a,b):
    logger.debug(f'Subtracting {a}-{b}: {a-b}')
    return a-b

def multiply(a,b):
    logger.debug(f'Multiply {a}*{b}: {a*b}')
    return a*b

def division(a,b):
    try:
        logger.debug(f'Division {a}/{b}: {a/b}')
        return a/b
    except Exception as e:
        logger.error(f'{e}')
        return None

add(10, 5)
subtract(10, 5)
multiply(10, 5)
division(10, 0)