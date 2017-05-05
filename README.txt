fpapi

This api connects to my database that records all deaths from zkillboard and parses the results via applied filters

Thanks to Squizz for providing the redisq zkillboard queue, giving my database a much needed source of food

usage:
/alliance/<allianceid>
and
/corporation/<corporationid>
    
    default request will retrieve last 24 hours of kill data

parameters:

    ?system=<systemid>      retrieve only kill data from specified system id

    ?days=<value>           retrieve only kill data from last value*24 before current time - value can be decimal, no greater than 6 days

    ?date=<YYYY-mm-dd>      retrieve only kill data from input date 11:05 GMT to next day 11:05 GMT

    the following combinations work

    ?system=<systemid>?days=<value>
    ?system=<systemid>?date=<YYYY-mm-dd> 

/doctrines

    default request will retrieve last 24 hours of doctrines and provide urls to killmails

parameters:

    ?date=<YYYY-mm-dd>      retrieve only kill data from input date 11:05 GMT to next day 11:05 GMT