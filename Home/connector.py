import time
from termcolor import colored, cprint
import data
 
def get_table(table_name): # Reads data from database "mydb"
    conn = data.mysql_connector()
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            if table_name <> "water":
                cursor.execute("SELECT * FROM " + table_name + " ORDER BY id DESC LIMIT 1")
            else:
                cursor.execute("SELECT * FROM water WHERE water_data > 0 ORDER BY id DESC LIMIT 1")
            tabledata = cursor.fetchone()
           
        cursor.close()
    except Error as e:
        print(e), "There is a problem !!!"
    finally:
        conn.close()
        return tabledata

def save_table(add_value, data_temp): # Saves data to db "mydb"
    conn = data.mysql_connector()
    try:
        if conn.is_connected():
            print "|==========================================|"
            cursor = conn.cursor()
            cursor.execute(add_value, data_temp) # Saving new temperatures
            conn.commit()
            cursor.close()
            print "|Updating:s1_boiler_input:  %s" % colored(data_temp[1], 'white', 'on_yellow', ['bold'])
            print "|         s2_boiler_output: %s" % colored(data_temp[2], 'white', 'on_green', ['bold'])
            print "|         s3_boiler_top:    %s" % colored(data_temp[3], 'white', 'on_red', ['bold'])
            print "|         s4_boiler_bottom: %s" % colored(data_temp[4], 'white', 'on_blue', ['bold'])
            print "|         s5_boiler_status:  %s" % colored(data_temp[5], 'white', 'on_cyan', ['bold'])
            print "|         s6_pump_status:    %s" % colored(data_temp[6], 'white', 'on_cyan', ['bold'])
            print "|         s0_pump_status:    %s" % colored(data_temp[7], 'white', 'on_blue', ['bold'])
            print "|         k1_kotel_output:  %s" % colored(data_temp[8], 'white', 'on_magenta', ['bold'])
            print "|         k2_boiler_input:  %s" % colored(data_temp[9], 'white', 'on_yellow', ['bold'])
            print "|         k3_boiler_top:    %s" % colored(data_temp[10], 'white', 'on_red', ['bold'])
            print "|         k4_boiler_bottom: %s" % colored(data_temp[11], 'white', 'on_blue', ['bold'])
            print "|         k5_boiler_status:  %s" % colored(data_temp[12], 'white', 'on_cyan', ['bold'])
            print "|         k6_pump_status:    %s" % colored(data_temp[13], 'white', 'on_cyan', ['bold'])
            print "|=========================================|"
            print ""
    except Error as e:
        print(e), "There is a problem !!!"
    finally:
        conn.close()
        
def save_water_data(prev_save, date_time):
    conn = data.mysql_connector()
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            if prev_save == 1:
                cursor.execute("SELECT * FROM water WHERE water_data > 0 ORDER BY id DESC LIMIT 1")
                last_row = cursor.fetchone()
                water_data = last_row[2]
                water_data = water_data + 0.01 
            # Saves "0" in "water_data"
            if prev_save == 0:
                cursor.execute("SELECT * FROM water ORDER BY id DESC LIMIT 1")
                last_row = cursor.fetchone()
                water_data = 0
                
            add_water = ("INSERT INTO water (date_time, water_data) VALUES (%s, %s)")
            water_value = (date_time, water_data)

        # Saving new data-----------------------------------
            cursor.execute(add_water, water_value)
            conn.commit()
            cursor.close()
        print "Updating Meter_Value record:  %s" % colored(water_data, 'grey', 'on_green')
        time.sleep(1)
        print "                                          "
    except Error as e:
        print(e), "There is a problem !!!"
    finally:
        conn.close()
    return water_data

def save_valve_states(valve1_state,valve2_state,valve3_state,valve4_state):
    conn = data.mysql_connector()
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            add_valves = ("INSERT INTO valves ""(date_time, valve1_state, valve2_state, valve3_state, valve4_state)"
                        "VALUES (%s, %s, %s, %s, %s)")
            date_time = data.date_time()
            data_valves = (date_time, valve1_state,valve2_state, valve3_state, valve4_state)

        # Saving new valve_statuses---------------------------------
            cursor.execute(add_valves, data_valves)
            conn.commit()
            cursor.close()
    except Error as e:
        print(e), "There is a problem !!!"
    finally:
        conn.close()
