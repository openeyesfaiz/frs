import threading
import time
import json
import ast
import MySQLdb
import configparser
import datetime
import random

from websocket import create_connection
from ws4py.client.threadedclient import WebSocketClient

def gh_query():
    q = {"Detail":{"PageSize":100,"Page":10,},"RequestType":400,"RequestId":1}
    return q

def gnh_query():
    q = {"Detail":{"PageSize":100,"Page":10,},"RequestType":401,"RequestId":1}
    return q

def enroll_query(create_time, query_img):
    name = create_time
    
    create_time_a = create_time.split(' ')[0]
    create_time_b = create_time.split(' ')[1]
    create_year = create_time_a.split('-')[0]
    create_month = create_time_a.split('-')[1]
    create_date = create_time_a.split('-')[2]
    create_hour = create_time_b.split(':')[0]
    create_min = create_time_b.split(':')[1]
    create_sec = create_time_b.split(':')[2]
    
    last_four = str(random.randrange(0, 9999)).zfill(4)
    
    ref_num = "{0}{1}{2}{3}{4}{5}{6}".format(create_year,create_month,create_date,create_hour,create_min,create_sec,last_four)
    
    q = {"Detail":{"User":{"Name":name,"Type":"-","CreateTime":create_time,"FullImage":query_img,"ReferenceNumber":ref_num},"Options":0},"RequestType":300,"RequestId":1}
    return q

def get_one_query(frs_id):
    q = {"Detail":{"UserId":frs_id,},"RequestType":312,"RequestId":1}
    return q

#print(gh_query())
'''
class create_con(threading.Thread):
    
    def __init__(self, threadID, name, opt):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.opt = opt
        
        self.config = configparser.RawConfigParser()
        self.config.read("config/config.txt")
        details_dict = dict(self.config.items('Configuration'))
        
        self.db = MySQLdb.connect(host=details_dict['db_host'], user=details_dict['db_user'], passwd=details_dict['db_pwd'], db=details_dict['db_db'])
        
        
    def run(self):
        #try:
        cursor = self.db.cursor()
        db = self.db
        print("Creating Connection {0}...".format(str(self.name)))
        ws = create_connection("ws://fr.pop3global.com", timeout=None)
        
        ws.onclose = function
        print("Connection Success")
        
        if self.opt == 'gh':
            print("{0} Sending Message {1}".format(self.threadID, str(gh_query())))
            ws.send(json.dumps(gh_query()))
        elif self.opt == 'gnh':
            print("{0} Sending Message {1}".format(self.threadID, str(gnh_query())))
            ws.send(json.dumps(gnh_query()))
        else:
            print("Wrong Option")
            
        while(True):
            #try:
            print("{0} Receiving Message...".format(self.threadID))
            result = ws.recv()
            print("Received ({0}): {1}".format(self.name, result))
            
            result = ast.literal_eval(result)
            #print(result.get("MessageType"))
            if result.get("MessageType") == 900: #Hit Alert
                details = result.get("Details")
                create_time = result.get("CreateTime")
                
                create_time_a = create_time.split(' ')[0]
                create_time_b = create_time.split(' ')[1]
                
                create_year = create_time_a.split('/')[2]
                create_month = create_time_a.split('/')[1].zfill(2)
                create_date = create_time_a.split('/')[0].zfill(2)
                
                create_time_reform = "{0}-{1}-{2} {3}".format(str(create_year),str(create_month),str(create_date),str(create_time_b))
                
                query_img = result.get("QueryImage")
                
                u_id = details[0]['UserId']
                
                cursor = self.db.cursor()
                user_id = None
                try:
                    #print("Debug A")
                    #print(u_id)
                    #print(type(str(u_id)))
                    cursor.execute("""SELECT * FROM enrolled_user WHERE frsid = %s""",(u_id,))
                    print("Debug A")
                    results = cursor.fetchall()
                    print(len(results))
                    if len(results) == 1:
                        for result in results:
                            user_id = result[3]
                except Exception as e:
                    print("Error: {0}".format(e))
                print(user_id)
                if user_id:
                    st_chance = details[0]
                    score = st_chance.get("Score")
                    user_id_frs = st_chance.get("UserId")
                    score = st_chance.get('Score')
                    
                    print(st_chance)
                    try:
                        cursor = self.db.cursor()
                        cursor.execute("""INSERT INTO hit_image(image,score,create_time,enrolled_userid) VALUES (%s, %s, %s, %s)""",(str(query_img), score, str(create_time_reform), user_id_frs))

                        db.commit()
                    except:
                        db.rollback()
                        
                
                #print("{0} {1} {2}".format(str(details), str(create_time), str(query_img)))
            elif result.get("MessageType") == 901: #Not Hit Alert
                create_time = result.get("CreateTime")
                query_img = result.get("QueryImage")
                #ws.send(json.dumps(enroll_query(create_time, query_img)))
                
                #print("{0} {1}".format(create_time, query_img))
                #print("Create Time {0}".format(create_time))
                create_time_a = create_time.split(' ')[0]
                create_time_b = create_time.split(' ')[1]
                
                create_year = create_time_a.split('/')[2]
                create_month = create_time_a.split('/')[1].zfill(2)
                create_date = create_time_a.split('/')[0].zfill(2)
                
                create_time_reform = "{0}-{1}-{2} {3}".format(str(create_year),str(create_month),str(create_date),str(create_time_b))
                #print("Create Time Reform {0}".format(create_time_reform))
                #print("a")
                ws.send(json.dumps(enroll_query(create_time_reform, query_img)))
                #print("b")
                
            elif result.get("RequestType") == 300 and result.get("ResponseCode") == 0:
                enroll_result = result
                
                if 'Detail' in enroll_result:
                    if 'PersonList' in enroll_result['Detail']:
                        enrolled_list = enroll_result['Detail']['PersonList']
                        for one_enrolled in enrolled_list:
                            the_frsid = one_enrolled['UserId']
                            the_name = "User_{0}".format(the_frsid)
                            the_img = one_enrolled['FaceInfo']['FaceImage']
                        
                            try:
                                cursor.execute("""INSERT INTO enrolled_user(name, image, frsid) VALUES (%s, %s, %s)""",(str(the_name),str(the_img),str(the_frsid)))
                                db.commit()
                            except:
                                db.rollback()
                
            elif result.get("ResponseType") == 300:
                print("User enrolled")
            #except Exception as e:
            #    print(e)
        ws.close()
        print("Connection {0} closed".format(self.threadID))
        #except Exception as e:
        #    print(e)



get_hit_thread = create_con(threadID=1, name="FRS Web Socket", opt="gh")
#get_nothit_thread = create_con(threadID=2, name="Get Not Hit", opt="gnh")

get_hit_thread.start()
#get_nothit_thread.start()

get_hit_thread.join()
#get_nothit_thread.join()

print("Exiting Main Thread")        
'''
#############################################################################


