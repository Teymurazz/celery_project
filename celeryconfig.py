broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

from celery.schedules import crontab

beat_schedule = {
    'fetch-api-data-every-5-minutes': {
        'task': 'tasks.fetch_and_store_api_data',
        'schedule': crontab(hour='*/1'),
    },
}
