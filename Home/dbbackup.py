import os
import datetime

from termcolor import colored, cprint
from data import db_connect
user = db_connect ['user']
password = db_connect ['password']
database = db_connect ['database']
backup_path = '/var/www/html/data/'

# Backup data base------------------------------------------------------
def dbbackup(time_):
    if time_ > 2356:
        date_time = '{:%Y.%m.%d-%H:%M:%S}'.format(datetime.datetime.now())
        todaybackup_path = backup_path + date_time

        # Checking if backup folder already exists or not. If not exists will create it.
        print "creating backup folder"
        if not os.path.exists(todaybackup_path):
            os.makedirs(todaybackup_path)

        # Code for checking if you want to take single database backup.
            print "Starting backup of database " + '"' + database+ '"'
            dumpcmd = "mysqldump -u " + user + " -p" + password + " " + database + " | " + " gzip "+ " > " + todaybackup_path + "/" + database + ".sql.gz"
            os.system(dumpcmd)
            os.system("clear")
            print "Backup script completed"
            print "Your backups has been created in '" + todaybackup_path + "' directory"
            print colored('Database was saved!', 'white', 'on_green')
    #else:
        #print colored('Dbase will be saved between 23:56 and 24:00!','white', 'on_red')
if __name__ == '__main__':
    import datetime
    dbbackup(2357)
