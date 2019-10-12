import bs4 as bs
import urllib.request
from datetime import date
from Classes.schedule import Schedule
import json

class ScheduleController:
    def __init__(self,group,semester,year,link,linkRoom=None,semigroup=None,day=None):
        self.group = group
        self.semester = semester
        self.year = year
        self.link = link
        self.semigroup = semigroup
        self.linkRoom = linkRoom

    def getSmartSchedule(self):
        schedule = Schedule(self.link, self.group, self.semigroup, self.linkRoom)
        data = schedule.getSmartSchedule()
        roomsData = schedule.getRooms()

        data = self.__sortScheduleByFormation(data)
        data = self.__sortScheduleByWeek(data)
        data = self.__atachLegend(roomsData, data)
        data = self.__sortScheduleByDays(data)


        app_json = json.dumps(data)
        return app_json

    def __atachLegend(self, roomsData, data):
        for roomNameSchedule in data:
            for roomName in roomsData:
                if roomName["room"] == roomNameSchedule["room"]:
                    roomNameSchedule["adress"] = roomName["adress"]
        return data

    def __sortScheduleByDays(self, infos):
        data = dict()
        data["Luni"] = []
        data["Marti"] = []
        data["Miercuri"] = []
        data["Joi"] = []
        data["Vineri"] = []

        for element in infos:
            data[element["day"]].append(element)

        return data
    def __sortScheduleByFormation(self, data):
        dataAll = []
        for element in data:
            if element["formation"] != self.group + "/" + self.__changeSemi(self.semigroup):
                dataAll.append(element)
        return dataAll

    def __sortScheduleByWeek(self, data):
        dataAll = []
        week = self.__getWeekNumber()
        for element in data:
            if week == True and element["weekly"] != "sapt. 2":
                dataAll.append(element)
            elif week == False and element["weekly"] != "sapt. 1":
                dataAll.append(element)

        return dataAll

    def __getWeekNumber(self):
        #true  = saptamana para
        #false = saptamana impara
        dateFinal = date.today()
        dateStart = date(2019, 9, 30)
        nrDays = ((dateFinal - dateStart).days)
        dateNowName = date.today().strftime("%A")
        if nrDays // 7 % 2 == 0:
            if dateNowName=="Saturday" or dateNowName=="Sunday":
                return False
            return True
        else:
            if dateNowName=="Saturday" or dateNowName=="Sunday":
                return True
            return False

    def __changeSemi(self, nr):
        if nr == "1":
            return "2"
        return "1"
