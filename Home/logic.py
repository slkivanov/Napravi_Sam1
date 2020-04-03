import subprocess
from termcolor import colored, cprint
import time
import data

snmpset129 = data.snmpset129
snmpset130 = data.snmpset130

def boiler_commands(name_, boiler_top, boiler_bottom, boiler_status):
    print "Top = %s," % boiler_top, "Bottom = %s" % boiler_bottom
    if boiler_status == 1 and name_ == "Solar":
        Boiler_ON = subprocess.check_output([snmpset129 + "1.2.2.1.0 i 1"], shell=True)
    elif boiler_status == 0 and name_ == "Solar":
        Boiler_OFF = subprocess.check_output([snmpset129 + "1.2.2.1.0 i 0"], shell=True)
    elif boiler_status == 1 and name_ == "Kotel":
        Boiler_ON = subprocess.check_output([snmpset130 + "1.2.2.5.0 i 1"], shell=True)
    elif boiler_status == 0 and name_ == "Kotel":
        Boiler_OFF = subprocess.check_output([snmpset130 + "1.2.2.5.0 i 0"], shell=True)

def pump_commands(s6_pump_status):
    if s6_pump_status == 1:
        pump_on = subprocess.check_output([snmpset129 + "1.2.2.2.0 i 1"], shell=True)
    elif s6_pump_status == 0:
        pump_Off = subprocess.check_output([snmpset129 + "1.2.2.2.0 i 0"], shell=True)

# Switching Circulation Pump according table_name "commands"-----------------         
def pump(time_, start_day, end_day, set_s6_pump_status, 
                s6_pump_status, s3_boiler_top, k3_boiler_top, 
                k1_kotel_output, t1_P1M_tSB_Hi, t2_P1A_tSB_Hi, 
                t3_P1A_tKB_Hi, t4_Dev_tKB_tSB_Hi, t5_P0A_tSB_L,
                s5_boiler_status, k5_boiler_status, end_sun):
    # Manual CONTROL  ----------------------------------------------
    if set_s6_pump_status == 0:
        if start_day <= time_ < end_sun and \
            k3_boiler_top < s3_boiler_top >= t1_P1M_tSB_Hi \
            and (s3_boiler_top - k3_boiler_top) > t4_Dev_tKB_tSB_Hi:
            print"Circul_pump_Hand1_off: Pump " + colored('On', 'grey', 'on_green') + " (by COMPUTER)"
            pump_commands(s6_pump_status = 1.0)
        else:
            print"Circul_pump_Hand2_Off: Pump " + colored('Off', 'white', 'on_red') + " (by manual command)"
            pump_commands(s6_pump_status = 0.0)  
    elif  set_s6_pump_status == 1:
        # Heating Kotel Boiler by Solar Boiler-----------------------------
        if s5_boiler_status == 0.0 and start_day <= time_ < end_sun and \
            k3_boiler_top < s3_boiler_top >= t1_P1M_tSB_Hi:# \ 
            #and (s3_boiler_top - k3_boiler_top) > t4_Dev_tKB_tSB_Hi:
            print"Circul_pump_Hand3: Pump " + colored('On', 'grey', 'on_green') + " (by manual command)"
            pump_commands(s6_pump_status = 1.0)
        # Heating Solar Boiler from Kotel Boiler when Kotel is working--
        elif s5_boiler_status == 0.0 and (k3_boiler_top - s3_boiler_top) > t4_Dev_tKB_tSB_Hi \
            and k1_kotel_output > k3_boiler_top >= t3_P1A_tKB_Hi:
            print"Circul_pump_Hand4: Pump " + colored('On', 'grey', 'on_green') + " (by manual command)"
            pump_commands(s6_pump_status = 1.0)
        else:
            print"Circul_pump_Hand5_Off: Pump " + colored('Off', 'white', 'on_red')
            pump_commands(s6_pump_status = 0.0)
    # PC CONTROL ---------------------------------------------------   
    elif set_s6_pump_status == 2:
        # Heating Kotel Boiler by Solar Boiler-----------------------------
        if s5_boiler_status == 0.0 and start_day <= time_ < end_sun and \
            k3_boiler_top < s3_boiler_top > t2_P1A_tSB_Hi \
            and (s3_boiler_top - k3_boiler_top) > t4_Dev_tKB_tSB_Hi:
            print"Circul_pump_Auto1: Pump " + colored('On', 'grey', 'on_green') + " (by COMPUTER)"
            pump_commands(s6_pump_status = 1.0)
    # Heating Solar Boiler from Kotel Boiler when Kotel is working--
        elif s5_boiler_status == 0.0 and (k3_boiler_top - s3_boiler_top) > t4_Dev_tKB_tSB_Hi \
            and k1_kotel_output > k3_boiler_top >= t3_P1A_tKB_Hi :
            print"Circul_Pump_Auto2: Pump " + colored('On', 'grey', 'on_green') + " (by COMPUTER)"
            pump_commands(s6_pump_status = 1.0)
        elif s6_pump_status == 1 and (s3_boiler_top - k3_boiler_top) < t4_Dev_tKB_tSB_Hi \
                or s3_boiler_top <= t5_P0A_tSB_L or time_ > end_sun:
            print"Circul_Pump_Auto3: Pump " + colored('Off', 'white', 'on_red') + " (by COMPUTER)"
            pump_commands(s6_pump_status = 0.0)
        else:
            print"Circul_pump_Auto4_Off: Pump " + colored('Off', 'white', 'on_red')
            pump_commands(s6_pump_status = 0.0)
    else:
        print"Circul_Pump " + colored('Off', 'white', 'on_red')
        pump_commands(s6_pump_status = 0.0)
    return s6_pump_status

