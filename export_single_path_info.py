import bpy

path_pos=bpy.data.objects["NurbsPath"].location

print(path_pos)
curve=bpy.data.curves['NurbsPath.001']

begin_point=curve.splines[0].points[0].co
end_point=curve.splines[0].points[1].co

print(begin_point)
begin_pos=[path_pos[x]+begin_point[x] for x in range(3)]
end_pos=[path_pos[x]+end_point[x] for x in range(3)]


print('"begin_pos":',begin_pos,',')
print('"end_pos":',end_pos)
