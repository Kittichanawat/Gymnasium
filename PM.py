import random
import pandas as pd
from datetime import datetime, timedelta

# จำนวนบรรทัดข้อมูลที่ต้องการสร้าง
num_rows = 500

# เริ่มต้นวันเวลา
start_date = datetime(2024, 9, 1, 0, 0, 0)

# สร้างข้อมูล PM2.5 และเวลาที่สอดคล้อง
data = []
for i in range(num_rows):
    # สุ่มค่า PM2.5 โดยมี 5% ของข้อมูลเป็นค่าลบ
    if random.random() < 0.05:
        pm25_value = -random.uniform(1, 100)  # ค่าลบ
    else:
        pm25_value = random.uniform(1, 500)  # ค่าปกติ
        
    # สร้างวันเวลาที่เพิ่มขึ้นทีละ 1 ชั่วโมง
    timestamp = start_date + timedelta(hours=i)
    
    # เพิ่มข้อมูลในลิสต์
    data.append([timestamp, pm25_value])

# สร้าง DataFrame จากข้อมูล
df = pd.DataFrame(data, columns=['Timestamp', 'PM2.5'])

# แสดงตัวอย่างข้อมูล 10 บรรทัดแรก
print(df.head(10))

# บันทึกข้อมูลลงไฟล์ CSV (ถ้าต้องการ)
df.to_csv('pm25_data.csv', index=False, header=False)
