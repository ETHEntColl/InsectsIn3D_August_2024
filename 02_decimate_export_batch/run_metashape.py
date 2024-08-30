# This file handles the interaction with metashape and all manipulations to the glb file.
import Metashape
from math import cos, sin, pi
from pygltflib import GLTF2
from settings import max_face, metallic, roughness
from medof_xml import medof_xml

def run_metashape(file_name):
	# Open document
	doc = Metashape.Document()
	doc.open(file_name)
	chunk = doc.chunk
	
	# Decimate
	if len(chunk.model.faces) > max_face:
		chunk.decimateModel(face_count=max_face)

		# Recalculate Texture
		chunk.buildUV(mapping_mode=Metashape.GenericMapping)
		chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)

	# Rotate 180 degrees around z(?)-axis
	Rz_180 = Metashape.Matrix.Rotation(Metashape.Matrix([[cos(pi), -sin(pi), 0],[sin(pi), cos(pi), 0], [0, 0, 1]]))
	chunk.transform.matrix = Rz_180 * chunk.transform.matrix

	crs1 = Metashape.CoordinateSystem('LOCAL_CS["Local Coordinates (mm)",LOCAL_DATUM["Local Datum",0],UNIT["millimetre",0.001,AUTHORITY["EPSG","1025"]]]')

	# Export
	chunk.exportModel(path=file_name.rstrip('psx') + 'glb', binary=True, precision=6, 
					texture_format = Metashape.ImageFormatJPEG, save_texture=True, save_uv=True, 
					save_normals=True, save_colors=False, save_alpha=True, colors_rgb_8bit=True,
					format=Metashape.ModelFormatGLTF, gltf_y_up=True, crs=crs1)
	
	camera_path = ("\\").join(file_name.split("\\")[:-2]) + "\\cameras.xml"
	chunk.exportCameras(path=camera_path)

	medof_xml(camera_path)

	# Fix metall/roughness (using blender preset)
	gltf = GLTF2.load(file_name.rstrip('psx') + 'glb')
	gltf.extensionsUsed = ['KHR_materials_specular', 'KHR_materials_ior']
	gltf.materials[0].extensions = {'KHR_materials_specular': {'specularFactor': 0}, 'KHR_materials_ior': {'ior': 1.4500000476837158}}
	gltf.materials[0].doubleSided = True
	gltf.materials[0].pbrMetallicRoughness.metallicFactor = metallic
	gltf.materials[0].pbrMetallicRoughness.roughnessFactor = roughness
	gltf.materials[0].pbrMetallicRoughness.baseColorFactor = [1.0,1.0,1.0,1.0]
	gltf.materials[0].alphaMode = "MASK"

	# Final Export
	gltf.save(file_name.rstrip('psx') + 'glb')