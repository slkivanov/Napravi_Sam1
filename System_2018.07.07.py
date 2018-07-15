#!/home/pi

# 15.05.2018_Inidication state of pump and heaters in green or in red;
# 24.05.2018_ New pico with 8 relaies: 1-st to 4-th for water relaies, 5-th for 'K5_BoilerStatus';
# 27.05.2018_Added status ot solar pump  S0_PumpStatus; Added record S0_PumpStatus to table 'temp';
# 03.06.2018_Reading water meter by "graph_water.php" and display value in "sceme.php"; 
# 03.06.2018_Conecting water meter impuls (1 imp / 10 L) to input "Alarm" on "Pico IP";
# 14.06.2018_Saving database in .gz format;
# 06.07.2018_Comment some "print" position to zoom display and rename PUMP_ON_OFF to Status_Pump_Heater;
# 07.07.2018_HAND CONTROLING of heateres - printing separate answers because hand command "off" or circul. pump is "on";
# 08.08.2018_ Resize and format output labels;
 
import os
import subprocess
import time
import datetime
import math
import mysql.connector
from mysql.connector import Error
from termcolor import colored, cprint
Delaing = 120
File_name = "System_2018.07.07.py"
while Delaing > 0:
    print "Remaining %s" % Delaing, " seconds to start of program '" + File_name + "'"
    time.sleep(1)
    os.system("clear")
    Delaing -= 1
# ======================================================================

# Measuring temperatures 20-times by PicoIP
def read_Solar_Kotel(str_snmp, correction, name, posy): 
    x=1
    Pico_Celsius_avrg=0
    while x < 21:
		Read_NTimes = subprocess.check_output([str_snmp], shell=True)
    # Changing to voltage [V]-------------------------------------------
		Pico_Voltage = (float(Read_NTimes[41:45])/1023)*3.3
    # Changing to temperature [C]---------------------------------------
		Pico_Celsius = ((Pico_Voltage-0.5)*100)+ correction
		print "\033[" + posy + ";0H", "|Reading %s "  % name, colored(x, 'white', 'on_blue'), colored(round(Pico_Celsius,1), 'white', 'on_red')
		Pico_Celsius_avrg = float(Pico_Celsius_avrg + Pico_Celsius)
		Pico_Celsius = Pico_Celsius_avrg/x
		print "\033[" + posy + ";35H", colored(round(Pico_Celsius,2), 'white', 'on_red')
		#time.sleep(1)
		x+=1
    print "\033[" + posy + ";2H|Reading %s "  % name, "Average:", colored(round(Pico_Celsius,1), 'grey', 'on_green', ['bold']) + " "
    return round(Pico_Celsius,1)

# Reading pump and heater status 2-times by PicoIP ---------------------
def read_Status_Pump_Heater(str_snmp, name, posy): 
	x=0
	Status_avrg=0
	while x < 2:
		Read_NTimes = subprocess.check_output([str_snmp], shell=True)
		Status_Pump_Heater = Read_NTimes[41:45]
		Status_Pump_Heater = float(Status_Pump_Heater[0:4])
		Status_avrg = Status_avrg + Status_Pump_Heater
		print "\033[" + posy + ";0H", "|Reading %s "  % name, colored(x, 'white', 'on_blue'), colored(round(Status_Pump_Heater,0), 'white', 'on_red')
		#time.sleep(1)
		x+=1
	Status_avrg=str(Status_avrg)
	Status_avrg=float(Status_avrg[0:4])
	Status_Pump_Heater = round((float(Status_avrg/x)),1)
	print "\033[" + posy + ";2H|Reading %s "  % name, "Average: ", colored(Status_Pump_Heater, 'white', 'on_blue', ['bold'])
	return Status_Pump_Heater

