import bpy
import cv2

depth_map_path_front = 'output_image.png'
depth_map_path_back = 'output_image.png'

depth_map_front = cv2.imread(depth_map_path_front, cv2.IMREAD_GRAYSCALE)
depth_map_back = cv2.imread(depth_map_path_back, cv2.IMREAD_GRAYSCALE)


if depth_map_front is None or depth_map_back is None:
    print(f"Error: Unable to load one or both of the depth maps")
else:
    if 'Cube' in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Cube'].select_set(True)
        bpy.ops.object.delete()
    if 'Light' in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Light'].select_set(True)
        bpy.ops.object.delete()
    mesh_front = bpy.data.meshes.new("FrontMesh")
    obj_front = bpy.data.objects.new("FrontObject", mesh_front)
    bpy.context.collection.objects.link(obj_front)

    bpy.context.view_layer.objects.active = obj_front
    obj_front.select_set(True)
    vertices_front = []
    faces_front = []

    for y in range(depth_map_front.shape[0]):
        for x in range(depth_map_front.shape[1]):
            depth_value = depth_map_front[y, x] / 10.0  
            vertices_front.append((x, y, depth_value))

    for y in range(depth_map_front.shape[0] - 1):
        for x in range(depth_map_front.shape[1] - 1):
            current = y * depth_map_front.shape[1] + x
            next_row = (y + 1) * depth_map_front.shape[1] + x
            faces_front.append((next_row, next_row + 1, current + 1, current))

    mesh_front.from_pydata(vertices_front, [], faces_front)
    mesh_front.update()

  
    bpy.ops.object.duplicate(linked=False)
    obj_back = bpy.context.active_object
    obj_back.name = "BackObject"

    vertices_back = []
    faces_back = []

    for y in range(depth_map_back.shape[0]):
        for x in range(depth_map_back.shape[1]):
            depth_value = depth_map_back[y, x] / 10.0  
            vertices_back.append((x, y, depth_value))

    for y in range(depth_map_back.shape[0] - 1):
        for x in range(depth_map_back.shape[1] - 1):
            current = y * depth_map_back.shape[1] + x
            next_row = (y + 1) * depth_map_back.shape[1] + x
            faces_back.append((next_row, next_row + 1, current + 1, current))

    mesh_back = bpy.data.meshes.new("BackMesh")
    obj_back.data = mesh_back
    mesh_back.from_pydata(vertices_back, [], faces_back)
    mesh_back.update()

    obj_front.location = (0, 0, 0)
    obj_back.location = (0, 0, -3)  

    output_path = '/home/dell/Desktop/op.blend'
    bpy.ops.wm.save_as_mainfile(filepath=output_path)

    print(f"Exported glTF file to: {output_path}")

