import bpy
#--------save all materials name------------------
print('-----------all material name---------------------')
def followLinks(node_in):
    for n_inputs in node_in.inputs:
        for node_links in n_inputs.links:
            print("going to " + node_links.from_node.name)
#            followLinks(node_links.from_node)
def findTexLink(n_inputs):
        
        for node_links in n_inputs.links:
            print("going to " + node_links.from_node.name)
            findTexLink(node_links.from_node)

mat_info_list=[];

for each_mat in bpy.data.materials:
    print(each_mat.name)    
    mat_info={};
    mat_info['name']=each_mat.name
    mat_info['use_node']=each_mat.use_nodes
    if(each_mat.use_nodes):
        mat_node=each_mat.node_tree.nodes["Principled BSDF"]
        
#        followLinks(mat_node);
        metallic=mat_node.inputs[4].default_value
        mat_info['metallic']=metallic
        specular=mat_node.inputs[5].default_value
        mat_info['specular']=specular
        roughness=mat_node.inputs[7].default_value
        mat_info['roughness']=roughness
        
        mat_info['emissive_use_tex']=mat_node.inputs[17].is_linked
        emissive_color=mat_node.inputs[17].default_value
        mat_info['emissive_color']=[emissive_color[0],emissive_color[1],emissive_color[2]]
    
        emissive_inten=mat_node.inputs[18].default_value
        mat_info['emissive_inten']=emissive_inten
        
        color_vec=mat_node.inputs[0].default_value
        mat_info['color']=[color_vec[0],color_vec[1],color_vec[2]]
                
       
    else:
        metallic=each_mat.metallic
        mat_info['metallic']=metallic
        specular=each_mat.specular_intensity
        mat_info['specular']=specular
        roughness=each_mat.roughness
        mat_info['roughness']=roughness
        color_vec=each_mat.diffuse_color
        mat_info['color']=[color_vec[0],color_vec[1],color_vec[2]]
        
    mat_info_list.append(mat_info);        

#    ------------------for all objects-------------------------------
objs_type='scene_objects'
obj_mat_list=[];
for collection in bpy.data.collections:
    if collection.name==objs_type:
        

        for obj in collection.all_objects:
            obj_mat_info={};
            obj_mat=obj.active_material
            obj_mat_info['name']=obj.name;
            obj_mat_info['mat_name']=obj_mat.name;
            obj_mat_list.append(obj_mat_info);
            
            print(obj_mat.name);
#------------------save materail info-------------------------------                      
blender_mat_info={};
blender_mat_info['all_mat']=mat_info_list    
blender_mat_info['obj_mat']=obj_mat_list       
 

print('----write to json file-----')
import json
import os
directory_path = os.getcwd()
print('current work path:',directory_path)

with open('objects_mat.json','w') as f:
    json.dump(blender_mat_info, f,indent=4,sort_keys=True)
print('----objects mat done-----')
     