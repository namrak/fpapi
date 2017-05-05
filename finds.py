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

# leaving this in because it might be helpful later
def get_name_from_id(mongohandle, typeid):
    """get item name from typeid db"""
    typeids = mongohandle.typeIDs
    cursor = typeids.find_one({"typeID": typeid}, {"name": 1})
    itemname = cursor['name']
    return itemname

def corporation_date(mongohandle, corporationid, date):
    """find by corp system and specified date"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('corporationtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_days(mongohandle, corporationid, days):
    """find by corp and specified days"""
    allloss = mongohandle.allLoss
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allloss.find({"corporationID": corporationid,
                               "unixKillTime": {
                                   "$gte": gmtminus}},
                              {"shipID": 1,
                               "shipName":1,
                               "items": 1,
                               "_id": 0}).hint('corporationtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_date(mongohandle, corporationid, system, date):
    """find by corp system and specified date"""
    allloss = mongohandle.allLoss
    system = int(system)
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_days(mongohandle, corporationid, system, days):
    """find by corp system and specified days"""
    allloss = mongohandle.allLoss
    system = int(system)
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allloss.find({"corporationID": corporationid,
                               "solarSystemID": system,
                               "unixKillTime": {
                                   "$gte": gmtminus}},
                              {"shipID": 1,
                               "shipName":1,
                               "items": 1,
                               "_id": 0}).hint('corporationsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_system_oneday(mongohandle, corporationid, system):
    """find by corp and system - one day"""
    allloss = mongohandle.allLoss
    system = int(system)
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def corporation_oneday(mongohandle, corporationid):
    """find by corp and system - one day"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_date(mongohandle, allianceid, date):
    """find by corp system and specified date"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('alliancetime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_days(mongohandle, allianceid, days):
    """find by corp and specified days"""
    allloss = mongohandle.allLoss
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allloss.find({"allianceID": allianceid,
                               "unixKillTime": {
                                   "$gte": gmtminus}},
                              {"shipID": 1,
                               "shipName":1,
                               "items": 1,
                               "_id": 0}).hint('alliancetime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_date(mongohandle, allianceid, system, date):
    """find by corp system and specified date"""
    allloss = mongohandle.allLoss
    system = int(system)
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_days(mongohandle, allianceid, system, days):
    """find by corp system and specified days"""
    allloss = mongohandle.allLoss
    if float(days) > 7 or float(days) < 0:
        shiptotals = [{"error":"parameter 'days' range error"}]
        itemtotals = [{"error":"parameter 'days' range error"}]
        ammototals = [{"error":"parameter 'days' range error"}]
        return (shiptotals, itemtotals, ammototals)
    else:
        timeframe = float(days) * 24 * 60 * 60
        gmtminus = time.mktime(time.gmtime()) - timeframe
        cursor = allloss.find({"allianceID": allianceid,
                               "solarSystemID": system,
                               "unixKillTime": {
                                   "$gte": gmtminus}},
                              {"shipID": 1,
                               "shipName":1,
                               "items": 1,
                               "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_system_oneday(mongohandle, allianceid, system):
    """find by corp and system - one day"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def alliance_oneday(mongohandle, allianceid):
    """find by corp and system - one day"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "shipName":1,
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    (ships, items, ammos) = parsecursor.ships_and_items(cursor)
    return (ships, items, ammos)

def doctrines(mongohandle):
    """find and count hashes in last 24 hours"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"unixKillTime": {"$gte": gmtminus}},
                          {"killID": 1,
                           "shipID": 1,
                           "shipName":1,
                           "corporationName": 1,
                           "fitHash": 1,
                           "_id": 0}).hint('timeindex')
    hashtotals = parsecursor.fithashes(cursor)
    return hashtotals

def doctrines_date(mongohandle, date):
    """find and count hashes for specific date"""
    allloss = mongohandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"unixKillTime": {"$gte": starttime, "$lt": stoptime}},
                          {"killID": 1,
                           "shipID": 1,
                           "shipName":1,
                           "corporationName": 1,
                           "fitHash": 1,
                           "_id": 0}).hint('timeindex')
    hashtotals = parsecursor.fithashes(cursor)
    return hashtotals

if __name__ == "__main__":
    #tests
    testhandle = connect()
    test1 = doctrines(testhandle)
    test2 = doctrines_date(testhandle, '2017-04-10')
    test3 = corporation_oneday(testhandle, 98388312)
    test4 = alliance_oneday(testhandle, 99005338)
    print(len(test1))
    print(len(test2))
    print(test3)
    print(test4)