# Backup data base------------------------------------------------------
def dbBackup():
	DB_USER = 'root'
	DB_USER_PASSWORD = '1'
	DB_NAME = 'mydb'
	BACKUP_PATH = '/var/www/html/Data/'

	# Getting current datetime to create separate backup folder like "20171231-071334".
	DATETIME = time.strftime('%Y.%m.%d-%H_%M_%S')
	TODAYBACKUPPATH = BACKUP_PATH + DATETIME

	# Checking if backup folder already exists or not. If not exists will create it.
	print "creating backup folder"
	if not os.path.exists(TODAYBACKUPPATH):
		os.makedirs(TODAYBACKUPPATH)

	# Code for checking if you want to take single database backup.
		print "Starting backup of database " + '"' + DB_NAME+ '"'
		dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " | " + " gzip "+ " > " + TODAYBACKUPPATH + "/" + DB_NAME + ".sql.gz"
		os.system(dumpcmd)

		print "Backup script completed"
		print "Your backups has been created in '" + TODAYBACKUPPATH + "' directory"

# main program entry point==============================================
def run(): 
	os.system("clear")
	#dbBackup()
	while True:  
		print "'" + File_name + "' Start measuring of Solar and Heating systems"
		print "========================================="
		snmpGet129 = "snmpget -t1 -r1000 -v1 -c private 192.168.0.129 1.3.6.1.4.1.19865."
		snmpGet130 = "snmpget -t1 -r1000 -v1 -c private 192.168.0.130 1.3.6.1.4.1.19865."
		snmpSet129 = "snmpset -t1 -r1000 -v1 -c private 192.168.0.129 1.3.6.1.4.1.19865."
		snmpSet130 = "snmpset -t1 -r1000 -v1 -c private 192.168.0.130 1.3.6.1.4.1.19865."
		S1_BoilerInput = read_Solar_Kotel(posy="4", str_snmp = snmpGet129 + "1.2.3.1.0", correction=2.4, name="S1_BoilerInput ")
		S2_BoilerOutput = read_Solar_Kotel(posy="5", str_snmp = snmpGet129 + "1.2.3.2.0", correction=1.5, name="S2_BoilerOutput")
		S3_BoilerTop = read_Solar_Kotel(posy="6", str_snmp = snmpGet129 + "1.2.3.5.0", correction=4.5, name="S3_BoilerTop   ")
		S4_BoilerBottom = read_Solar_Kotel(posy="7", str_snmp = snmpGet129 + "1.2.3.6.0", correction=2.5, name="S4_BoilerBottom")
		S5_BoilerStatus = read_Status_Pump_Heater(posy="8", str_snmp = snmpGet129 + "1.2.2.1.0", name="S5_BoilerStatus")
		S6_PumpStatus = read_Status_Pump_Heater(posy="9", str_snmp = snmpGet129 + "1.2.2.2.0", name="S6_PumpStatus  ")
		S0_PumpStatus = read_Status_Pump_Heater(posy="10", str_snmp = snmpGet129 + "1.2.3.7.0", name="S0_PumpStatus  ")
		K1_KotelOutput = read_Solar_Kotel(posy="11", str_snmp = snmpGet130 + "1.2.3.3.0", correction=-0.7, name="K1_KotelOutput ")
		K2_BoilerInput = read_Solar_Kotel(posy="12", str_snmp = snmpGet130 + "1.2.3.5.0", correction=1.6, name="K2_BoilerInput ")
		K3_BoilerTop = read_Solar_Kotel(posy="13", str_snmp = snmpGet130 + "1.2.3.6.0", correction=3+4, name="K3_BoilerTop   ")
		K4_BoilerBottom = read_Solar_Kotel(posy="14", str_snmp = snmpGet130 + "1.2.3.4.0", correction=1.7, name="K4_BoilerBottom")
		K5_BoilerStatus = read_Status_Pump_Heater(posy="15", str_snmp = snmpGet130 + "1.2.2.5.0", name="K5_BoilerStatus")
		K6_PumpStatus = read_Status_Pump_Heater(posy="16", str_snmp = snmpGet130 + "1.2.2.6.0", name="K6_PumpStatus  ")
        
