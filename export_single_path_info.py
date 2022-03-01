import bpy
#path name
#curve name
path_name="horizontal_path"
curve_name=path_name+"_curve"

def coordSwitch(loc_vec):
    return [loc_vec[0],loc_vec[2],-1*loc_vec[1]]



path_pos=bpy.data.objects[path_name].location

print(path_pos)
curve=bpy.data.curves[curve_name]

begin_point=curve.splines[0].points[0].co
end_point=curve.splines[0].points[1].co
print('"begin_point":',begin_point,',')
print('"end_point":',end_point)

begin_pos=[path_pos[x]+begin_point[x] for x in range(3)]
end_pos=[path_pos[x]+end_point[x] for x in range(3)]

path_list=[];
single_path_info={};
single_path_info["name"]="cube_light_0";
single_path_info["begin_pos"]=coordSwitch(begin_pos);
single_path_info["end_pos"]=coordSwitch(end_pos);
single_path_info["speed_per_second"]=8e-1;

print('"begin_pos":',begin_pos,',')
print('"end_pos":',end_pos)

path_list.append(single_path_info);


print('----write to json file-----')
import json
with open('single_path_info.json','w') as f:
    json.dump(path_list, f,indent=4,sort_keys=True)