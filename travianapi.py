from robobrowser import RoboBrowser
import re
from bs4 import BeautifulSoup
class TravianGuerrillaApi:

    def __init__(self, user, pasw, server):
        self.browser = RoboBrowser(history=True,parser='html.parser')
        self.browser.open('https://www.travian.net/')
        self.server = server.strip()
        self.loggin(user, pasw)

    def loggin(self, user, pasw):
        url = 'https://%s.travian.net/'%(self.server)
        self.browser.open(url)
        logging_form = self.browser.get_form(action="dorf1.php")
        

        logging_form.fields["password"].value=pasw
        logging_form.fields["name"].value=user

        self.browser.submit_form(logging_form)

    def show_actual_page(self):
        page = self.browser.parsed
        print(page)

    def open_page(self, url):
        self.browser.open(url)

    def actual_queue(self):
        url = 'https://%s.travian.net/dorf1.php'%(self.server)
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
            print("Empty queue")
            return "Empty queue"
    def build_resource(self, resource_id):
        try:
            self.open_page('https://%s.travian.net/build.php?id=%s'%(self.server, resource_id))
            onclick = self.browser.select('.green.build')[0].attrs['onclick']
            link = re.match(".*'(.*)'.*", onclick).group(1)
            url = 'https://%s.travian.net/%s'%(self.server, link)
            self.open_page(url)
        except:
            print("Full Queue")

    def show_avilable_building(self,solar_id,category_id=1):
        self.open_page('https://%s.travian.net/build.php?id=%s&category=%s'%(self.server, solar_id, category_id))
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
            self.open_page('https://%s.travian.net/build.php?id=%s&category=1'%(self.server, solar_id))
            soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
            code = re.findall('c=.*\Z',re.match(".*'(.*)'.*",soup.find("button",{'class':'green new'}).attrs["onclick"]).group(1))[0][2:]
        
            self.open_page('https://%s.travian.net/dorf2.php?a=%s&id=%s&c=%s'%(self.server, building_id, solar_id, code))
        except:
            print("Full Queue")

    def upgrade_building(self, solar_id):
        try:
            self.open_page('https://%s.travian.net/build.php?id=%s'%(self.server, solar_id))
            soup = BeautifulSoup(str(self.browser.parsed), 'html.parser')
            link = re.match(".*'(.*)'.*",soup.find("button",{'class':'green build'}).attrs["onclick"]).group(1)
            url = 'https://%s.travian.net/%s'%(self.server, link)
            self.open_page(url)
        except:
            print("Full Queue/Unavailable")


    def get_actual_production(self):
        url = 'https://%s.travian.net/dorf1.php'%(self.server)
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
        url = 'https://%s.travian.net/dorf1.php'%(self.server)
        self.open_page(url)
        resource_map = self.browser.find(id="rx").find_all("area")
        for item in resource_map:
            try:
                print('%s -> %s'%(re.findall('\d+\Z',item['href'])[0],item['alt']))
            except:
                pass
    def map_buildings(self):
        url = 'https://%s.travian.net/dorf2.php'%(self.server)
        self.open_page(url)
        building_map = self.browser.find(id="clickareas").find_all("area")
        for item in building_map:
            try:
                print('%s -> %s'%(re.findall('\d+\Z',item['href'])[0],item['alt'].split('||')[0].replace('<span class="level">','').replace('</span>','')))
            except:
                pass

    def actual_resources(self):
        url = 'https://%s.travian.net/dorf1.php'%(self.server)
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


class Resource:
    def __init__(self,resource,amount):
        self.resource = resource
        self.amount = amount
