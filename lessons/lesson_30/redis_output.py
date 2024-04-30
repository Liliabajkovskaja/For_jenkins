import time
from random import choice

if __name__ == '__main__':
    print('start')
    while True:
        if choice(range(100)) > 80:
            print('Record was created')
        else:
            print('None')
        time.sleep(0.5)
