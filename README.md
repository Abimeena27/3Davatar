Blender Depth Map to 3D Object Converter
Overview

This project is a Python script designed to run in Blender, a 3D computer graphics software. The script takes depth maps as input, generates 3D objects based on the depth information, and exports the scene as a glTF (GL Transmission Format) file.
Requirements

    Blender: Make sure you have Blender installed on your system. The script is written to be executed within Blender's Python environment.

    OpenCV: The script utilizes the OpenCV library for reading and processing depth maps. Ensure that OpenCV is installed in your Python environment.

Usage

    Open Blender and create a new project.

    Copy and paste the provided Python script into Blender's text editor.

    Adjust the depth_map_path_front and depth_map_path_back variables to point to the paths of your front and back depth map images.

    Run the script in Blender.

    The script will create two 3D objects based on the depth maps, arrange them in the scene, and export the scene as a glTF file.

Script Explanation

    The script loads depth maps using OpenCV and creates two 3D mesh objects in Blender based on the depth information.

    It checks and deletes default cube and light objects in the Blender scene.

    The front and back objects are created with vertices and faces generated from the depth maps.

    The script exports the scene as a glTF file for further use.

File Descriptions

    dm.py: The main Python script for converting depth maps to 3D objects in Blender.
