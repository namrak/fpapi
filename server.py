"""api for totals"""
from flask import Flask, jsonify, request
import finds

app = Flask(__name__)
mongohandle = finds.connect()

@app.route('/corporation/<int:corporationid>', methods=['GET'])
def get_by_corporation(corporationid):
    """get totals of all losses for a corporation over specified time period"""
    if request.args.get('system') != None and request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_days(mongohandle,
                                                                             corporationid,
                                                                             request.args.get('system'),
                                                                             request.args.get('days'))
    elif request.args.get('system') != None and request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_date(mongohandle,
                                                                             corporationid,
                                                                             request.args.get('system'),
                                                                             request.args.get('date'))
    elif request.args.get('system') != None:
        system = int(request.args.get('system'))
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_oneday(mongohandle,
                                                                               corporationid,
                                                                               request.args.get('system'))
    elif request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_days(mongohandle,
                                                                      corporationid,
                                                                      request.args.get('days'))
    elif request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_date(mongohandle,
                                                                      corporationid,
                                                                      request.args.get('date'))
    else:
        (shiptotals, itemtotals, ammototals) = finds.corporation_oneday(mongohandle,
                                                                        corporationid)
    return jsonify({'shiptotals': shiptotals,
                    'itemtotals': itemtotals,
                    'ammototals': ammototals})

@app.route('/alliance/<int:allianceid>', methods=['GET'])
def get_by_alliance(allianceid):
    """get totals of all losses for a alliance over specified time period"""
    if request.args.get('system') != None and request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_days(mongohandle,
                                                                          allianceid,
                                                                          request.args.get('system'),
                                                                          request.args.get('days'))
    elif request.args.get('system') != None and request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_date(mongohandle,
                                                                          allianceid,
                                                                          request.args.get('system'),
                                                                          request.args.get('date'))
    elif request.args.get('system') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_oneday(mongohandle,
                                                                            allianceid,
                                                                            request.args.get('system'))
    elif request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_days(mongohandle,
                                                                   allianceid,
                                                                   request.args.get('days'))
    elif request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_date(mongohandle,
                                                                   allianceid,
                                                                   request.args.get('date'))
    else:
        (shiptotals, itemtotals, ammototals) = finds.alliance_oneday(mongohandle,
                                                                     allianceid)
    return jsonify({'shiptotals': shiptotals,
                    'itemtotals': itemtotals,
                    'ammototals': ammototals})

@app.route('/doctrines', methods=['GET'])

def get_doctrines():
    """get doctrines by date or by last 24 hour time period"""
    if request.args.get('date') != None:
        doctrines = finds.doctrines_date(mongohandle, request.args.get('date'))
    else:
        doctrines = finds.doctrines(mongohandle)
    return jsonify(doctrines)

if __name__ == '__main__':
    app.run(debug=True)
