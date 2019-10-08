from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from scrapTable import ScrapTable
app = Flask(__name__)
cors = CORS(app)
app.config['TESTING'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def getTable():

        group = request.args.get('group')
        semigroup = request.args.get('semigroup')
        semester = request.args.get('semester')
        year = request.args.get('year')
        day = request.args.get('day')
        link = 'http://www.cs.ubbcluj.ro/files/orar/'+ year + '-' + semester + '/tabelar/'

        if day != None:
            scrapTable = ScrapTable(link, group, semigroup, day)
            app_json = json.dumps(scrapTable.getTable())
            return app_json
        else:
            scrapTable = ScrapTable(link, group, semigroup)
            app_json = json.dumps(scrapTable.getTable())
            return app_json


# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0')
