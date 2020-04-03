import time
from termcolor import colored, cprint
import connector
import read_
import data

def metering(prev_save, date_time):
    name_ = "water"
    snmpget130 = data.snmpget130
    str_snmp = snmpget130 + "2.3.1.31.6.0"
    impulse = read_.state(str_snmp, name_)
    print "\033[30;0H-------'WATER METERING'------------------------------"
    print "\033[31;0H Impulse from water meter = %s " % colored(impulse, 'white', 'on_blue', ['bold'])
    table_name = "water"
    tabledata = connector.get_table(table_name)
    water_data = str(tabledata[2]) + " m3 on " + str(tabledata[1])
    
    print "\033[32;0H Water meter display: " , colored(str(water_data),'white', 'on_blue', ['bold'])

    if impulse > 2 and prev_save == 0:
        prev_save = 1
        water_data = connector.save_water_data(prev_save, date_time)
        print "\033[33;0H Updating Meter_Value record:  %s" % colored(water_data, 'grey', 'on_green')
        time.sleep(3)
        print "\033[33;0H                                                  "
    
    #Stop saving water_data
    elif impulse > 2 and prev_save == 1:
        prev_save = 1
    
    #Start saving water_data.
    elif impulse < 2 and prev_save == 1:
        prev_save = 0
    
    #Start saving "0" in water_data.
    elif impulse < 2 and prev_save == 0:
        prev_save = 0    
    
    return prev_save


if __name__ == '__main__':
    prev_save = 0
    impulse = 3
    import datetime
    date_time = data.date_time
    metering(prev_save, date_time)
