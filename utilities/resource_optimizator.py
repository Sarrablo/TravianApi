

class Woodcutter:
    def __init__(self, initial_level, final_level):
        wood = [0,40,65,110,185,310,520,870,1450,2420,4040]
        clay = [0,100,165,280,465,780,1300,2170,3625,6050,10105]
        iron = [0,50,85,140,235,390,650,1085,1810,3025,5050]
        crop = [0,60,100,165,280,465,780,1300,2175,3630,6060]
        self.cost = {'wood':wood, 'clay':clay, 'iron':iron, 'crop':crop}
        self.production = [
                            [3  ,0,0,0],
                            [7  ,0,0,0],
                            [13 ,0,0,0],
                            [21 ,0,0,0],
                            [31 ,0,0,0],
                            [46 ,0,0,0],
                            [70 ,0,0,0],
                            [98 ,0,0,0],
                            [140,0,0,0],
                            [203,0,0,0],
                            [280,0,0,0]
                            ]
        self.consumption = [0,2,3,4,5,6,8,10,12,14,16]
        self.actual_level = initial_level

    def get_production(self):
        return self.production[self.actual_level]

    def get_cost(self):
        return [self.cost['wood'][self.actual_level+1],
                self.cost['clay'][self.actual_level+1],
                self.cost['iron'][self.actual_level+1],
                self.cost['crop'][self.actual_level+1]]
    def upgrade(self):
        self.actual_level += 1

    def get_consumption(self):
        return self.consumption[self.actual_level]

        

    

class Clay_pit:
    def __init__(self, initial_level, final_level):
        wood = [0,80,135,225,375,620,1040,1735,2900,4840,8080]
        clay = [0,40,65,110,185,310,520,870,1450,2420,4040]
        iron = [0,80,135,225,375,620,1040,1735,2900,4840,8080]
        crop = [0,50,85,140,235,390,650,1085,1810,3025,5050]
        self.cost = {'wood':wood, 'clay':clay, 'iron':iron, 'crop':crop}
        self.production = [
                            [0  ,3  ,0,0],
                            [0  ,7  ,0,0],
                            [0  ,13 ,0,0],
                            [0  ,21 ,0,0],
                            [0  ,31 ,0,0],
                            [0  ,46 ,0,0],
                            [0  ,70 ,0,0],
                            [0  ,98 ,0,0],
                            [0  ,140,0,0],
                            [0  ,203,0,0],
                            [0  ,280,0,0]
                            ]
        self.consumption = [0,2,3,4,5,6,8,10,12,14,16]
        self.actual_level = initial_level

    def get_production(self):
        return self.production[self.actual_level]

    def get_cost(self):
        return [self.cost['wood'][self.actual_level+1],
                self.cost['clay'][self.actual_level+1],
                self.cost['iron'][self.actual_level+1],
                self.cost['crop'][self.actual_level+1]]
    def upgrade(self):
        self.actual_level += 1

    def get_consumption(self):
        return self.consumption[self.actual_level]

class Iron_mine:
    def __init__(self, initial_level, final_level):
        wood = [0,100,165,280,465,780,1300,2170,3625,6050,10105]
        clay = [0,80,135,225,375,620,1040,1735,2900,4840,8080]
        iron = [0,30,50,85,140,235,390,650,1085,1815,3030]
        crop = [0,60,100,165,280,465,780,1300,2175,3630,6060]
        self.cost = {'wood':wood, 'clay':clay, 'iron':iron, 'crop':crop}
        self.production = [
                            [0  ,0  ,3  ,0],
                            [0  ,0  ,7  ,0],
                            [0  ,0  ,13 ,0],
                            [0  ,0  ,21 ,0],
                            [0  ,0  ,31 ,0],
                            [0  ,0  ,46 ,0],
                            [0  ,0  ,70 ,0],
                            [0  ,0  ,98 ,0],
                            [0  ,0  ,140,0],
                            [0  ,0  ,203,0],
                            [0  ,0  ,280,0]
                            ]
        self.consumption = [0,3,5,7,9,11,13,15,17,19,21]
        self.actual_level = initial_level

    def get_production(self):
        return self.production[self.actual_level]

    def get_cost(self):
        return [self.cost['wood'][self.actual_level+1],
                self.cost['clay'][self.actual_level+1],
                self.cost['iron'][self.actual_level+1],
                self.cost['crop'][self.actual_level+1]]

    def upgrade(self):
        self.actual_level += 1

    def get_consumption(self):
        return self.consumption[self.actual_level]

