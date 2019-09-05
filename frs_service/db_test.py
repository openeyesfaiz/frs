import MySQLdb
import configparser

config = configparser.RawConfigParser()
config.read("config/config.txt")
details_dict = dict(config.items('Configuration'))
db = MySQLdb.connect(host=details_dict['db_host'], user=details_dict['db_user'], passwd=details_dict['db_pwd'], db=details_dict['db_db'])

cursor = db.cursor()
cursor.execute("""INSERT INTO hit_image(image,score,create_time,enrolled_userid) VALUES (%s, %s, %s, %s)""",("ghgh g b", 0.651, "2019-08-21 17:19:50", 5))
db.commit()