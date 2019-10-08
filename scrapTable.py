import bs4 as bs
import urllib.request
from datetime import date

class ScrapTable:
    def __init__(self, link, group, semigroup, day=None):
        self.source = link + self.matchGroup(group)+".html"
        self.group = group
        self.day = day
        self.semigroup = semigroup

    def getWeekNumber(self):
        dateFinal = date.today()
        dateStart = date(2019, 9, 30)
        nrDays = ((dateFinal - dateStart).days)
        if nrDays // 7 % 2 == 0:
            return True
        else:
            return False

    def changeSemi(self, nr):
        if nr == "1":
            return "2"
        return "1"

    def matchGroup(self, title):
        if title[0]=="2":
            return str("I" + title[1])
        if title[0]=="1":
            return str("M" + title[1])
        if title[0]=="3":
            return str("MI" + title[1])
        if title[0]=="8":
            return str("MIE" + title[1])
        if title[0]=="4":
            return str("MM" + title[1])
        if title[0]=="5":
            return str("IM" + title[1])
        if title[0]=="6":
            return str("MIM" + title[1])
        if title[0]=="9":
            return str("IE" + title[1])
        if title[0]=="7":
            return str("IG" + title[1])

    def getTable(self):
        source = urllib.request.urlopen(self.source).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        index = int(self.group[2]) - 1
        table = soup.find_all('table')[index]

        final = []
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            data = dict()
            for i, column in enumerate(columns):
                if i == 0:
                    data["day"] = column.string
                if i == 1:
                    data["time"] = column.string
                if i == 2:
                    data["weekly"] = column.string
                if i == 3:
                    data["room"] = column.string
                if i == 4:
                    data["formation"] = column.string
                if i == 5:
                    data["type"] = column.string
                if i == 6:
                    data["title"] = column.string
                if i == 7:
                    data["author"] = column.string

            week = self.getWeekNumber()
            if data != {}:
                if self.day == None:
                    if data["formation"] != self.group + "/" + self.changeSemi(self.semigroup):
                        if week == True and data["weekly"] != "sapt. 2":
                            final.append(data)
                        elif week == False and data["weekly"] != "sapt. 1":
                            final.append(data)
                else:
                    if data["day"] == self.day:
                        if data["formation"] != self.group + "/" + self.changeSemi(self.semigroup):
                            if week == True and data["weekly"] != "sapt. 2":
                                final.append(data)
                            elif week == False and data["weekly"] != "sapt. 1":
                                final.append(data)
        return final
