from datetime import date
import bs4 as bs
import urllib.request

class Schedule:
    def __init__(self, link, group, semigroup=None, day=None):
        self.source = link
        self.group = group
        self.day = day
        self.semigroup = semigroup

    def getSmartSchedule(self):
        print(self.source)
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
            if data != {}:
                final.append(data)
                                
        return final