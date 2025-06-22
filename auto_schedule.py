import schedule
import time
import subprocess

def job():
    print(" Running export.")
   
    subprocess.run(["python", "export_formats.py"])


schedule.every(1).minutes.do(job)

print("Auto-export scheduler started .")


while True:
    schedule.run_pending()
    time.sleep(1)
