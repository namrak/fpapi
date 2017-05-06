"""build find queries"""
import calendar
import time
from pymongo import MongoClient
import parsecursor
from mdb import creds

def connect():
    """connect to mongodb"""
    client = MongoClient(creds['ip'], int(creds['port']))
    db = client.fpLoss
    db.authenticate(creds['un'], creds['pw'])
    return db

def corporation_date(mongohandle, corporation_id, date):
    """find by corp system and specified date"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allkills.find({"corporation_id": corporation_id,
                            "unix_kill_time": {
                                "$gte": starttime,
                                "$lt": stoptime}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('corptime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_days(mongohandle, corporation_id, days):
    """find by corp and specified days"""
    allkills = mongohandle.allkills
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allkills.find({"corporation_id": corporation_id,
                                "unix_kill_time": {
                                    "$gte": gmtminus}},
                               {"ship": 1,
                                "items": 1,
                                "_id": 0}).hint('corptime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_date(mongohandle, corporation_id, system, date):
    """find by corp system and specified date"""
    allkills = mongohandle.allkills
    system = int(system)
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allkills.find({"corporation_id": corporation_id,
                            "solar_system_id": system,
                            "unix_kill_time": {
                                "$gte": starttime,
                                "$lt": stoptime}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('corpsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_days(mongohandle, corporation_id, system, days):
    """find by corp system and specified days"""
    allkills = mongohandle.allkills
    system = int(system)
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allkills.find({"corporation_id": corporation_id,
                                "solar_system_id": system,
                                "unix_kill_time": {
                                    "$gte": gmtminus}},
                               {"ship": 1,
                                "items": 1,
                                "_id": 0}).hint('corpsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_oneday(mongohandle, corporation_id, system):
    """find by corp and system - one day"""
    allkills = mongohandle.allkills
    system = int(system)
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allkills.find({"corporation_id": corporation_id,
                            "solar_system_id": system,
                            "unix_kill_time": {
                                "$gte": gmtminus}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('corpsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_oneday(mongohandle, corporation_id):
    """find by corp and system - one day"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allkills.find({"corporation_id": corporation_id,
                            "unix_kill_time": {
                                "$gte": gmtminus}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('corptime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_date(mongohandle, alliance_id, date):
    """find by corp system and specified date"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allkills.find({"alliance_id": alliance_id,
                            "unix_kill_time": {
                                "$gte": starttime,
                                "$lt": stoptime}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('alliancetime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_days(mongohandle, alliance_id, days):
    """find by corp and specified days"""
    allkills = mongohandle.allkills
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allkills.find({"alliance_id": alliance_id,
                                "unix_kill_time": {
                                    "$gte": gmtminus}},
                               {"ship": 1,
                                "items": 1,
                                "_id": 0}).hint('alliancetime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_date(mongohandle, alliance_id, system, date):
    """find by corp system and specified date"""
    allkills = mongohandle.allkills
    system = int(system)
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allkills.find({"alliance_id": alliance_id,
                            "solar_system_id": system,
                            "unix_kill_time": {
                                "$gte": starttime,
                                "$lt": stoptime}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_days(mongohandle, alliance_id, system, days):
    """find by corp system and specified days"""
    allkills = mongohandle.allkills
    system = int(system)
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allkills.find({"alliance_id": alliance_id,
                                "solar_system_id": system,
                                "unix_kill_time": {
                                    "$gte": gmtminus}},
                               {"ship": 1,
                                "items": 1,
                                "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_oneday(mongohandle, alliance_id, system):
    """find by corp and system - one day"""
    allkills = mongohandle.allkills
    system = int(system)
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allkills.find({"alliance_id": alliance_id,
                            "solar_system_id": system,
                            "unix_kill_time": {
                                "$gte": gmtminus}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_oneday(mongohandle, alliance_id):
    """find by corp and system - one day"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allkills.find({"alliance_id": alliance_id,
                            "unix_kill_time": {
                                "$gte": gmtminus}},
                           {"ship": 1,
                            "items": 1,
                            "_id": 0}).hint('alliancetime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def doctrines(mongohandle):
    """find and count hashes in last 24 hours"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allkills.find({"unix_kill_time": {"$gte": gmtminus}},
                           {"kill_id": 1,
                            "ship": 1,
                            "corporation_name": 1,
                            "fithash": 1,
                            "_id": 0}).hint('timefithashindex')
    hashtotals = parsecursor.fithashes(cursor)
    for fithash in list(hashtotals):
        if hashtotals[fithash]['count'] < 5:
            hashtotals.pop(fithash)
    return hashtotals

def doctrines_date(mongohandle, date):
    """find and count hashes for specific date"""
    allkills = mongohandle.allkills
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allkills.find({"unix_kill_time": {"$gte": starttime, "$lt": stoptime}},
                           {"kill_id": 1,
                            "ship": 1,
                            "corporation_name": 1,
                            "fithash": 1,
                            "_id": 0}).hint('timefithashindex')
    hashtotals = parsecursor.fithashes(cursor)
    for fithash in list(hashtotals):
        if hashtotals[fithash]['count'] < 5:
            hashtotals.pop(fithash)
    return hashtotals

def doctrines_days(mongohandle, days):
    """find and count hashes for specified days"""
    allkills = mongohandle.allkills
    if float(days) > 7 or float(days) < 0:
        return {"error":"parameter 'days' range error"}
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe    
        cursor = allkills.find({"unix_kill_time": {"$gte": gmtminus}},
                               {"kill_id": 1,
                                "ship": 1,
                                "corporation_name": 1,
                                "fithash": 1,
                                "_id": 0}).hint('timefithashindex')
    hashtotals = parsecursor.fithashes(cursor)
    for fithash in list(hashtotals):
        if hashtotals[fithash]['count'] < 5:
            hashtotals.pop(fithash)
    return hashtotals

if __name__ == "__main__":
    # tests
    testhandle = connect()
    test1 = doctrines(testhandle)
    test2 = doctrines_date(testhandle, '2017-05-05')
    test3 = doctrines_days(testhandle, 4)
    (shiptest1, itemtest1, ammotest1) = corporation_oneday(testhandle, 98388312)
    (shiptest2, itemtest2, ammotest2) = alliance_oneday(testhandle, 99005338)
    (shiptest3, itemtest3, ammotest3) = corporation_days(testhandle, 98388312, 2)
    (shiptest4, itemtest4, ammotest4) = alliance_days(testhandle, 99005338, 2)
    (shiptest5, itemtest5, ammotest5) = corporation_date(testhandle, 98388312, '2017-05-05')
    (shiptest6, itemtest6, ammotest6) = alliance_date(testhandle, 99005338, '2017-05-05')
    (shiptest7, itemtest7, ammotest7) = corporation_system_days(testhandle, 98388312, 30002016, 2)
    (shiptest8, itemtest8, ammotest8) = alliance_system_days(testhandle, 99005338, 30002016, 2)
    (shiptest9, itemtest9, ammotest9) = corporation_system_date(testhandle, 98388312, 30002016, '2017-05-05')
    (shiptest10, itemtest10, ammotest10) = alliance_system_date(testhandle, 99005338, 30002016, '2017-05-05')
    (shiptest11, itemtest11, ammotest11) = corporation_system_oneday(testhandle, 98388312, 30002016)
    (shiptest12, itemtest12, ammotest12) = alliance_system_oneday(testhandle, 99005338, 30002016)
    print(len(test1),len(test2),len(test3))
    print(len(shiptest1), len(itemtest2),len(shiptest3), len(itemtest4))
    print(len(ammotest5), len(itemtest6),len(shiptest7), len(itemtest8))
    print(len(ammotest8), len(itemtest10),len(shiptest10), len(itemtest7))
    print(len(ammotest7), len(itemtest6),len(shiptest4), len(itemtest3))
    print(len(ammotest11), len(itemtest11),len(shiptest12), len(itemtest12))


