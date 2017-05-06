"""build return data from cursor"""
import podorstructure

def ships_and_items(cursor):
    """return data from cursor - ships and items"""
    ships = {}
    items = {}
    ammos = {}
    for killmail in cursor:
        if killmail['ship']['type_id'] in ships:
            ships[killmail['ship']['type_id']]['total_lost'] += 1
        else:
            ships[killmail['ship']['type_id']] = {}
            ships[killmail['ship']['type_id']]['name'] = killmail['ship']['name']
            ships[killmail['ship']['type_id']]['total_lost'] = 1
        for item in killmail['items']:
            if item['is_ammo'] is True:
                if item['type_id'] in ammos:
                    ammos[item['type_id']]['total_lost'] += item['quantity']
                    if item['dropped'] is True:
                        ammos[item['type_id']]['quantity_dropped'] += item['quantity']
                    if item['is_attached'] is True:
                        ammos[item['type_id']]['quantity_attached'] += item['quantity']
                else:
                    ammos[item['type_id']] = {}
                    ammos[item['type_id']]['_name'] = item['name']
                    ammos[item['type_id']]['total_lost'] = item['quantity']
                    if item['dropped'] is True:
                        ammos[item['type_id']]['quantity_dropped'] = item['quantity']
                    else:
                        ammos[item['type_id']]['quantity_dropped'] = 0
                    if item['is_attached'] is True:
                        ammos[item['type_id']]['quantity_attached'] = item['quantity']
                    else:
                        ammos[item['type_id']]['quantity_attached'] = 0
            else:
                if item['type_id'] in items:
                    items[item['type_id']]['total_lost'] += item['quantity']
                    if item['dropped'] is True:
                        items[item['type_id']]['quantity_dropped'] += item['quantity']
                    if item['is_attached'] is True:
                        items[item['type_id']]['quantity_attached'] += item['quantity']
                else:
                    items[item['type_id']] = {}
                    items[item['type_id']]['_name'] = item['name']
                    items[item['type_id']]['total_lost'] = item['quantity']
                    if item['dropped'] is True:
                        items[item['type_id']]['quantity_dropped'] = item['quantity']
                    else:
                        items[item['type_id']]['quantity_dropped'] = 0
                    if item['is_attached'] is True:
                        items[item['type_id']]['quantity_attached'] = item['quantity']
                    else:
                        items[item['type_id']]['quantity_attached'] = 0
    return (ships, items, ammos)

def fithashes(cursor):
    """return data from cursor - fit hashes"""
    hashtotals = {}
    for killmail in cursor:
        if podorstructure.check(killmail['ship']['type_id']) != 1:
            if killmail['fithash'] in hashtotals:
                hashtotals[killmail['fithash']]['count'] += 1
                hashreport = {}
                hashreport['corporation'] = killmail['corporation_name']
                hashreport['url'] = 'https://zkillboard.com/kill/' + str(killmail['kill_id'])
                hashtotals[killmail['fithash']]['data'].append(hashreport)
            else:
                hashtotals[killmail['fithash']] = {}
                hashtotals[killmail['fithash']]['count'] = 1
                hashtotals[killmail['fithash']]['_name'] = killmail['ship']['name']
                hashtotals[killmail['fithash']]['data'] = []
                hashreport = {}
                hashreport['corporation'] = killmail['corporation_name']
                hashreport['url'] = 'https://zkillboard.com/kill/' + str(killmail['kill_id'])
                hashtotals[killmail['fithash']]['data'].append(hashreport)
    return hashtotals


