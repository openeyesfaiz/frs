import threading
import time
import json
import ast
import MySQLdb
import configparser

from websocket import create_connection

def enroll_query(create_time, query_img):
    name = "ABC"
    q = {"Detail":{"User":{"Name":name,"Type":"V","CreateTime":create_time,"FullImage":query_img}},"RequestType":300,"RequestId":1}
    return q

def gnh_query():
    q = '{"Detail":{"PageSize":100,"Page":1,},"RequestType":406,"RequestId":1}'
    return q

def gh_query():
    q = '{"Detail":{"PageSize":100,"Page":1,},"RequestType":401,"RequestId":1}'
    return q

def get_userlst():
    q = '{"Detail":{"PageSize":100,"Page":1,},"RequestType":311,"RequestId":1}'
    return q

def deenroll_query(the_id):
    q = '{"Detail":{"UserId":' + str(the_id) + ',"Option":0,},"RequestType":302,"RequestId":1}'
    return q



ws = create_connection("ws://fr.pop3global.com", timeout=None)
print("a")
#create_time = '2019-08-15 10:47:40'
#query_img = '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'
#ws.send(json.dumps(enroll_query(create_time, query_img)))
#ws.send(gnh_query())
#ws.send(gh_query())
#print("Send: {0}".format(json.dumps(enroll_query(create_time, query_img))))
'''
ws.send(get_userlst())

while(True):
    result = ws.recv()
    print("Result is: {0}".format(str(result)))


for i in range(448,466):
    ws.send(deenroll_query(i))
    result = ws.recv()
    print("Result is: {0}".format(str(result)))
'''