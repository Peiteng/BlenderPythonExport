import bpy

collection_type='lights'
lights_list=[];
for obj in  bpy.data.lights:
    print('current light:',obj.type)
    print('current name:',obj.name)
    info_json={};
    
    info_json['name']=obj.name
    info_json['type']=obj.type
    color_vec=obj.color
    info_json['color']=[color_vec[0],color_vec[1],color_vec[2]]
    loc_vec=bpy.data.objects[obj.name].location
    info_json['loc']=[loc_vec[0],loc_vec[2],-1*loc_vec[1]]
    info_json['power']=obj.energy
#    ------Point Light-------------
    if(obj.type=="POINT"):    
        info_json['dis']=obj.cutoff_distance

    if(obj.type=="SUN"):
        dir_vec=bpy.data.objects[obj.name].rotation_euler
        info_json['dir']=[dir_vec[0],dir_vec[2],-1*dir_vec[1]]
 
    lights_list.append(info_json)

print('----write to json file-----')
import os
directory_path = os.getcwd()
print('current work path:',directory_path)

import json
with open('lights.json','w') as f:
    json.dump(lights_list, f,indent=4,sort_keys=True)
    
     