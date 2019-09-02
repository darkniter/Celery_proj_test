from proj.tasks import add, mul
from time import sleep


def test_init(celery_val):
    print(celery_val)
    pass


def standby(celery_val_wait):
    while not celery_val_wait.ready():
        sleep(1)
        print(celery_val_wait.ready())
    test_init(celery_val_wait.get())


def main():
    celery_val_init = add.delay(10, 20)
    standby(celery_val_init)

    celery_val_init = mul.delay(123123123, 12223409879)
    standby(celery_val_init)

    celery_val_init = add.delay('ab', 'ba')
    standby(celery_val_init)


if __name__ == "__main__":
    main()
