import bpy

glow_objs_type='glow_objs'

#---------unselect all objs in all collections
for collection in bpy.data.collections:
     for obj in collection.all_objects:
            obj.select_set(False)   
    
    
for collection in bpy.data.collections:
   if collection.name==glow_objs_type:
        glow_objs_list=[];
       
        for obj in collection.all_objects:
            obj_mat=obj.active_material
            
            print("obj: ", obj.name)
            print("Loc:",obj.location)
            info_json={};
#            bpy.data.objects["gl_cube_0"].rotation_euler[0]
            #convert to a Y-axis position, because vertexes positions are in Y-axis            
            info_json['loc']=[obj.location[0],obj.location[2],-1*obj.location[1]]
            info_json['scale']=[obj.scale[0],obj.scale[2],obj.scale[1]]
            info_json['rotation']=[obj.rotation_euler[0],obj.rotation_euler[2],obj.rotation_euler[1]]
            
            info_json['name']=obj.name
    
            color_vec=bpy.data.materials[obj_mat.name].node_tree.nodes["Principled BSDF"].inputs[0].default_value
            info_json['color']=[color_vec[0],color_vec[1],color_vec[2]]
            
            glow_objs_list.append(info_json)
 
            
    
            obj.select_set(True)
            #translate the object to the origin
            origin_loc=obj.location.copy()
            print('origin_loc:',origin_loc)
            bpy.data.objects[obj.name].location[0]=0;
            bpy.data.objects[obj.name].location[1]=0;
            bpy.data.objects[obj.name].location[2]=0;  
            
            #---export obj            
         
            bpy.ops.export_scene.obj(filepath='./'+obj.name+'.obj',
                use_selection=True,axis_up='Y')
        
            #translate the object back
            bpy.data.objects[obj.name].location=origin_loc
            #--deselect this obj            
            obj.select_set(False)
import json
with open('glow_objs_info.json','w') as f:
    json.dump(glow_objs_list, f,indent=4,sort_keys=True)
    
     