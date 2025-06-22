import pandas as pd
from sqlalchemy import create_engine


source_engine = create_engine("mysql+pymysql://root:root123@localhost:3306/kartik_db")


target_engine = create_engine("mysql+pymysql://root:root123@localhost:3306/kartiktarget_db")

try:
    
    df = pd.read_sql("SELECT * FROM `studentsperformance`", source_engine)
    print(" Data read from source database.")

   
    df.to_sql("studentsperformance", target_engine, index=False, if_exists="replace")
    print(" Data written to target database as `studentsperformance`.")

except Exception as e:
    print(" Error occurred:", e)
