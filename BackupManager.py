"""
Simple backup manager for a minecraft server.

Written by Jessie Harvey, 19/02/2022.
Intended for use with a vanilla minecraft server using standard Mojang server hosting tools.
Creates a backup each time the server is started. 
"""

from datetime import datetime
import os
import shutil

server_directory = 'C:\\Users\\45232903\\Desktop\\MinecraftServer' # <-- insert your server directory here.

backup_directory = server_directory + '\\backups'
backup_name = 'backup' + str(datetime.today()).split()[0].replace('-', '_')
world_file = server_directory + '\\world' # World name and directory. Change this if you rename your world folder.

if not os.path.isdir(backup_directory):
    print('attempting to create backup directory...')
    try:
        os.mkdir(backup_directory)
        print('Backup directory created successfully.')
    except:
        print('Failed to create backup directory.')

if backup_name not in os.listdir(backup_directory):
    print('attempting to create backup...')
    try:
        shutil.copytree(world_file, str(backup_directory + '\\' + backup_name))
        print('Backup successful.')
    except:
        print('Backup failed.')

# Deletes oldest backup if there are more than 10 after performing the most recent backup.
if len(os.listdir(backup_directory)) > 10:
    print('attempting to prune excess backups...')
    oldest_backup = None
    for file in os.listdir(backup_directory):
        try:
            if os.path.getmtime(backup_directory + '\\' + file) < os.path.getmtime(backup_directory + '\\' + oldest_backup):
                oldest_backup = file
        except:
            oldest_backup = file
    try:
        shutil.rmtree(backup_directory + '\\' + oldest_backup)
        print('Backup pruning successful.')
    except:
        print('Backup pruning failed.')