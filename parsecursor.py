"""build return data from cursor"""
import podorstructure

def ships_and_items(cursor):
    """return data from cursor - ships and items"""
    ships = {}
    items = {}
    ammos = {}
    for killmail in cursor:
        if killmail['shipID'] in ships:
            ships[killmail['shipID']]['totallost'] += 1
        else:
            ships[killmail['shipID']] = {}
            ships[killmail['shipID']]['name'] = killmail['shipName']
            ships[killmail['shipID']]['totallost'] = 1
        for item in killmail['items']:
            if item['isAmmo'] is True:
                if item['itemID'] in ammos:
                    ammos[item['itemID']]['totallost'] += item['quantity']
                    if item['dropped'] is True:
                        ammos[item['itemID']]['quantitydropped'] += item['quantity']
                    if item['isAttached'] is True:
                        ammos[item['itemID']]['quantityattached'] += item['quantity']
                else:
                    ammos[item['itemID']] = {}
                    ammos[item['itemID']]['name'] = item['itemName']
                    ammos[item['itemID']]['totallost'] = item['quantity']
                    if item['dropped'] is True:
                        ammos[item['itemID']]['quantitydropped'] = item['quantity']
                    else:
                        ammos[item['itemID']]['quantitydropped'] = 0
                    if item['isAttached'] is True:
                        ammos[item['itemID']]['quantityattached'] = item['quantity']
                    else:
                        ammos[item['itemID']]['quantityattached'] = 0
            else:
                if item['itemID'] in items:
                    items[item['itemID']]['totallost'] += item['quantity']
                    if item['dropped'] is True:
                        items[item['itemID']]['quantitydropped'] += item['quantity']
                    if item['isAttached'] is True:
                        items[item['itemID']]['quantityattached'] += item['quantity']
                else:
                    items[item['itemID']] = {}
                    items[item['itemID']]['name'] = item['itemName']
                    items[item['itemID']]['totallost'] = item['quantity']
                    if item['dropped'] is True:
                        items[item['itemID']]['quantitydropped'] = item['quantity']
                    else:
                        items[item['itemID']]['quantitydropped'] = 0
                    if item['isAttached'] is True:
                        items[item['itemID']]['quantityattached'] = item['quantity']
                    else:
                        items[item['itemID']]['quantityattached'] = 0
    return (ships, items, ammos)

def fithashes(cursor):
    """return data from cursor - fit hashes"""
    hashtotals = {}
    for killmail in cursor:
        if podorstructure.check(killmail['shipID']) != 1:
            if killmail['fitHash'] in hashtotals:
                hashreport = {}
                hashreport['corporation'] = killmail['corporationName']
                hashreport['url'] = 'https://zkillboard.com/kill/' + str(killmail['killID'])
                hashtotals[killmail['fitHash']]['count'] += 1
                hashtotals[killmail['fitHash']]['data'].append(hashreport)
            else:
                hashreport = {}
                hashreport['corporation'] = killmail['corporationName']
                hashreport['url'] = 'https://zkillboard.com/kill/' + str(killmail['killID'])
                hashtotals[killmail['fitHash']] = {}
                hashtotals[killmail['fitHash']]['count'] = 1
                hashtotals[killmail['fitHash']]['shipname'] = killmail['shipName']
                hashtotals[killmail['fitHash']]['data'] = []
                hashtotals[killmail['fitHash']]['data'].append(hashreport)
    return hashtotals


