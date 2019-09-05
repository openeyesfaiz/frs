import threading
import time
import json
import ast
import MySQLdb
import configparser

from websocket import create_connection

def get_user_list_query():
    q = {"Detail":{"PageSize":100,"Page":10,"GetFullImage":true,"GetThrumbnailImage":true},"RequestType":311,"RequestId":1}
    return q

class create_con(threading.Thread):
    
    def __init__(self, threadID, name, opt):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
        self.config = configparser.RawConfigParser()
        self.config.read("config/config.txt")
        details_dict = dict(self.config.items('Configuration'))
        
        self.db = MySQLdb.connect(host=details_dict['db_host'], user=details_dict['db_user'], passwd=details_dict['db_pwd'], db=details_dict['db_db'])
        
        
    def run(self):
        try:
            pass
        except Exception as e:
            print(e)



get_userlist_thread = create_con(threadID=1, name="FRS Get User List")

get_userlist_thread.start()

get_userlist_thread.join()

print("Exiting Main Thread")    