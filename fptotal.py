
def countships(ships, uships):
    """count ships"""
    shiptotals = []
    for ship in uships:
        typeid = int(ship)
        shiptotal = {}
        shiptotal['typeid'] = typeid
        count = 0
        for cship in ships:
            if cship == typeid:
                count += 1
                shipdata.pop(shipdata.index(cship))
        shiptotal['quantitylost'] = count
        shiptotals.append(shiptotal)
    return shiptotals

def countitems(itemdata, uitems):
    """count items"""
    itemtotals = []
    for item in uitems:
        typeid = int(item)
        itemtotal = {}
        itemtotal['typeid'] = typeid
        dropped = 0
        attached = 0
        quantitylost = 0
        for itemm in itemdata:
            if itemm['typeid'] == typeid:
                quantitylost += itemm['quantity']
                if itemm['attached'] is True:
                    attached += 1
                if itemm['dropped'] is True:
                    dropped += itemm['quantity']
                itemdata.pop(itemdata.index(itemm))
        itemtotal['quantityAttached'] = attached
        itemtotal['quantityDropped'] = dropped
        itemtotal['totalLost'] = quantitylost
        itemtotals.append(itemtotal)
    return itemtotals

def countammos(itemdata, uammos):
    """count ammos"""
    ammototals = []
    for ammoid in uammos:
        typeid = int(ammoid)
        ammototal = {}
        ammototal['typeid'] = typeid
        dropped = 0
        attached = 0
        quantitylost = 0
        for itemm in itemdata:
            if itemm['typeid'] == typeid:
                quantitylost += itemm['quantity']
                if itemm['attached'] is True:
                    attached += 1
                if itemm['dropped'] is True:
                    dropped += itemm['quantity']
                itemdata.pop(itemdata.index(itemm))
        ammototal['quantityAttached'] = attached
        ammototal['quantityDropped'] = dropped
        ammototal['quantityLost'] = quantitylost
        ammototals.append(ammototal)
    return ammototals

def countfits(hashdata, uhashes):
    """count fits"""
    reportarray = []
    for uhash in uhashes:
        count = 0
        report = {}
        outarray = []
        report['fithash'] = uhash
        for killmail in hashdata:
            if killmail['fitHash'] == uhash:
                count += 1
                kreport = {}
                kreport['url'] = killmail['killurl']
                kreport['corporation'] = killmail['corpName']
                outarray.append(kreport)
                hashdata.pop(hashdata.index(killmail))
        report['data'] = outarray
        report['count'] = count
        if count > 2:
            reportarray.append(report)
    return reportarray
