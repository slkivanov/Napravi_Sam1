import connector
import logic
import read_
import data
snmpget130 = data.snmpget130
snmpset130 = data.snmpset130

def irigation(time_):
  while True:
    # Reads data from table_name "valves"    
    valve1_state = read_.state(str_snmp = snmpget130 + "1.2.2.1.0", name_="valve1_state")
    valve2_state = read_.state(str_snmp = snmpget130 + "1.2.2.2.0", name_="valve2_state")
    valve3_state = read_.state(str_snmp = snmpget130 + "1.2.2.3.0", name_="valve3_state")
    valve4_state = read_.state(str_snmp = snmpget130 + "1.2.2.4.0", name_="valve4_state")  

    # Reads data from table_name "set_valves"
    table_name = "set_valves"
    tabledata = connector.get_table(table_name)
    set_valve1 = tabledata[1]
    set_valve2 = tabledata[2]
    set_valve3 = tabledata[3]
    set_valve4 = tabledata[4]
    start_time = tabledata[6]
    duration = tabledata[7]
    print "\033[34;0H----------'IRIGATION'---------------------     "
    print "Valve states - V1 to V4 are: %s" % set_valve1, set_valve2, \
    set_valve3, set_valve4
    print "Time is: %s" % time_, ", V1 start time: %s" % start_time, ", Duration = %s" %  duration

    # set_valves --------------------------------------------------
    valve1_state = logic.valves(snmpset130, time_, start_time, \
    end_time = start_time + duration, \
    set_valve = set_valve1, valve_state = valve1_state, ID = "1")
    if valve1_state == 1:
        connector.save_valve_states(1, 0, 0, 0)
    elif valve1_state == 0:
        connector.save_valve_states(0, 0, 0, 0)
        
    valve2_state = logic.valves(snmpset130, time_, start_time = start_time + duration, \
    end_time = start_time +(duration *2), \
    set_valve = set_valve2, valve_state = valve2_state, ID = "2")
    if valve2_state == 1:
        connector.save_valve_states(0, 1, 0, 0)
    elif valve2_state == 0:
        connector.save_valve_states(0, 0, 0, 0)
        
    valve3_state = logic.valves(snmpset130, time_, start_time = start_time +(duration *2), \
    end_time = start_time +(duration *3), \
    set_valve = set_valve3, valve_state = valve3_state, ID = "3")
    if valve3_state == 1:
        connector.save_valve_states(0, 0, 1, 0)
    elif valve3_state == 0:
        connector.save_valve_states(0, 0, 0, 0)
        
    valve4_state = logic.valves(snmpset130, time_, start_time = start_time +(duration *3), \
    end_time = start_time +(duration *4), \
    set_valve = set_valve4, valve_state = valve4_state, ID = "4")
    if valve4_state == 1:
        connector.save_valve_states(0, 0, 0, 1)
    elif valve4_state == 0:
        connector.save_valve_states(0, 0, 0, 0)
    return valve1_state
