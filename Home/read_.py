import subprocess

def temperatures(str_snmp, correction, name_): # Measuring temperatures
    x=1
    pico_celsius_avrg=0
    while x < 21:
        read_snmp = subprocess.check_output([str_snmp], shell=True)
    # Converting to voltage [V]-------------------------------------------
        pico_voltage = (float(read_snmp[41:45])/1023)*3.3
    # Converting to temperature [C]---------------------------------------
        pico_celsius = ((pico_voltage-0.5)*100)+ correction
        pico_celsius_avrg = float(pico_celsius_avrg + pico_celsius)
        pico_celsius = pico_celsius_avrg/x
        x+=1
    return round(pico_celsius,1)

def state(str_snmp, name_):# Reads pump, heater and valve statuses
    x=0
    state_avrg=0
    while x < 2:
        read_snmp = subprocess.check_output([str_snmp], shell=True)
        if name_ == "water":
            state = read_snmp[44:48]
            state = (float(state[0:4])/1024)*3.3
        else:
            state = read_snmp[41:45]
            state = float(state[0:4])
        state_avrg = state_avrg + state
        x+=1
        state_avrg=str(state_avrg)
        state_avrg=float(state_avrg[0:4])
        state = round((float(state_avrg/x)),1)          
    return round(state,2)
 

