class Configuration:
    def __init__(self):
        self.__webUrl = 'http://www.cs.ubbcluj.ro/files/orar/'

    def __matchGroup(self, title):
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
    
    def getWebUrl(self):
        print(self.__webUrl)
        return self.__webUrl

    def completeWebUrl(self, year, semester, group):
        self.__webUrl = self.__webUrl + year + '-' + semester + '/tabelar/' + self.__matchGroup(group)+".html"
        print(self.__webUrl)