class Cropland:
    def __init__(self, initial_level, final_level):
        wood = [0,70,115,195,325,545,910,1520,2535,4235,7070]
        clay = [0,90,150,250,420,700,1170,1950,3260,5445,9095]
        iron = [0,70,115,195,325,545,910,1520,2535,4235,7070]
        crop = [0,20,35,55,95,155,260,435,725,1210,2020]
        self.cost = {'wood':wood, 'clay':clay, 'iron':iron, 'crop':crop}
        self.production = [
                            [0  ,0  ,0  ,3  ],
                            [0  ,0  ,0  ,7  ],
                            [0  ,0  ,0  ,13 ],
                            [0  ,0  ,0  ,21 ],
                            [0  ,0  ,0  ,31 ],
                            [0  ,0  ,0  ,46 ],
                            [0  ,0  ,0  ,70 ],
                            [0  ,0  ,0  ,98 ],
                            [0  ,0  ,0  ,140],
                            [0  ,0  ,0  ,203],
                            [0  ,0  ,0  ,280]
                            ]
        self.consumption = [0,0,0,0,0,0,1,2,3,4,5]
        self.actual_level = initial_level

    def get_production(self):
        return self.production[self.actual_level]

    def get_cost(self):
        return [self.cost['wood'][self.actual_level+1],
                self.cost['clay'][self.actual_level+1],
                self.cost['iron'][self.actual_level+1],
                self.cost['crop'][self.actual_level+1]]

    def upgrade(self):
        self.actual_level += 1

    def get_consumption(self):
        return self.consumption[self.actual_level]


resources = [Woodcutter(0,5),
            Cropland(0,5),
            Woodcutter(0,5),
            Iron_mine(0,5),
            Clay_pit(0,5),
            Clay_pit(0,5),
            Iron_mine(0,5),
            Cropland(0,5),
            Cropland(0,5),
            Iron_mine(0,5),
            Iron_mine(0,5),
            Cropland(0,5),
            Cropland(0,5),
            Woodcutter(0,5),
            Cropland(0,5),
            Clay_pit(0,5),
            Woodcutter(0,5),
            Clay_pit(0,5)]

def get_lower(res_class):
    index = 0
    max_level = 99
    for resource in resources:
        if resource.__class__ is res_class:
            if resource.actual_level < max_level:
                max_level = resource.actual_level
                index = resources.index(resource)
    return index
            

def cicle(cicle):
    total_wood_cost = 0
    total_clay_cost = 0
    total_iron_cost = 0
    total_crop_cost = 0
    total_wood_prod = 0
    total_clay_prod = 0
    total_iron_prod = 0
    total_crop_prod = 0
    total_consumption = 0
    for res in resources:
        total_wood_cost += res.get_cost()[0]
        total_clay_cost += res.get_cost()[1]
        total_iron_cost += res.get_cost()[2]
        total_crop_cost += res.get_cost()[3]
        total_wood_prod += res.get_production()[0]
        total_clay_prod += res.get_production()[1]
        total_iron_prod += res.get_production()[2]
        total_crop_prod += res.get_production()[3]
        total_consumption += res.get_consumption()

    total_crop_prod -= total_consumption
    wood_percent = total_wood_cost / total_wood_prod
    clay_percent = total_clay_cost / total_clay_prod
    iron_percent = total_iron_cost / total_iron_prod
    crop_percent = total_crop_cost / total_crop_prod

    #print "%-6s|%-6s|%-6s|%-6s"%(total_wood_cost, total_clay_cost, total_iron_cost, total_crop_cost)
    #print "%-6s|%-6s|%-6s|%-6s"%(total_wood_prod, total_clay_prod, total_iron_prod, total_crop_prod)
    #print "------|------|------|------"
    #print "%-6s|%-6s|%-6s|%-6s"%(wood_percent, clay_percent, iron_percent, crop_percent)

    if clay_percent >= wood_percent and clay_percent >= iron_percent and clay_percent >= crop_percent:
        index = get_lower(Clay_pit)
        print cicle,"->",index+1,"-> Clay"
        resources[index].upgrade()

    elif wood_percent >= clay_percent and wood_percent >= iron_percent and wood_percent >= crop_percent:
        index = get_lower(Woodcutter)
        print cicle,"->",index+1,"-> Wood"
        resources[index].upgrade()

    elif iron_percent >= wood_percent and iron_percent >= clay_percent and iron_percent >= crop_percent:
        index = get_lower(Iron_mine)
        print cicle,"->",index+1,"-> Iron"
        resources[index].upgrade()

    elif crop_percent >= wood_percent and crop_percent >= clay_percent and crop_percent >= iron_percent:
        index = get_lower(Cropland)
        print cicle,"->",index+1,"-> Crop"
        resources[index].upgrade()


def start_life(times):
    cic = 0
    for i in range(times):
        cic += 1
        cicle(cic)

def restart_life():
    resources = [Woodcutter(0,5),Woodcutter(0,5),Woodcutter(0,5),Woodcutter(0,5),
             Clay_pit(0,5),Clay_pit(0,5),Clay_pit(0,5),Clay_pit(0,5),
             Iron_mine(0,5),Iron_mine(0,5),Iron_mine(0,5),Iron_mine(0,5),
             Cropland(0,5),Cropland(0,5),Cropland(0,5),Cropland(0,5),
             Cropland(0,5),Cropland(0,5)]
    
def get_levels():
    for res in resources:
        print res.__class__, res.actual_level



