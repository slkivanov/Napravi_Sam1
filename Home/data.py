import mysql.connector
from mysql.connector import Error
import datetime
import time
db_connect = {'host' :'localhost', 'database' : 'mydb', 'user': 'root', 'password' : '1'}
snmpget129 = "snmpget -t1 -r1000 -v1 -c private 192.168.0.129 1.3.6.1.4.1.19865."
snmpget130 = "snmpget -t1 -r1000 -v1 -c private 192.168.0.130 1.3.6.1.4.1.19865."
snmpset129 = "snmpset -t1 -r1000 -v1 -c private 192.168.0.129 1.3.6.1.4.1.19865."
snmpset130 = "snmpset -t1 -r1000 -v1 -c private 192.168.0.130 1.3.6.1.4.1.19865."

add_temp = ("INSERT INTO temp ""(date_time, s1_boiler_input,"
        "s2_boiler_output, s3_boiler_top, s4_boiler_bottom, s5_boiler_status,"
        "s6_pump_status, s0_pump_status, k1_kotel_output, k2_boiler_input,"
        " k3_boiler_top, k4_boiler_bottom, k5_boiler_status, k6_pump_status) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)")
add_set = ("INSERT INTO commands ""(set_s5_boiler_status, set_s6_pump_status,"
        " set_k5_boiler_status, set_k6_pump_status, date_time) "
            "VALUES (%s, %s, %s, %s, %s)")
 
def mysql_connector(): # Data to connect database tables in  'mydb'
    conn = mysql.connector.connect(host = 'localhost', database = 'mydb', 
        user = 'root', password = '1')
    return conn
    
def date_time():
    date_time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    return date_time

def get_time(): # Gets current time_ ----------------------------------
    time_ = datetime.datetime.now().time()
    time_ = str(time_)
    time_ = int(time_[0:2] + time_[3:5])
    return time_
       
def get_date(): # Gets current date -----------------------------------
    date_ = datetime.datetime.now().date()   
    date_ = str(date_)
    date_ = int(date_[5:7] + date_[8:10])
    return date_

def sum_win_time(date_): # Summer and Winter time --------------------------
    if 330 < date_ < 1101:
        start_day = 700
        end_day = 2300
        print "Now is Summer time: ", "start_day: %s" % start_day, ", end_day: %s" % end_day
    else:
        start_day = 600
        end_day = 2200
        print "Now is Winter time: ", "start_day: %s" % start_day, ", end_day: %s" % end_day
    return start_day, end_day
    