class CG_Client(WebSocketClient):
    def opened(self):
        
        config = configparser.RawConfigParser()
        config.read("config/config.txt")
        details_dict = dict(config.items('Configuration'))
        
        self.db = MySQLdb.connect(host=details_dict['db_host'], user=details_dict['db_user'], passwd=details_dict['db_pwd'], db=details_dict['db_db'])
        
        self.send(json.dumps(gh_query()))
        
    def closed(self, code, reason=None):
        print("Closed down:", code, reason)
        
    def received_message(self, resp):
        print("Receiving Message...")

        print("Received: {0}".format(resp))
        
        result = ast.literal_eval(resp.data.decode("utf-8"))
        #print(result.get("MessageType"))
        if result.get("MessageType") == 900: #Hit Alert
            details = result.get("Details")
            create_time = result.get("CreateTime")
            
            create_time_a = create_time.split(' ')[0]
            create_time_b = create_time.split(' ')[1]
            
            create_year = create_time_a.split('/')[2]
            create_month = create_time_a.split('/')[1].zfill(2)
            create_date = create_time_a.split('/')[0].zfill(2)
            
            create_time_reform = "{0}-{1}-{2} {3}".format(str(create_year),str(create_month),str(create_date),str(create_time_b))
            
            query_img = result.get("QueryImage")
            
            u_id = details[0]['UserId']
            
            cursor = self.db.cursor()
            user_id = None
            try:
                #print("Debug A")
                #print(u_id)
                #print(type(str(u_id)))
                cursor.execute("""SELECT * FROM enrolled_user WHERE frsid = %s""",(u_id,))
                #print("Debug A")
                results = cursor.fetchall()
                #print(len(results))
                if len(results) == 1:
                    for result in results:
                        user_id = result[3]
            except Exception as e:
                print("Error: {0}".format(e))
            print(user_id)
            if user_id:
                st_chance = details[0]
                score = st_chance.get("Score")
                user_id_frs = st_chance.get("UserId")
                score = st_chance.get('Score')
                
                print(st_chance)
                try:
                    cursor = self.db.cursor()
                    cursor.execute("""INSERT INTO hit_image(image,score,create_time,enrolled_userid) VALUES (%s, %s, %s, %s)""",(str(query_img), score, str(create_time_reform), user_id_frs))

                    self.db.commit()
                except:
                    self.db.rollback()
                    
            
            #print("{0} {1} {2}".format(str(details), str(create_time), str(query_img)))
        elif result.get("MessageType") == 901: #Not Hit Alert
            create_time = result.get("CreateTime")
            query_img = result.get("QueryImage")
            #ws.send(json.dumps(enroll_query(create_time, query_img)))
            
            #print("{0} {1}".format(create_time, query_img))
            #print("Create Time {0}".format(create_time))
            create_time_a = create_time.split(' ')[0]
            create_time_b = create_time.split(' ')[1]
            
            create_year = create_time_a.split('/')[2]
            create_month = create_time_a.split('/')[1].zfill(2)
            create_date = create_time_a.split('/')[0].zfill(2)
            
            create_time_reform = "{0}-{1}-{2} {3}".format(str(create_year),str(create_month),str(create_date),str(create_time_b))
            #print("Create Time Reform {0}".format(create_time_reform))
            #print("a")
            the_query = enroll_query(create_time_reform, query_img)
            ws.send(json.dumps(the_query))
            ref_num = the_query['Detail']['User']['ReferenceNumber']
            print(ref_num)
            #print("b")
            
        elif result.get("RequestType") == 300 and result.get("ResponseCode") == 0:  #User enrolled
            enroll_result = result
            
            if 'Detail' in enroll_result:
                if 'PersonList' in enroll_result['Detail']:
                    enrolled_list = enroll_result['Detail']['PersonList']
                    for one_enrolled in enrolled_list:
                        the_frsid = one_enrolled["UserId"]
                        the_name = "User_{0}".format(the_frsid)
                        
                        the_createtime = enroll_result['Detail']['CreateTime']
                        the_img = one_enrolled['FaceInfo']['FaceImage']

                        try:    #insert a profile
                            cursor = self.db.cursor()
                            cursor.execute("""INSERT INTO profile(name, image, create_datetime, frsid) VALUES (%s, %s, %s, %s)""",(str(the_name),str(the_img),str(the_createtime),str(the_frsid)))
                            self.db.commit()
                            
                        except:
                            self.db.rollback()
                            
                        profile_id = None
                        try:    #select the new profile
                            cursor = self.db.cursor()
                            cursor.execute("""SELECT * FROM enrolled_user WHERE image = %s""",(str(the_img),))
                            results = cursor.fetchall()
                            if len(results) > 0:
                                for result in results:
                                    profile_id = result[0]
                        except:
                            self.db.rollback()

                        try:    #insert a new enrolled user and see if profile exist
                            cursor = self.db.cursor()
                            if profile_id:
                                cursor.execute("""INSERT INTO enrolled_user(name, image, create_datetime, frsid, profile_id) VALUES (%s, %s, %s, %s, %s)""",(str(the_name),str(the_img),str(the_createtime),str(the_frsid),str(profile_id)))
                            else:
                                cursor.execute("""INSERT INTO enrolled_user(name, image, create_datetime, frsid) VALUES (%s, %s, %s, %s)""",(str(the_name),str(the_img),str(the_createtime),str(the_frsid)))
                            self.db.commit()
                            
                        except:
                            self.db.rollback()

                        the_query = get_one_query(the_frsid)
                        ws.send(json.dumps(the_query))

        elif result.get("RequestType") == 312 and result.get("ResponseCode") == 0:  #User searched
            search_result = result
            
            if 'Detail' in search_result:
                if 'User' in search_result['Detail']:
                    search_list = search_result['Detail']['User']
                    
                    search_id = search_list["Id"]
                    search_name = search_list["Name"]
                    search_refnum = search_list["ReferenceNumber"]
                    search_createtime = search_list["CreateTime"]
                    #search_fullimage = search_list["FullImage"]
                    
                    print("Testing B")
                    print(search_id)
                    print(search_name)
                    print(search_refnum)
                    print(search_createtime)
                    try:
                        
                        cursor = self.db.cursor()
                        cursor.execute("""UPDATE enrolled_user SET ref_num=%s WHERE frsid=%s""",(str(search_refnum), str(search_id)))
                        self.db.commit()
                        
                    except Exception as e:
                        self.db.rollback()
                        #print("Testing C")
                        print(e)
        

if __name__ == '__main__':
    ws = None
    try:
        ws = CG_Client("ws://fr.pop3global.com")
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()