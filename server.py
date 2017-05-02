"""api for totals"""
from flask import Flask, jsonify, request
import finds
#pylint: disable=C0301

app = Flask(__name__)
apphandle = finds.connect()

@app.route('/corporation/<int:corporationid>', methods=['GET'])
def get_by_corporation(corporationid):
    """get totals of all losses for a corporation over specified time period"""
    if request.args.get('system') != None and request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_days(apphandle,
                                                                             corporationid,
                                                                             request.args.get('system'),
                                                                             request.args.get('days'))
    elif request.args.get('system') != None and request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_date(apphandle,
                                                                             corporationid,
                                                                             request.args.get('system'),
                                                                             request.args.get('date'))
    elif request.args.get('system') != None:
        system = int(request.args.get('system'))
        (shiptotals, itemtotals, ammototals) = finds.corporation_system_oneday(apphandle,
                                                                               corporationid,
                                                                               request.args.get('system'))
    elif request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_days(apphandle,
                                                                      corporationid,
                                                                      request.args.get('days'))
    elif request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.corporation_date(apphandle,
                                                                      corporationid,
                                                                      request.args.get('date'))
    else:
        (shiptotals, itemtotals, ammototals) = finds.corporation_oneday(apphandle,
                                                                        corporationid)
    return jsonify({'shiptotals': shiptotals,
                    'itemtotals': itemtotals,
                    'ammototals': ammototals})

@app.route('/alliance/<int:allianceid>', methods=['GET'])
def get_by_alliance(allianceid):
    """get totals of all losses for a alliance over specified time period"""
    if request.args.get('system') != None and request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_days(apphandle,
                                                                          allianceid,
                                                                          request.args.get('system'),
                                                                          request.args.get('days'))
    elif request.args.get('system') != None and request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_date(apphandle,
                                                                          allianceid,
                                                                          request.args.get('system'),
                                                                          request.args.get('date'))
    elif request.args.get('system') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_system_oneday(apphandle,
                                                                            allianceid,
                                                                            request.args.get('system'))
    elif request.args.get('days') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_days(apphandle,
                                                                   allianceid,
                                                                   request.args.get('days'))
    elif request.args.get('date') != None:
        (shiptotals, itemtotals, ammototals) = finds.alliance_date(apphandle,
                                                                   allianceid,
                                                                   request.args.get('date'))
    else:
        (shiptotals, itemtotals, ammototals) = finds.alliance_oneday(apphandle,
                                                                     allianceid)
    return jsonify({'shiptotals': shiptotals,
                    'itemtotals': itemtotals,
                    'ammototals': ammototals})

@app.route('/doctrines', methods=['GET'])
# get doctrines by date or by last 24 hour time period
def get_doctrines():
    if request.args.get('date') != None:
        doctrines = finds.doctrines_date(apphandle, request.args.get('date'))
    else:
        # last 24 hours
        doctrines = finds.doctrines(apphandle)
    return jsonify(doctrines)

if __name__ == '__main__':
    app.run(debug=True)
