from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('proj',
             broker='redis://localhost:6379/13',
             backend='redis://localhost:6379/13',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,

)

if __name__ == '__main__':
    app.start()
