
# extract pbr mat from gltf models
import gltflib
import json

resource_folder_path='C:/LensFlare/createdScenes/collectedScenes/'
file_path=resource_folder_path+'/PBRTestScene/NormalMapTest/';

model_name='normalmap_wall';
json_file=file_path+model_name+'.gltf';

gltf_model = gltflib.GLTF.load(json_file)
gltf_mat_data=gltf_model.model.materials
all_images_list=gltf_model.model.images

pbr_material=[]
for mat_id in range(0,len(gltf_mat_data)):

    current_mat=gltf_mat_data[mat_id]
    mat_info={};
    mat_info['name']=current_mat.name

    # albedo map
    if current_mat.pbrMetallicRoughness.baseColorTexture is None:
        mat_info['has_albedo_tex']=False
        mat_info['albedo_constant']=current_mat.pbrMetallicRoughness.baseColorFactor
        mat_info['albedo_tex_file'] =''

    else:
        mat_info['has_albedo_tex']=True
        mat_info['albedo_constant']=[0.5,0.5,0.5,1]
        albedo_tex_id=current_mat.pbrMetallicRoughness.baseColorTexture.index
        mat_info['albedo_tex_file']=all_images_list[albedo_tex_id].uri

    # normal map
    if current_mat.normalTexture is None:
        mat_info['has_normal_tex'] = False
        mat_info['normal_tex_file'] = ''
    else:
        mat_info['has_normal_tex'] = True
        normal_tex_id = current_mat.normalTexture.index
        mat_info['normal_tex_file'] = all_images_list[normal_tex_id].uri

    # emissive map
    if current_mat.emissiveTexture is None:
        mat_info['has_emissive_tex'] = False
        mat_info['emissive_tex_file'] = ''
        if current_mat.emissiveFactor is None:
            mat_info['emissive_color']=[0,0,0]
        else:
            mat_info['emissive_color']=current_mat.emissiveFactor

        mat_info['emissive_strength'] =1.0
    else:
        mat_info['has_emissive_tex'] = True
        tex_id= current_mat.emissiveTexture.index
        mat_info['emissive_tex_file'] =all_images_list[tex_id].uri
        mat_info['emissive_color'] =[0,0,0]
        mat_info['emissive_strength'] = 1.0

    # metallic and roughness
    if current_mat.pbrMetallicRoughness.metallicRoughnessTexture is None:
        mat_info['has_metallicRoughness_tex'] = False
        mat_info['metallicRoughness_tex_file'] = ''

    else:
        mat_info['has_metallicRoughness_tex'] = True
        tex_id= current_mat.pbrMetallicRoughness.metallicRoughnessTexture.index
        mat_info['metallicRoughness_tex_file'] = all_images_list[tex_id].uri

    if current_mat.pbrMetallicRoughness.metallicFactor is None:
        mat_info['metallic_factor'] = 0.0
    else:
        mat_info['metallic_factor'] = current_mat.pbrMetallicRoughness.metallicFactor
    if current_mat.pbrMetallicRoughness.roughnessFactor is None:
        mat_info['roughness_factor'] = 0.0
    else:
        mat_info['roughness_factor'] = current_mat.pbrMetallicRoughness.roughnessFactor
    print(mat_info['name'])


    pbr_material.append(mat_info)

# save the extracted material info
output_file=file_path+model_name+'_pbrmat.json'
with open(output_file,'w') as f:
    json.dump(pbr_material, f,indent=4,sort_keys=True)
# loop material name
print('export pbr mat done...\n')
# output mat name with albedo, normal, metalness, roughness

