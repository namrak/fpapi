"""build find queries"""
import calendar
import time
import numpy as np
from pymongo import MongoClient
import fptotal
import parsecursor
from mdb import creds
#pylint: disable=C0103,C0301

def connect():
    """connect to mongodb"""
    client = MongoClient(creds['ip'], int(creds['port']))
    db = client.fpLoss
    db.authenticate(creds['un'], creds['pw'])
    return db

def get_name_from_id(apphandle, typeid):
    """get item name from typeid db"""
    typeids = apphandle.typeIDs
    cursor = typeids.find_one({"typeID": typeid}, {"name": 1})
    itemname = cursor['name']
    return itemname

def corporation_date(apphandle, corporationid, date):
    """find by corp system and specified date"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('corporationtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def corporation_days(apphandle, corporationid, days):
    """find by corp and specified days"""
    allloss = apphandle.allLoss
    if float(days) > 3 or float(days) < 0:
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
                               "items": 1,
                               "_id": 0}).hint('corporationtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def corporation_system_date(apphandle, corporationid, system, date):
    """find by corp system and specified date"""
    allloss = apphandle.allLoss
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
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def corporation_system_days(apphandle, corporationid, system, days):
    """find by corp system and specified days"""
    allloss = apphandle.allLoss
    system = int(system)
    if float(days) > 3 or float(days) < 0:
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
                               "items": 1,
                               "_id": 0}).hint('corporationsystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def corporation_system_oneday(apphandle, corporationid, system):
    """find by corp and system - one day"""
    allloss = apphandle.allLoss
    system = int(system)
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def corporation_oneday(apphandle, corporationid):
    """find by corp and system - one day"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"corporationID": corporationid,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('corporationsystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_date(apphandle, allianceid, date):
    """find by corp system and specified date"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "unixKillTime": {
                               "$gte": starttime,
                               "$lt": stoptime}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('alliancetime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_days(apphandle, allianceid, days):
    """find by corp and specified days"""
    allloss = apphandle.allLoss
    if float(days) > 3 or float(days) < 0:
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
                               "items": 1,
                               "_id": 0}).hint('alliancetime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_system_date(apphandle, allianceid, system, date):
    """find by corp system and specified date"""
    allloss = apphandle.allLoss
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
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_system_days(apphandle, allianceid, system, days):
    """find by corp system and specified days"""
    allloss = apphandle.allLoss
    if float(days) > 3 or float(days) < 0:
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
                               "items": 1,
                               "_id": 0}).hint('alliancesystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_system_oneday(apphandle, allianceid, system):
    """find by corp and system - one day"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "solarSystemID": system,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def alliance_oneday(apphandle, allianceid):
    """find by corp and system - one day"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"allianceID": allianceid,
                           "unixKillTime": {
                               "$gte": gmtminus}},
                          {"shipID": 1,
                           "items": 1,
                           "_id": 0}).hint('alliancesystemtime')
    #build lists for processing
    (ships, items, ammos, shipdata, itemdata) = parsecursor.ships_and_items(cursor)

    # generate ship list and count
    uships = np.unique(ships)
    shiptotals = fptotal.countships(shipdata, uships)
    for shiptotal in shiptotals:
        typename = get_name_from_id(apphandle, shiptotal['typeid'])
        shiptotal['name'] = typename

    # generate item list and count
    uitems = np.unique(items)
    itemtotals = fptotal.countitems(itemdata, uitems)
    for itemtotal in itemtotals:
        typename = get_name_from_id(apphandle, itemtotal['typeid'])
        itemtotal['name'] = typename

    # generate ammo list and count
    uammos = np.unique(ammos)
    ammototals = fptotal.countammos(itemdata, uammos)
    for ammototal in ammototals:
        typename = get_name_from_id(apphandle, ammototal['typeid'])
        ammototal['name'] = typename

    return (shiptotals, itemtotals, ammototals)

def doctrines(apphandle):
    """find and count hashes in last 24 hours"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    gmtminus = time.mktime(time.gmtime()) - timeframe
    cursor = allloss.find({"unixKillTime": {"$gte": gmtminus}},
                          {"killID": 1,
                           "shipID": 1,
                           "corporationName": 1,
                           "fitHash": 1,
                           "_id": 0}).hint('timeindex')
    (hashes, hashdata) = parsecursor.fithashes(cursor)
    uhashes = np.unique(hashes)
    hashtotals = fptotal.countfits(hashdata, uhashes)
    return hashtotals

def doctrines_date(apphandle, date):
    """find and count hashes for specific date"""
    allloss = apphandle.allLoss
    timeframe = 24 * 60 * 60
    datestring = date + ' 11:05:00'
    starttime = calendar.timegm(time.strptime(datestring, '%Y-%m-%d %H:%M:%S'))
    stoptime = starttime + timeframe
    cursor = allloss.find({"unixKillTime": {"$gte": starttime, "$lt": stoptime}},
                          {"killID": 1,
                           "shipID": 1,
                           "corporationName": 1,
                           "fitHash": 1,
                           "_id": 0}).hint('timeindex')
    (hashes, hashdata) = parsecursor.fithashes(cursor)
    uhashes = np.unique(hashes)
    hashtotals = fptotal.countfits(hashdata, uhashes)
    return hashtotals


if __name__ == "__main__":
    #tests
    mongohandle = connect()
    test1 = doctrines(mongohandle)
    test2 = doctrines_date(mongohandle, '2017-04-10')
    test3 = corporation_oneday(mongohandle, 98388312)
    test4 = alliance_oneday(mongohandle, 99005338)
    print(len(test1))
    print(len(test2))
    print(test3)
    print(test4)

