#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import time
from termcolor import colored, cprint
import logic
import connector
import read_
import dbbackup
import water_meter
import irigation
import data
file_name = sys.argv[0]
dbbackup.dbbackup(2359) # On start, saves just one time database 'mydb' 

def delay(delaing):
    while delaing > 0:
        print "Remaining %s" % delaing, " seconds to start of program '" + file_name + "'"
        time.sleep(1)
        os.system("clear")
        delaing -= 1

def run():
    os.system("clear")
    delay(delaing = 120)
    
    prev_save = 0
    last_imp = 0
    
    while True:
        try:
            print "Starting 'Solar and Heating systems' - " + "'" + file_name + "'" 
            print "============================================================="      
            snmpget129 = data.snmpget129
            snmpget130 = data.snmpget130
            s1_boiler_input = read_.temperatures(str_snmp = snmpget129 + "1.2.3.1.0", correction=0, name_="s1_boiler_input ")
            s2_boiler_output = read_.temperatures(str_snmp = snmpget129 + "1.2.3.2.0", correction=0, name_="s2_boiler_output")
            s3_boiler_top = read_.temperatures(str_snmp = snmpget129 + "1.2.3.5.0", correction=1.2, name_="s3_boiler_top   ")
            #s4_boiler_bottom = read_.temperatures(str_snmp = snmpget129 + "1.2.3.6.0", correction=0.5, name_="s4_boiler_bottom")
            s4_boiler_bottom = "10.0"
            s5_boiler_status = read_.state(str_snmp = snmpget129 + "1.2.2.1.0", name_="s5_boiler_status")
            s6_pump_status = read_.state(str_snmp = snmpget129 + "1.2.2.2.0", name_="s6_pump_status  ")
            s0_pump_status = read_.state(str_snmp = snmpget129 + "1.2.3.7.0", name_="s0_pump_status  ")
            k1_kotel_output = read_.temperatures(str_snmp = snmpget130 + "1.2.3.3.0", correction=-0.7, name_="k1_kotel_output ")
            k2_boiler_input = read_.temperatures(str_snmp = snmpget130 + "1.2.3.5.0", correction=1.6, name_="k2_boiler_input ")
            k3_boiler_top = read_.temperatures(str_snmp = snmpget130 + "1.2.3.6.0", correction=3+4, name_="k3_boiler_top   ")
            k4_boiler_bottom = read_.temperatures(str_snmp = snmpget130 + "1.2.3.4.0", correction=1.7, name_="k4_boiler_bottom")
            k5_boiler_status = read_.state(str_snmp = snmpget130 + "1.2.2.5.0", name_="k5_boiler_status")
            k6_pump_status = read_.state(str_snmp = snmpget130 + "1.2.2.6.0", name_="k6_pump_status  ")

        # Gets current date_ and time_  -------------------------------
            time_ = data.get_time()             
            date_ = data.get_date()   
            print "time_ = " , time_ , " date_ = ", date_
            
        # Summer and Winter time ---------------------------------------
            sum_win_time = data.sum_win_time(date_)
            sum_win_time = str(sum_win_time)
            start_day = sum_win_time[1:4]
            end_day = sum_win_time[6:10]
        # Uncomment 'time' to save database 'mydb'
            #time_ = 2358 
        
        # Reads data from table_name "commands"
            table_name = "commands"
            tabledata = connector.get_table(table_name)
            set_s5_boiler_status = tabledata[1]
            set_s6_pump_status = tabledata[2]
            set_k5_boiler_status = tabledata[3]
            set_k6_pump_status = tabledata[4]

        # Reads data from table_name "settings"
            table_name = "settings"
            tabledata = connector.get_table(table_name)
            t1_P1M_tSB_Hi = tabledata[1]
            start_day = tabledata[2]
            end_day = tabledata[3]
            t2_P1A_tSB_Hi = tabledata[4]      
            end_sun = tabledata[5]
            t3_P1A_tKB_Hi = tabledata[6]
            t4_Dev_tKB_tSB_Hi = tabledata[7]
            t5_P0A_tSB_L = tabledata[8]
            t6_B1M_tB_L = tabledata[9]
            start_tmax = tabledata[10]
            t8_B1A_tB_L = tabledata[11]
            t9_B0A_tB_Hi = tabledata[12]
            t10_prev_heat = tabledata[14]
            start_heat = tabledata[15]
        
        # Visualisation of System States    ================================        
            print "|==========================================|"
            print "|     Visualisation of System States       |"
            print "|==========================================|"
        
        # State of Solar Pump (s6_pump_status) according table_name "temp"----
            if s0_pump_status > (0.75*1023):
                s0_pump_status = "0"
                print "Solar pump is " + colored('Off', 'white', 'on_red')   
            else:
                s0_pump_status = "5"
                print "Solar pump is " + colored('On', 'grey', 'on_green')
        """===================================================================
         Testing  system  logic's
            s4_boiler_bottom = 20  #  New values
            k4_boiler_bottom = 50  # for testing 
            time_ = 2400           #  of logic
            print time_            #
            print "set_s5_boiler_status = %s" % set_s5_boiler_status
            print "set_k5_boiler_status = %s" % set_k5_boiler_status
            print "   "
        ==================================================================="""
            # Checks pump state and switchs on_off if necessary 
            pump_status = logic.pump(time_, start_day, end_day, set_s6_pump_status, 
                    s6_pump_status, s3_boiler_top, k3_boiler_top, 
                    k1_kotel_output, t1_P1M_tSB_Hi, t2_P1A_tSB_Hi, 
                    t3_P1A_tKB_Hi, t4_Dev_tKB_tSB_Hi, t5_P0A_tSB_L,
                    s5_boiler_status, k5_boiler_status, end_sun)
            s6_pump_status = pump_status

        # Checks boiler state and switchs heaters if necessary 
            name_ = "Solar"
            boiler_status = logic.boilers(time_, name_, start_day, start_heat, end_day, start_tmax,
                                set_s5_boiler_status, s5_boiler_status, s6_pump_status, 
                                s3_boiler_top, s4_boiler_bottom, t6_B1M_tB_L, t10_prev_heat, t8_B1A_tB_L)
            
            s5_boiler_status  = boiler_status
            
            name_ = "Kotel"
            boiler_status = logic.boilers(time_, name_, start_day, start_heat, end_day, start_tmax,
                                set_k5_boiler_status, k5_boiler_status, s6_pump_status,
                                k3_boiler_top, k4_boiler_bottom, t6_B1M_tB_L, t10_prev_heat, t8_B1A_tB_L)
            k5_boiler_status = boiler_status                   

        # Saves data in table_name "temp"
            date_time = data.date_time()
            add_temp = data.add_temp
            
            data_temp = (date_time, s1_boiler_input,s2_boiler_output,s3_boiler_top,
            s4_boiler_bottom,s5_boiler_status,s6_pump_status, s0_pump_status,
            k1_kotel_output, k2_boiler_input, k3_boiler_top, k4_boiler_bottom,
            k5_boiler_status, k6_pump_status)
            connector.save_table(add_temp, data_temp)
        
        # Saves "0" in table_name "water" every 180 seconds 
            if prev_save == 0 and last_imp == 0:
                connector.save_water_data(prev_save, date_time)
            elif prev_save == 0 and last_imp >170 :
                connector.save_water_data(prev_save, date_time)
            last_imp = 0
        # Saves database "mydb" in backup_path = '/var/www/html/data/'------  
            dbbackup.dbbackup(time_)

            for c in range(1,180):
                #Checks for water_meter impulse
                prev_save =  water_meter.metering(prev_save, data.date_time())
                if prev_save == 1:
                    last_imp = last_imp + prev_save

                #Checks irigation system
                tabledata = connector.get_table(table_name = "set_valves")
                duration = tabledata[7]
                
                if duration <> 0: # if duration = 0  irigation rows and values will be hiden
                    irigation.irigation(time_ = data.get_time())
                    y_pos = '42'
                    print  "\033[" + y_pos + ";0H", \
                    colored("Awaiting for another cycle after 3 min.: ", 'white', 'on_blue', ['bold']), \
                    colored(c, 'white', 'on_red', ['bold']), last_imp
                else:
                    y_pos = '34'
                    for d in range (35,43):
                        print  "\033[" + str(d) + ";0H                                                       "
                    print  "\033[" + y_pos + ";0H", \
                    colored("Awaiting for another cycle after 3 min.: ", 'white', 'on_blue', ['bold']), \
                    colored(c, 'white', 'on_red', ['bold']), last_imp
                time.sleep(1)
            os.system("clear")
        except Exception:
            sys.exc_clear()
        finally:
            os.system("clear")           
run()
