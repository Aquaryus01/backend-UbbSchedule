from flask import Flask, request
from flask_cors import CORS, cross_origin
from Configuration import Configuration
from Controller.scheduleController import ScheduleController
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/schedule', methods=['GET'])
@cross_origin()
def getTable():

        group = request.args.get('group')
        semigroup = request.args.get('semigroup')
        semester = request.args.get('semester')
        year = request.args.get('year')
        day = request.args.get('day')
        
        conf = Configuration()
        conf.completeWebUrl(year,semester, group)
        
        link = conf.getWebUrl()
        linkRoom = conf.getWebUrlRoom()

        scCon = ScheduleController(group,semester,year,link,linkRoom,semigroup)
        return scCon.getSmartSchedule()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
