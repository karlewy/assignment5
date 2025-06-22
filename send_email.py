import os
import yagmail


SENDER_EMAIL = "saxenakartik19@gmail.com"
APP_PASSWORD = "filzotuaheczubmn"
RECIPIENT_EMAIL = "karl09lewy@gmail.com"  


export_folder = os.getcwd()  


files_to_send = [
    os.path.join(export_folder, f)
    for f in os.listdir(export_folder)
    if f.endswith((".csv", ".parquet", ".avro"))
]


try:
    yag = yagmail.SMTP(SENDER_EMAIL, APP_PASSWORD)
    yag.send(
        to=RECIPIENT_EMAIL,
        subject=" Exported Tables - Data Pipeline",
        contents="Please find attached the exported tables (CSV, Parquet, Avro).",
        attachments=files_to_send
    )
    print(" Email sent")
except Exception as e:
    print(" Failed ", e)
