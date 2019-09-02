from proj.tasks import add, mul
from time import sleep
from random import randint
import sys


def test_init(celery_val):
    print(celery_val)
    pass


def standby(celery_val_wait):
    while not celery_val_wait.ready():
        print(celery_val_wait.ready(), celery_val_wait.id)
    test_init(celery_val_wait.get())


def main():
    celery_val_init = add.delay(10, 20)
    standby(celery_val_init)

    celery_val_init = mul.delay(randint(0, sys.maxsize), randint(0, sys.maxsize))
    standby(celery_val_init)

    celery_val_init = add.delay('ab', 'ba')
    standby(celery_val_init)

    celery_val_init = mul.delay(randint(0, sys.maxsize), randint(0, sys.maxsize))
    standby(celery_val_init)

if __name__ == "__main__":
    main()
