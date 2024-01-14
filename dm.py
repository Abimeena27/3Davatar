import bpy
import cv2

# Load the depth maps
depth_map_path_front = 'output_image.png'
depth_map_path_back = 'output_image.png'

depth_map_front = cv2.imread(depth_map_path_front, cv2.IMREAD_GRAYSCALE)
depth_map_back = cv2.imread(depth_map_path_back, cv2.IMREAD_GRAYSCALE)

# Check if the depth maps are loaded successfully
if depth_map_front is None or depth_map_back is None:
    print(f"Error: Unable to load one or both of the depth maps")
else:
    # Check if the default cube exists and delete it
    if 'Cube' in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Cube'].select_set(True)
        bpy.ops.object.delete()

    # Check if the default light exists and delete it
    if 'Light' in bpy.data.objects:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Light'].select_set(True)
        bpy.ops.object.delete()

    # Create a new mesh data block for the front object
    mesh_front = bpy.data.meshes.new("FrontMesh")
    obj_front = bpy.data.objects.new("FrontObject", mesh_front)
    bpy.context.collection.objects.link(obj_front)

    # Set the front object as the active object
    bpy.context.view_layer.objects.active = obj_front
    obj_front.select_set(True)

    # Create vertices, faces, and normals based on the front depth map
    vertices_front = []
    faces_front = []

    for y in range(depth_map_front.shape[0]):
        for x in range(depth_map_front.shape[1]):
            depth_value = depth_map_front[y, x] / 10.0  # Scale down the depth values
            vertices_front.append((x, y, depth_value))

    # Create faces with inverted order for the front side
    for y in range(depth_map_front.shape[0] - 1):
        for x in range(depth_map_front.shape[1] - 1):
            current = y * depth_map_front.shape[1] + x
            next_row = (y + 1) * depth_map_front.shape[1] + x
            faces_front.append((next_row, next_row + 1, current + 1, current))

    # Create the front mesh
    mesh_front.from_pydata(vertices_front, [], faces_front)
    mesh_front.update()

    # Duplicate the front object
    bpy.ops.object.duplicate(linked=False)
    obj_back = bpy.context.active_object
    obj_back.name = "BackObject"

    # Create vertices, faces, and normals based on the back depth map
    vertices_back = []
    faces_back = []

    for y in range(depth_map_back.shape[0]):
        for x in range(depth_map_back.shape[1]):
            depth_value = depth_map_back[y, x] / 10.0  # Scale down the depth values
            vertices_back.append((x, y, depth_value))

    # Create faces with inverted order for the back side
    for y in range(depth_map_back.shape[0] - 1):
        for x in range(depth_map_back.shape[1] - 1):
            current = y * depth_map_back.shape[1] + x
            next_row = (y + 1) * depth_map_back.shape[1] + x
            faces_back.append((next_row, next_row + 1, current + 1, current))

    # Create the back mesh
    mesh_back = bpy.data.meshes.new("BackMesh")
    obj_back.data = mesh_back
    mesh_back.from_pydata(vertices_back, [], faces_back)
    mesh_back.update()

    # Adjust the positions of the front and back objects as needed
    obj_front.location = (0, 0, 0)
    obj_back.location = (0, 0, -3)  # Adjust the z-coordinate as needed

    # Export as glTF
    output_path = '/home/dell/Desktop/op.blend'
    bpy.ops.wm.save_as_mainfile(filepath=output_path)

    print(f"Exported glTF file to: {output_path}")

