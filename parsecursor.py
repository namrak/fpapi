"""build lists from cursor"""
import podorstructure

def ships_and_items(cursor):
    """return data from cursor - ships and items"""
    ships = []
    items = []
    ammos = []
    shipdata = []
    itemdata = []
    for killmail in cursor:
        ships.append(killmail['shipID'])
        shipdata.append({'typeid': killmail['shipID']})
        for item in killmail['items']:
            if item['isAmmo'] is True:
                ammos.append(item['itemID'])
            else:
                items.append(item['itemID'])
            itemdata.append(
                {'typeid': item['itemID'],
                 'attached': item['isAttached'],
                 'quantity': item['quantity'],
                 'dropped': item['dropped']})
    return (ships, items, ammos, shipdata, itemdata)

def fithashes(cursor):
    """return data from cursor - fit hashes"""
    hashes = []
    hashdata = []
    for killmail in cursor:
        if podorstructure.check(killmail['shipID']) != 1:
            hashes.append(killmail['fitHash'])
            killmailurl = 'https://zkillboard.com/kill/' + str(killmail['killID'])
            hashdata.append({
                'fitHash': killmail['fitHash'],
                'killurl': killmailurl,
                'corpName': killmail['corporationName']})
    return (hashes, hashdata)
