import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:root123@localhost:3306/kartik_db")

try:
    
    df = pd.read_sql("SELECT * FROM `studentsperformance`", engine)

    
    df.to_csv("studentsperformance.csv", index=False)
    print(" studentsperformance.csv exported.")

    
    table = pa.Table.from_pandas(df)
    pq.write_table(table, "studentsperformance.parquet")
    print(" studentsperformance.parquet exported.")

    
    df_reset = df.reset_index(drop=True)

    
    schema = {
        "type": "record",
        "name": "studentsperformance",  
        "fields": [{"name": col, "type": "string"} for col in df_reset.columns],
    }

    
    df_str = df_reset.astype(str)
    records = df_str.to_dict(orient="records")

    
    with open("studentsperformance.avro", "wb") as out_file:
        fastavro.writer(out_file, schema, records)
    print(" studentsperformance.avro exported.")

except Exception as e:
    print(" error occurred:", e)
