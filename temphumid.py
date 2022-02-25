import sqlite3
import serial
import time
from datetime import datetime

try:
    db = sqlite3.connect('temphumid.db')
except Error as e:
    print(e)

# Create cursor to execute commands
cursor = db.cursor()

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600)

while True:
    time.sleep(10)
    # Get and prepare data
    data = str(arduino.readline())
    if len(data) == 16:
        data = data[-14:]
        data = data[:11]
    elif len(data) == 15:
        data = data[-13:]
        data = data[:10]
    else:
        continue            # Sometimes data can come in incomplete and crash the program becasue of the spliting so this will avoid that
    datalist = data.split("|")
    temp = datalist[0]
    humid = datalist[1]
    
    dt = datetime.now()
    dbtime = dt.strftime("%Y-%m-%d %H:%M:%S")

    # Place data into db every 10 minutes
    cursor.execute("INSERT INTO temphumid(temperature, humidity, date) VALUES (?,?,?)", (temp, humid, dbtime))
    db.commit()

    print(datalist)
    print(dbtime)
    time.sleep(590)
    arduino.flushInput()

cursor.close()
