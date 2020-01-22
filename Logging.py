#Debug- Detailed info, diagnostics
#Info- Confirmation of proper execution
#Warning- Error, but still working
#Error- Failure, part of the program may not work
#Critical- Program crash
#Default- Warning, Error, Critical

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

num_one = 3
num_two = 10

add_nums = add(num_one, num_two)
logging.debug('Add {} + {} = {}'.format(num_one, num_two, add_nums))
sub_nums = subtract(num_one, num_two)

multiply_nums = multiply(num_one, num_two)

divide_nums = divide(num_one, num_two)