# Reading data from database "mydb"-------------------------------------
	# Connecting to database "mydb"  -----------------------------------
		try:
			conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='1')
			if conn.is_connected():
				#print "Connected to 'mydb' database, table 'commands'"
				cursor = conn.cursor()
				cursor.execute("SELECT * FROM commands ORDER BY id DESC LIMIT 1")
				last_row = cursor.fetchone()
				#print last_row
				Set_S5_BoilerStatus = last_row[1]
				Set_S6_PumpStatus = last_row[2]
				Set_K5_BoilerStatus = last_row[3]
				Set_K6_PumpStatus = last_row[4]
				#print "-----------------------------"
				
				#print "Connected to 'mydb'database, table 'settings'"
				cursor = conn.cursor()
				cursor.execute("SELECT * FROM settings ORDER BY id DESC LIMIT 1")
				last_row = cursor.fetchone()
				#print last_row
			   # print "-----------------------------"
				temp1=last_row[1]
				#print "PUMP_ON_by Hand if t* S3_BoilerTop >=  %s" % temp1
				
				StartTime=last_row[2]
			   # print "Start time  > %s" % StartTime
				
				EndTime=last_row[3]
			   # print "End time <= %s" % EndTime
			   # print "-----------------------------"
				temp2=last_row[4]
				#print "PUMP_ON by PC if t* S3_BoilerTop >=  %s" % temp2
				
				Time3=last_row[5]
				#print "Start time > %s" % Time3
				
				Time4=last_row[6]
				#print "End time <= %s" % Time4
				
				temp3=last_row[7]
				#print "OR t* K3_BoilerTop >= %s" % temp3
							
				temp4=last_row[8]
				#print "t* K3_BoilerTop - S3_BoilerTop >  %s" % temp4 
			   # print "-----------------------------"
				
				temp5=last_row[9]
				#print "PUMP_OFF by PC if t* S3_BoilerTop <=  %s" % temp5
				
				Time5=last_row[10]
				#print "OR if time is >  %s" %   Time5   
				#print "-----------------------------"
				#temp1: 40; StartTime: 700; EndTime: 2300temp2: 54; Time3: 700; Time4: 1600temp3: 40; temp4: 5; temp5: 52; Time5: 1600
				
				#print "-----------------------------"
				temp6=last_row[11]
				#print "Boiler_ON_by Hand if t* S3_BoilerTop < %s" % temp6
				
				temp7=last_row[12]
				#print "t* S3_BoilerTop-S3_BoilerBottom > %s" % temp7
				
				Time6=last_row[13]
				#print "Start time >  %s" % Time6
				
				Time7=last_row[14]
				#print "End time <= %s" % Time7
				#print "-----------------------------"
				
				temp8=last_row[15]
				#print "Boiler_ON by PC if t* S3_BoilerTop <= %s" % temp8
				
				Time8=last_row[16]
				#print "Start time %s <" % Time8
				
				Time9=last_row[17]
				#print "End time >= %s" % Time9
				#print "-----------------------------"
				
				temp9=last_row[18]
			   #print "Boiler_OFF by PC if t* S3_BoilerTop >  %s" % temp9
				
				Time10=last_row[19]
				#print "OR if time is >=  %s" %  Time10  
				#print "-----------------------------"
				
				#temp6: 50; temp7: 3; Time6: 700; Time7: 2300; temp8: 39; Time8: 700; Time9: 2300; temp9: 40; Time10: 700

				#print Set_S5_BoilerStatus, Set_S6_PumpStatus, Set_K5_BoilerStatus, Set_K6_PumpStatus, 
				#print temp1, StartTime, EndTime, temp2, Time3, Time4, temp3, temp4, temp5, Time5
				cursor.close()
		except Error as e:
			print(e)
		finally:
			conn.close()
    
	# Geting current Date and time  ------------------------------------
		print "========================================="
		Time = datetime.datetime.now().time()
		#print Time    
		Time = str(Time)
		Time = int(Time[0:2] + Time[3:5])
				
		Date = datetime.datetime.now().date()
		#print Date    
		Date = str(Date)
		Date = int(Date[5:7] + Date[8:10])
		print "Time = " , Time , " Date = ", Date
		
		# Summer and Winter time  --------------------------------------
		if (Date > 325 and Date < 1101):
			StartTime = 700
			EndTime = 2300
			print "Now is Summer time: ", StartTime, EndTime
		else:
			StartTime = 600
			EndTime = 2200
			print "Now is Winter time: ",StartTime, EndTime
	# Saving all database "mydb" ---------------------------------------  
		if Time > 2356:
			dbBackup()
			print colored('Database was saved!', 'white', 'on_green')
		else:
			print colored('Dbase will be saved between 23:56 and 24:00!', 'white', 'on_red')
			
	# Visualisation of Sistem States    ================================		
		if True:
			print "|=========================================|"
			print "|     Visualisation of System States      |"
			print "|=========================================|"
			
		# State of Solar Pump (S6_PumpStatus) according table "temp"----
			if S0_PumpStatus > (0.75*1023):
				S0_PumpStatus="0"
				print"Solar pump is " + colored('OFF', 'white', 'on_red')	
			else:
				S0_PumpStatus="5"
				print"Solar pump is " + colored('ON', 'grey', 'on_green')
		
		# Switching Circulation PUMP according table "commands"---------
			# HAND CONTROLING  -----------------------------------------
			if  Set_S6_PumpStatus == 1 and (S3_BoilerTop >= temp1 and (Time > StartTime and Time <= EndTime)):
				PUMP_ON = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 1"], shell=True)
				S6_PumpStatus = 1.0
				print"Circul_PUMP_Hand1: PUMP " + colored('ON', 'grey', 'on_green') + " (by HAND COMMAND)"
				
			elif  Set_S6_PumpStatus == 1 and (K3_BoilerTop - S3_BoilerTop > temp4 and K1_KotelOutput >= K3_BoilerTop):
				PUMP_ON = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 1"], shell=True)
				S6_PumpStatus = 1.0
				print"Circul_PUMP_Hand2: PUMP " + colored('ON', 'grey', 'on_green') + " (by HAND COMMAND)"
				
			elif Set_S6_PumpStatus == 0:
				PUMP_OFF = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 0"], shell=True)
				S6_PumpStatus = 0.0
				print"Circul_Pump_Hand3: PUMP " + colored('OFF', 'white', 'on_red') + " (by HAND COMMAND)"	
			
			# COMPUTER CONTROLING---------------------------------------   
			elif S5_BoilerStatus == 0.0  and (Time > Time3 and Time <= Time4) \
				and (S3_BoilerTop > temp2 and S3_BoilerTop > K3_BoilerTop)\
				and S3_BoilerTop - K3_BoilerTop > temp4:
				S6_PumpStatus = 1.0
				PUMP_ON = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 1"], shell=True)
				print"Circul_Pump_Pico1: PUMP " + colored('ON', 'grey', 'on_green') + " (by COMPUTER)"
				
			elif S5_BoilerStatus == 0.0 and K3_BoilerTop >= temp3 \
				and K3_BoilerTop - S3_BoilerTop > temp4 and K1_KotelOutput > K3_BoilerTop:
				S6_PumpStatus = 1.0
				PUMP_ON = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 1"], shell=True)
				print"Circul_Pump_Pico2: PUMP " + colored('ON', 'grey', 'on_green') + " (by COMPUTER)"
				
			elif S6_PumpStatus == 1.0 and S3_BoilerTop - K3_BoilerTop < temp4 or (S3_BoilerTop <= temp5 or Time > Time5) :
				S6_PumpStatus = 0.0
				PUMP_OFF = subprocess.check_output([snmpSet129 + "1.2.2.2.0 i 0"], shell=True)
				print"Circul_PUMP_Pico3: PUMP " + colored('OFF', 'white', 'on_red') + " (by COMPUTER)"
			
			else:
				print "No Action to Circulation_PUMP"
				
		# Switching Solar Boiler_ON_OFF according table "commands"------
			# HAND CONTROLING-------------------------------------------
			if  Set_S5_BoilerStatus == 1 and S3_BoilerTop < temp6 and (Time > Time6 and Time <= Time7)\
				or Set_S5_BoilerStatus == 1 and (S3_BoilerTop-S4_BoilerBottom >temp7) :
				Boiler_ON = subprocess.check_output([snmpSet129 + "1.2.2.1.0 i 1"], shell=True)
				S5_BoilerStatus = 1.0
				print"Solar_Heater_Hand1: Boiler " + colored('ON', 'grey', 'on_green') + " (by HAND COMMAND)"
				
			elif S6_PumpStatus == 1.0:
				Boiler_OFF = subprocess.check_output([snmpSet129 + "1.2.2.1.0 i 0"], shell=True)
				S5_BoilerStatus = 0.0
				print"Solar_Heater_Hand3: Boiler " + colored('OFF', 'white', 'on_red') + " (because SOLAR_PUMP is 'ON')"
				
			elif Set_S5_BoilerStatus == 0:            
				Boiler_OFF = subprocess.check_output([snmpSet129 + "1.2.2.1.0 i 0"], shell=True)
				S5_BoilerStatus = 0.0
				print"Solar_Heater_Hand2: Boiler " + colored('OFF', 'white', 'on_red') + " (by HAND COMMAND)"
					
			# COMPUTER CONTROLING---------------------------------------       
			elif S3_BoilerTop <= temp8 and (Time < Time8 or Time >= Time9) and S6_PumpStatus == 0.0:
				S5_BoilerStatus=1.0
				Boiler_ON = subprocess.check_output([snmpSet129 + "1.2.2.1.0 i 1"], shell=True)
				print"Solar_Heater_Pico1: Boiler " + colored('ON', 'grey', 'on_green') + " (by COMPUTER)"
				
			elif S5_BoilerStatus == 1.0 and (S3_BoilerTop > temp9 or Time >= Time10):
				S5_BoilerStatus = 0.0
				Boiler_OFF = subprocess.check_output([snmpSet129 + "1.2.2.1.0 i 0"], shell=True)
				print"Heater_Pico2: Boiler " + colored('OFF', 'white', 'on_red') + " (by COMPUTER)"
				
			else:
				print "No Action to Solar_Boiler"

		# Switching Kotel Boiler_ON_OFF according table "commands"------
			# HAND CONTROLING ------------------------------------------
			if  Set_K5_BoilerStatus == 1 and K3_BoilerTop < temp6 and (Time > Time6 and Time <= Time7)\
				or Set_K5_BoilerStatus == 1 and (K3_BoilerTop-K4_BoilerBottom >temp7) :
				Boiler_ON = subprocess.check_output([snmpSet130 + "1.2.2.5.0 i 1"], shell=True)
				K5_BoilerStatus = 1.0
				print"Kotel_Heater_Hand1: Boiler " + colored('ON', 'grey', 'on_green') + " (by HAND COMMAND)"
				
			elif S6_PumpStatus == 1.0:
				Boiler_OFF = subprocess.check_output([snmpSet130 + "1.2.2.5.0 i 0"], shell=True)
				K5_BoilerStatus = 0.0
				print"Kotel_Heater_Hand3: Boiler " + colored('OFF', 'white', 'on_red') + " (because SOLAR_PUMP is 'ON')"
				
			elif Set_K5_BoilerStatus == 0:
				Boiler_OFF = subprocess.check_output([snmpSet130 + "1.2.2.5.0 i 0"], shell=True)
				K5_BoilerStatus = 0.0
				print"Kotel_Heater_Hand2: Boiler " + colored('OFF', 'white', 'on_red') + " (by HAND COMMAND)"
				
			# COMPUTER CONTROLING---------------------------------------       
			elif K3_BoilerTop <= temp8 and (Time < Time8 or Time >= Time9) and S6_PumpStatus == 0.0:
				K5_BoilerStatus=1.0
				Boiler_ON = subprocess.check_output([snmpSet130 + "1.2.2.5.0 i 1"], shell=True)
				print"Kotel_Heater_Pico1: Boiler " + colored('ON', 'grey', 'on_green') + " (by COMPUTER)"
				
			elif K5_BoilerStatus == 1.0 and (K3_BoilerTop > temp9 or Time >= Time10):
				K5_BoilerStatus = 0.0
				Boiler_OFF = subprocess.check_output([snmpSet130 + "1.2.2.5.0 i 0"], shell=True)
				print"Kotel_Heater_Pico2: Boiler " + colored('OFF', 'white', 'on_red') + " (by COMPUTER)"
			
			else:
				print "No Action to Kotel_Boiler" 

		# Save data into mydb-------------------------------------------
			#Connect to mydb database ----------------------------------
			try:
				conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='1')
				if conn.is_connected():
					print "|=========================================|"
					print "| Connected to 'mydb' dbase, table 'temp' |"
					print "|=========================================|"
					cursor = conn.cursor()
					add_temp = ("INSERT INTO temp ""(Datetime, S1_BoilerInput, S2_BoilerOutput,"
					" S3_BoilerTop, S4_BoilerBottom, S5_BoilerStatus, S6_PumpStatus, S0_PumpStatus, K1_KotelOutput, K2_BoilerInput,"
					" K3_BoilerTop, K4_BoilerBottom, K5_BoilerStatus, K6_PumpStatus) "
							"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)")
					Datetime = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
					data_temp = (Datetime, S1_BoilerInput,S2_BoilerOutput,S3_BoilerTop,
					S4_BoilerBottom,S5_BoilerStatus,S6_PumpStatus, S0_PumpStatus, K1_KotelOutput, K2_BoilerInput,
					K3_BoilerTop, K4_BoilerBottom, K5_BoilerStatus, K6_PumpStatus)

				# Saving new temperatures-------------------------------
					cursor.execute(add_temp, data_temp)
					conn.commit()
					cursor.close()
					print "|Updating S1_BoilerInput:  %s" % colored(S1_BoilerInput, 'grey', 'on_green')
					print "|Updating S2_BoilerOutput: %s" % colored(S2_BoilerOutput, 'grey', 'on_green')
					print "|Updating S3_BoilerTop:    %s" % colored(S3_BoilerTop, 'grey', 'on_green')
					print "|Updating S4_BoilerBottom: %s" % colored(S4_BoilerBottom, 'grey', 'on_green')
					print "|Updating S5_BoilerStatus:  %s" % colored(S5_BoilerStatus, 'white', 'on_blue')
					print "|Updating S6_PumpStatus:    %s" % colored(S6_PumpStatus, 'white', 'on_blue')
					print "|Updating S0_PumpStatus:    %s" % colored(S0_PumpStatus, 'white', 'on_blue')
					print "|Updating K1_KotelOutput:  %s" % colored(K1_KotelOutput, 'grey', 'on_green')
					print "|Updating K2_BoilerInput:  %s" % colored(K2_BoilerInput, 'grey', 'on_green')
					print "|Updating K3_BoilerTop:    %s" % colored(K3_BoilerTop, 'grey', 'on_green')
					print "|Updating K4_BoilerBottom: %s" % colored(K4_BoilerBottom, 'grey', 'on_green')
					print "|Updating K5_BoilerStatus:  %s" % colored(K5_BoilerStatus, 'white', 'on_blue')
					print "|Updating K6_PumpStatus:    %s" % colored(K6_PumpStatus, 'white', 'on_blue')
					print "|=========================================|"
					for c in range(1,180):
						time.sleep(1)
						print  "\033[46;0H", colored("Awaiting for another cycle after 3 min.: ", 'white', 'on_blue', ['bold']), colored(c, 'white', 'on_red', ['bold'])
					os.system("clear")
			except Error as e:
				print(e)
			finally:
				conn.close()
run()