# Switching boilers according table_name "commands"------
def boilers(time_, name_, start_day, start_heat, end_day, start_tmax,
                set_boiler_status, boiler_status, pump_status, 
                boiler_top, boiler_bottom, t6_B1M_tB_L, t10_prev_heat, t8_B1A_tB_L):
    if pump_status == 1:
        print name_ + " Boiler is 'Off' because PUMP is 'On'"
        boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 0.0)
    else:
        # Manual CONTROL -----------------------------------------------
        if set_boiler_status == 0:
            print name_ + " Boiler is " + colored('OFF', 'white', 'on_red')
            boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 0.0)
        elif  set_boiler_status == 1:
            if start_day <= time_ <= 2400 and boiler_bottom < t6_B1M_tB_L:
                print name_ + " Boiler_Man1_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than %s" % t6_B1M_tB_L, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            elif 0 <= time_ < start_tmax and boiler_bottom < t10_prev_heat:
                print name_ + " Boiler_Man2_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than  %s" % t10_prev_heat, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            elif start_day > time_ >= start_tmax and boiler_bottom < t8_B1A_tB_L:
                print name_ + " Boiler_Man3_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than  %s"% t8_B1A_tB_L, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            else:
                print name_ + " Boiler_Man4_" + colored('OFF', 'white', 'on_red') + ": Boiler Off."
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 0.0)
        
        # PC CONTROL----------------------------------------------------       
        elif set_boiler_status == 2.0:
            # 03.12.2018 Switch Heater if bottom is low requirement temperature, between 19:00 and 2 hours before start of day tariff time_; 
            if start_heat <= time_ <= 2400 and boiler_bottom < t10_prev_heat:
                print name_ + " Boiler_PrevHeat_Auto1_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than  %s" % t10_prev_heat, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            elif 0 <= time_ < start_tmax and boiler_bottom < t10_prev_heat:
                print name_ + " Boiler_PrevHeat_Auto2_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than  %s" % t10_prev_heat, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            elif start_day > time_ >= start_tmax and boiler_bottom < t8_B1A_tB_L:
                print name_ + " Boiler_Auto3_" + colored('ON', 'grey', 'on_green') + ": Boiler temperature is low than  %s"% t8_B1A_tB_L, "C"
                boiler_commands(name_, boiler_top, boiler_bottom, boiler_status = 1.0)
            else:
                boiler_status = 0.0
                if start_heat <= time_ <= 2400 or 0 <= time_ < start_tmax:
                    print name_ + " Boiler_PrevHeat_Auto4_" + colored('OFF', 'white', 'on_red')  + ": Boiler temperature is Hi than %s" % t10_prev_heat, "C"
                    boiler_commands(name_, boiler_top, boiler_bottom, boiler_status)
                elif start_day > time_ >= start_tmax:
                    print name_ + " Boiler_Auto5_" + colored('OFF', 'white', 'on_red') + ": Boiler temperature is Hi than %s" % t8_B1A_tB_L, "C"
                    boiler_commands(name_, boiler_top, boiler_bottom, boiler_status)
                else:
                   print name_ + " Boiler_Auto6_" + colored('OFF', 'white', 'on_red')
                   boiler_commands(name_, boiler_top, boiler_bottom, boiler_status)
    return boiler_status

def valves(snmpset130, time_, start_time, end_time, set_valve, valve_state, ID):         
    if set_valve == 1 and valve_state == 0.0:
        valve_ON = subprocess.check_output([snmpset130 + "1.2.2." + ID + ".0 i 1"], shell=True)
        print  "Valve" + ID + " is switched on manually!!!    "
        valve_state = 1
        time.sleep(1)  
        return valve_state 
    elif set_valve == 0 and valve_state == 1.0:
        valve_off = subprocess.check_output([snmpset130 + "1.2.2." + ID + ".0 i 0"], shell=True)
        print  "Valve" + ID + " is switched off manually!!!   "
        valve_state = 0
        time.sleep(1)
        return valve_state  
    elif set_valve == 2 and valve_state == 0.0 and time_ >= start_time and time_ < end_time:
        valve_ON = subprocess.check_output([snmpset130 + "1.2.2." + ID + ".0 i 1"], shell=True)
        print  "Valve" + ID + " is switched", colored('ON', 'grey', 'on_green'), " by computer!!! "
        valve_state = 1
        time.sleep(1)
        return valve_state    
    elif set_valve == 2 and valve_state == 1 and time_ >= end_time:
        valve_off = subprocess.check_output([snmpset130 + "1.2.2." + ID + ".0 i 0"], shell=True)
        print  "Valve" + ID + " is switched off by computer!  !!"
        valve_state = 0
        time.sleep(1)
        return valve_state
    elif valve_state == 1.0:
        print  "Valve" + ID + " is switched", colored('ON', 'grey', 'on_green'), '                  '
        return
    else:
        print ' ', colored("No", 'white', 'on_red', ['bold']), "action to valve " + ID + "                      "
        return
