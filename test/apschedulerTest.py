from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job():
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

schdule = BlockingScheduler()
schdule.add_job(job,'cron', minute ='*/1')
schdule.start()