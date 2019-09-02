from proj import celery
from proj.tasks import add


def test_init(celery_val):
    print(celery_val)
    pass


def main():
    celery_val_init = add.delay(10, 20)
    while not celery_val_init.ready():
        print(celery_val_init.ready())

    test_init(celery_val_init.get())

    celery_val_init = add.delay('ab', 'ba')
    while not celery_val_init.ready():
        print(celery_val_init.ready())

    test_init(celery_val_init.get())


if __name__ == "__main__":
    main()
