import bpy

glow_objs_type='glow_objs'
for collection in bpy.data.collections:
   if collection.name==glow_objs_type:
        #unselect all objs
        for obj in collection.all_objects:
            obj.select_set(False)   
        glow_objs_list=[];
       
        for obj in collection.all_objects:
            info_json={};
            #convert to a Y-axis position, because vertexes positions are in Y-axis            
            info_json['loc']=[obj.location[0],obj.location[2],-1*obj.location[1]]
            info_json['scale']=[obj.scale[0],obj.scale[2],-1*obj.scale[1]]
            info_json['name']=obj.name
    
            color_vec=bpy.data.materials[obj.name].node_tree.nodes["Principled BSDF"].inputs[0].default_value
            info_json['color']=[color_vec[0],color_vec[1],color_vec[2]]
            
            glow_objs_list.append(info_json)
 
         
            print("obj: ", obj.name)
            print("Loc:",obj.location)
            obj.select_set(True)
            bpy.ops.export_scene.obj(filepath='./'+obj.name+'.obj',
                use_selection=True,axis_up='Y')
            obj.select_set(False)
import json
with open('glow_objs_info.json','w') as f:
    json.dump(glow_objs_list, f)
    
     