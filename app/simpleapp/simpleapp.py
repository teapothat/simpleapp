from bottle import route,run,template,post,request,response
from pymongo import MongoClient
import json
from datetime import datetime

@route('/')
@route('/dashboard')
def dashboard():
    return template('search.html')



@post('/api/v1/search')
def search():
    text = request.forms.get('text')
    try:
        before = _get_date_in_millis(request.forms.get('before'))
        after = _get_date_in_millis(request.forms.get('after'))
    except: 
        return "Date invalid; use format dd/mm/YY"

    datetime.strptime('24052010', "%d%m%Y").date()
    
    doodles = _search(text, before, after)
    response.content_type = 'application/json'
    return json.dumps(doodles)



def _search(text=None, before=None, after=None):
    client = MongoClient()
    db = client.simpleapp
    collection = db.doodles

    doodles = []
    cursor = collection.find( _get_query(text, before, after))
    for document in cursor:
        doodles.append(document)
    return doodles


def _get_date_in_millis(str_date):
    in_millis = None
    if str_date:
        dt = datetime.strptime(str_date, "%d/%m/%Y").strftime('%s')
        in_millis = int(dt)*1000

    return in_millis


def _get_query(text, before, after):
    querys = []
    if text:
        querys.append({"$text": {"$search": text}})

    time_subquery = {}
    if before:
        time_subquery['$lt'] = before
    if after:
        time_subquery['$gte'] = after
    if time_subquery:
        querys.append({'initiated': time_subquery})

    if not querys:
        return {}

    if len(querys) == 1:
        return querys[0]
    else:
        return {
            "$and": querys
        }
        


# Main server
import socket
host = socket.gethostbyname(socket.gethostname())
run(host=host, port=8080, debug=True)