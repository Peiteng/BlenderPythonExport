import bpy

path_pos=bpy.data.objects["NurbsPath"].location

print(path_pos)
curve=bpy.data.curves['NurbsPath.001']

begin_point=curve.splines[0].points[0].co
end_point=curve.splines[0].points[1].co

print(begin_point)
begin_pos=[path_pos[x]+begin_point[x] for x in range(3)]
end_pos=[path_pos[x]+end_point[x] for x in range(3)]

single_path_info={};
single_path_info["name"]="Sphere_0";
single_path_info["begin_pos"]=begin_pos;
single_path_info["end_pos"]=end_pos;

print('"begin_pos":',begin_pos,',')
print('"end_pos":',end_pos)
print('----write to json file-----')
import json
with open('single_path_info.json','w') as f:
    json.dump(single_path_info, f,indent=4,sort_keys=True)