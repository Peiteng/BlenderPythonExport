import bpy

collection_type='lights'
lights_list=[];
for obj in  bpy.data.lights:
    print('current light:',obj.type)
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
#   if collection.name==collection_type:
#        #unselect all objs
#        for obj in collection.all_objects:
#            obj.select_set(False)   
#        glow_objs_list=[];
#       
#        for obj in collection.all_objects:
#            info_json={};
#            bpy.data.lights["Lamp"].type
#            print(obj.type)
#            #convert to a Y-axis position, because vertexes positions are in Y-axis            
#            info_json['loc']=[obj.location[0],obj.location[2],-1*obj.location[1]]
#            info_json['scale']=[obj.scale[0],obj.scale[2],-1*obj.scale[1]]
#            info_json['name']=obj.name
#    
#            color_vec=bpy.data.materials[obj.name].node_tree.nodes["Principled BSDF"].inputs[0].default_value
#            info_json['color']=[color_vec[0],color_vec[1],color_vec[2]]
#            
#            lights_list.append(info_json)
#                   
#         
#            print("obj: ", obj.name)
#            print("Loc:",obj.location)
#            obj.select_set(True)
#            bpy.ops.export_scene.obj(filepath='./'+obj.name+'.obj',
#                use_selection=True,axis_up='Y')
#            obj.select_set(False)
print('----write to json file-----')
import json
with open('lights.json','w') as f:
    json.dump(lights_list, f,indent=4,sort_keys=True)
    
     