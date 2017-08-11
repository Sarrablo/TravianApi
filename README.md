# TravianApi
Guerrilla Api for Travian. Why Guerrilla? Because is not oficcial, scraping bassed api. 
 
## What can i do with that?
Actually, i have implemented the construction functionality. You can build resources, build builgings (no, it's not redundant), consult actual production, consult actual queue, map resoures and map buildings.

# Methods:

## General
<br/>
Constructor:<br/>

```api = TravianGuerrillaApi("user_example","password_example", "server_example","domain_example")```

<br/>Initialize the api<br/>

```loggin(user, pasword)```
<br/>Log in the travian webpage ( constructor do that)
<br/>

## Resources and buildings
```actual_queue()```
<br/>Show the actual construction queue
<br/>

```build_resource(resource_id)```
<br/> Build (if its posible) a resource (dorf1) in the resource_id position<br/>

```show_avilable_building(solar_id,category_id=1):```
<br/> Show the possible buildings for a certain solar, category is arbitrari, default 1 (1 - infraestructure, 2 - military, 3 - resources)<br/>

```build_building(solar_id, building_id)```
<br/> If posible, build a certain building in the specified solar <br/>

```upgrade_building(solar_id):```
<br/> If possible, upgrade the building in the speified solar<br/>

```get_actual_production()```
<br/> Show the actual resource production <br/>

```map_resources()```
<br/> Show the actual resources (dorf1) ,their levels and the id <br/>

```map_buildings()```
<br/> Show the actual buildings (dorf2) ,their levels and the id <br/>

```actual_resources()```
<br/> Show the actual balance of the resources <br/>

## Units production
```show_available_units(solar_id)```
<br/> Show the actual available units (infantry) <br/>

```create_units(solar_id,t1,t2,t3)```
<br/> Create units in the barracks, only infantry (on construction)<br/>

## Units movements
```get_next_atack()```
<br/> Prints the time to the next atack (on construction)<br/>

```send_attack(coord, mode='4', t1=0, t2=0, t3=0, t4=0, t5=0, t6=0, t7=0, t8=0, t9=0, t10=0)```
<br/> Send attack to the specified coordenates:<br/>
Usage
 - coord -> ['88','-55']
 - mode:
   - '2' -> reinforcement
   - '3' -> normal attack
   - '4' -> raid attack
