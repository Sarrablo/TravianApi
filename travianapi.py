from robobrowser import RoboBrowser
import re
from bs4 import BeautifulSoup

class TravianGuerrillaApi:

    def __init__(self, user, pasw, server, domain='net'):
        self.browser = RoboBrowser(history=True,parser='html.parser')
        self.browser.open('https://www.travian.net/')
        self.server = server.strip()
        self.domain = domain
        self.loggin(user, pasw)

    def loggin(self, user, pasw):
        url = 'https://%s.travian.%s/'%(self.server,self.domain)
        self.browser.open(url)
        logging_form = self.browser.get_form(action="dorf1.php")


        logging_form.fields["password"].value=pasw
        logging_form.fields["name"].value=user

        self.browser.submit_form(logging_form)

    def show_actual_page(self):
        page = self.browser.parsed
        print(page)

    def list_villages(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        villages = {}
        for item in self.browser.find('div', {'id':'sidebarBoxVillagelist'}).find('div',{'class':'innerBox content'}).find_all('li'):
            villages[item.find('a').find('div',{'class':'name'}).getText()] = re.search("\?.+=(\d+)&",item.find('a')['href']).group(1)
        return villages

    def set_village(self, village_id):
        url = 'https://%s.travian.%s/dorf1.php?newdid=%s&'%(self.server,self.domain, village_id)
        self.open_page(url)

    def show_available_units(self,solar_id):
        url = 'https://%s.travian.%s/build.php?id=%s'%(self.server, self.domain,solar_id)
        self.open_page(url)

        soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
        units = soup.find('div',{'class':'buildActionOverview trainUnits'}).find_all('div', {'class':'details'})
        for item in units:
            name = item.find('div',{'class':'tit'}).find('img')['alt']
            quant_available = item.find('a',{'onclick':re.compile(r"div.details")}).getText()
            print("%s -> %s Available"%(name,quant_available))

    def get_actual_units(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        troops = {}
        for item in self.browser.find('table',{'id':'troops'}).find_all('tr'):
            try:
                troops[item.find('td',{'class':'un'}).getText()] = item.find('td',{'class':'num'}).getText()
            except:
                pass
        return troops

    def create_units(self, solar_id, t1=0,t2=0,t3=0):
        url = 'https://%s.travian.%s/build.php?id=%s'%(self.server,self.domain,solar_id)
        self.open_page(url)
        try:
            search_form = self.browser.get_form(action=re.compile(r'build.php'))
            dic = {'t1':t1,'t2':t2,'t3':t3}
            for key, value in dic.items():
                try:
                    search_form.fields[key].value = value
                except:
                    pass
            self.browser.submit_form(search_form)
            return "Creating.."
        except:
            return "Unavailable"

    def send_attack(self, coord, mode='4', t1=0, t2=0, t3=0, t4=0, t5=0, t6=0, t7=0, t8=0, t9=0, t10=0):
        url = 'https://%s.travian.%s/build.php?id=39&tt=2'%(self.server,self.domain)
        self.open_page(url)
        try:
            search_form = self.browser.get_form(action=re.compile(r'build.php'))
            dic = {'t1':t1,'t2':t2,'t3':t3,'t4':t4,'t5':t5,'t6':t6,'t7':t7,'t8':t8,'t9':t9,'t10':t10}
            for key, value in dic.items():
                try:
                    search_form.fields[key].value = value
                except:
                    pass

            search_form.fields['x'].value = coord[0]
            search_form.fields['y'].value = coord[1]
            search_form.fields['c'].value = mode
            self.browser.submit_form(search_form)

            try:
                search_form = self.browser.get_form(action=re.compile(r'build.php'))
                self.browser.submit_form(search_form)
                print("Ok")
            except:
                print("Unavailable second layer")
        except:
            print("Unavailable general")


    def get_next_atack(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
        seconds = soup.find('table',{'id':'movements'}).find('span',{'class':'timer'})['value']
        m, s = divmod(int(seconds), 60)
        h, m = divmod(m, 60)

        print('%s -> %d:%02d:%02d'%(seconds, h, m, s))

    def open_page(self, url):
        try:
            self.browser.open(url)
        except Exception as e:
            print(e)
            print("problem on open_page")

    def is_busy(self):
        if self.actual_queue() == "Empty queue":
            return False
        else:
            return True

    def actual_queue(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        try:
            soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
            queue = soup.find('div',{'class':'boxes buildingList'}).find_all('li')
            for item in queue:
                soup = BeautifulSoup(str(item), 'html.parser')
                div_name = soup.find('div',{'class':'name'})
                print(div_name.getText().replace('"','').strip())
                div_duration = soup.find('div',{'class':'buildDuration'})
                print(div_duration.getText().replace('"','').replace('\t','').strip())
                return ("%s -> %s"%(div_name.getText().replace('"','').replace('\t','').strip(),div_duration.getText().replace('"','').strip()))
        except:
            return "Empty queue"

    def build_resource(self, resource_id):
        if not self.is_busy():
            try:
                self.open_page('https://%s.travian.%s/build.php?id=%s'%(self.server,self.domain, resource_id))
                onclick = self.browser.select('.green.build')[0].attrs['onclick']
                link = re.match(".*'(.*)'.*", onclick).group(1)
                url = 'https://%s.travian.%s/%s'%(self.server, self.domain, link)
                self.open_page(url)
            except:
                return "Unavailable"
        else:
            return "Full queue"

    def show_avilable_building(self,solar_id,category_id=1):
        self.open_page('https://%s.travian.%s/build.php?id=%s&category=%s'%(self.server,self.domain, solar_id, category_id))
        soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
        buildings = soup.find(id="build").find_all('div',{'class':'buildingWrapper'})
        for item in buildings:
            try:
                soup = BeautifulSoup(str(item), 'html.parser')
                label = soup.find('h2').getText().strip()
                link = re.match(".*'(.*)'.*",soup.find("button",{'class':'green new'}).attrs["onclick"]).group(1)
                print('%s -> %s'%( re.findall('\d+',link)[1], label))
            except:
                pass

    def build_building(self, solar_id, building_id ):
        try:
            self.open_page('https://%s.travian.%s/build.php?id=%s&category=1'%(self.server,self.domain, solar_id))
            soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
            code = re.findall('c=.*\Z',re.match(".*'(.*)'.*",soup.find("button",{'class':'green new'}).attrs["onclick"]).group(1))[0][2:]

            self.open_page('https://%s.travian.%s/dorf2.php?a=%s&id=%s&c=%s'%(self.server,self.domain, building_id, solar_id, code))
            return 'Ok'
        except:
            return 'Unavailable'

    def upgrade_building(self, solar_id):
        try:
            self.open_page('https://%s.travian.%s/build.php?id=%s'%(self.server, self.domain, solar_id))
            soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
            link = re.match(".*'(.*)'.*",soup.find("button",{'class':'green build'}).attrs["onclick"]).group(1)
            url = 'https://%s.travian.%s/%s'%(self.server,self.domain, link)
            self.open_page(url)
        except:
           return "Unavailable"


    def get_actual_production(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        production = self.browser.find(id="production").find_all("tr")
        for item in production:
            soup = BeautifulSoup(str(item), 'html.parser')
            res = soup.find("td",{'class':'res'})
            if res != None:
                resource = res.getText().strip()
            amo = soup.find("td",{'class':'num'})
            if amo != None:
                ammount = amo.getText().strip()
            if res != None and amo != None:
                print('%s -> %s'%(resource,ammount))

    def map_resources(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        resource_map = self.browser.find(id="rx").find_all("area")
        for item in resource_map:
            try:
                print('%s -> %s'%(re.findall('\d+\Z',item['href'])[0],item['alt']))
            except:
                pass
    def map_buildings(self):
        url = 'https://%s.travian.%s/dorf2.php'%(self.server,self.domain)
        self.open_page(url)
        building_map = self.browser.find(id="clickareas").find_all("area")
        for item in building_map:
            try:
                print('%s -> %s'%(re.findall('\d+\Z',item['href'])[0],item['alt'].split('||')[0].replace('<span class="level">','').replace('</span>','')))
            except:
                pass

    def actual_resources(self):
        url = 'https://%s.travian.%s/dorf1.php'%(self.server,self.domain)
        self.open_page(url)
        actual_resources = self.browser.find(id="stockBar").find_all("li")
        actual_resources_list=[]
        for item in actual_resources:
            soup = BeautifulSoup(str(item), 'html.parser')
            res = None
            amo = None
            res = soup.find("img",{'src':'img/x.gif'})
            if res != None:
                resource = res['alt'].strip()
            amo = soup.find("span",{'class':'value'})
            if amo != None:
                ammount = amo.getText().strip()
            if res != None and amo != None:
                print('%s -> %s'%(resource,ammount))
                actual_resources_list.append(Resource(resource,ammount))
        return actual_resources_list

    def get_alliance(self, alliance_id):
        tribes ={'tribe1':'Romans',
                'tribe2':'Teutons',
                'tribe3':'Gauls',
                'tribe4':'',
                'tribe5':'',
                'tribe6':'Egypthians',
                'tribe7':'Huns'}
        url = 'https://%s.travian.%s/allianz.php?aid=%s'%(self.server,self.domain,alliance_id)
        self.open_page(url)
        contain = self.browser.find('div',{'id':'details'}).find_all('tr')
        info = {}
        for item in contain:
            tag = item.find('th').getText()
            data = item.find('td').getText()
            info[tag] = data
        url = 'https://%s.travian.%s/allianz.php?aid=%s&action=members'%(self.server,self.domain,alliance_id)

        self.open_page(url)
        contain = self.browser.find('table',{'class':'allianceMembers'}).find_all('tr')
        members = []
        for item in contain:
            try:

                tribe = tribes[item.find('td', {'class':'tribe'}).find('div')['class'][1]]
                name = item.find('td', {'class':'player'}).find('a').getText()
                online = item.find('td', {'class':'player'}).find('img')['title']
                population = item.find('td', {'class':'population'}).getText()
                villages = item.find('td', {'class':'villages'}).getText()
                members.append(User(name, tribe, online, population, villages))
            except:
                print("Exception")
                pass

        return Alliance(info, members)

    def help(self):
        methods = '''Methods:
        loggin(user, pasword)
        actual_queue()
        build_resource(resource_id)
        show_avilable_building(solar_id,category_id=1)
        build_building(solar_id, building_id)
        upgrade_building(solar_id)
        get_actual_production()
        map_resources()
        map_buildings()
        actual_resources()
'''
        return(methods)

class Resource:
    def __init__(self,resource,amount):
        self.resource = resource
        self.amount = amount

class Alliance:
    def __init__(self, info, members):
        self.info = info
        self.members = members

class User:
    def __init__(self, name, tribe, online, population, villages):
        self.name = name
        self.tribe = tribe
        self.online = online
        self.population = population
        self.villages = villages
