
# extract pbr mat from gltf models
import gltflib
import json


resource_folder_path='C:/LensFlare/createdScenes/'
# /collectedScenes/generatedGridScene/thickgrid_example/
#/collectedScenes/generatedGridScene/thickerwall_grid/
file_path=resource_folder_path+'/bunny_hole/';

model_name='bunny_hole';
json_file=file_path+model_name+'.gltf';

gltf_model = gltflib.GLTF.load(json_file)
gltf_mat_data=gltf_model.model.materials
all_images_list=gltf_model.model.images
all_textures_list=gltf_model.model.textures
pbr_material=[]
for mat_id in range(0,len(gltf_mat_data)):

    current_mat=gltf_mat_data[mat_id]
    mat_info={};
    mat_info['name']=current_mat.name
    print(mat_info['name'])
    if current_mat.name=='stone_stairs':
        print('debug current mat')
    # albedo map
    if current_mat.pbrMetallicRoughness.baseColorTexture is None:
        mat_info['has_albedo_tex']=False
        mat_info['albedo_constant']=current_mat.pbrMetallicRoughness.baseColorFactor
        mat_info['albedo_tex_file'] =''

    else:
        mat_info['has_albedo_tex']=True
        mat_info['albedo_constant']=[0.5,0.5,0.5,1]
        tex_id=current_mat.pbrMetallicRoughness.baseColorTexture.index
        img_id=all_textures_list[tex_id].source
        mat_info['albedo_tex_file']=all_images_list[img_id].uri

    # normal map
    if current_mat.normalTexture is None:
        mat_info['has_normal_tex'] = False
        mat_info['normal_tex_file'] = ''
    else:
        mat_info['has_normal_tex'] = True
        tex_id = current_mat.normalTexture.index
        img_id = all_textures_list[tex_id].source
        mat_info['normal_tex_file'] = all_images_list[img_id].uri

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
        img_id = all_textures_list[tex_id].source

        mat_info['emissive_tex_file'] =all_images_list[img_id].uri
        mat_info['emissive_color'] =[0,0,0]
        mat_info['emissive_strength'] = 1.0

    # metallic and roughness
    if current_mat.pbrMetallicRoughness.metallicRoughnessTexture is None:
        mat_info['has_metallicRoughness_tex'] = False
        mat_info['metallicRoughness_tex_file'] = ''

    else:
        mat_info['has_metallicRoughness_tex'] = True
        tex_id=current_mat.pbrMetallicRoughness.metallicRoughnessTexture.index
        img_id = all_textures_list[tex_id].source
        mat_info['metallicRoughness_tex_file'] = all_images_list[img_id].uri

    if current_mat.pbrMetallicRoughness.metallicFactor is None:
        mat_info['with_metallic'] = True
        mat_info['metallic_factor'] = -1.0
    else:
        mat_info['with_metallic'] = False
        mat_info['metallic_factor'] = current_mat.pbrMetallicRoughness.metallicFactor

    if current_mat.pbrMetallicRoughness.roughnessFactor is None:
        mat_info['with_roughness'] = True
        mat_info['roughness_factor'] = 0.0
    else:
        mat_info['with_roughness'] = False
        mat_info['roughness_factor'] = current_mat.pbrMetallicRoughness.roughnessFactor


    pbr_material.append(mat_info)

# save the extracted material info
output_file=file_path+'pbrmat.json'
with open(output_file,'w') as f:
    json.dump(pbr_material, f,indent=4,sort_keys=True)
# loop material name
print('export pbr mat done...\n')
# output mat name with albedo, normal, metalness, roughness

