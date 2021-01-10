from datetime import datetime
from newsscraper import main
from sendnews import sendnews
from apscheduler.schedulers.blocking import BlockingScheduler





sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(main, 'interval', min=20)

sched.start()