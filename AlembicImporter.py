import unreal
from FileImporter import *

#TODO: Start every setting as None and create on the setters.
#TODO: self.import_settings declared as none in FileImporter.
class AlembicImporter(FileImporter):

    def __init__(self,alembic_path,asset_path,asset_name):
        super(AlembicImporter, self).__init__(alembic_path,asset_path,asset_name)
        self.import_settings = unreal.AbcImportSettings()
        self.compression_settings = unreal.AbcCompressionSettings()
        self.conversion_settings = unreal.AbcConversionSettings()
        self.geometry_cache_settings = unreal.AbcGeometryCacheSettings()
        self.material_settings = unreal.AbcMaterialSettings()
        self.normal_generation_settings = unreal.AbcNormalGenerationSettings()
        self.sampling_settings = unreal.AbcSamplingSettings()
        self.static_mesh_settings = unreal.AbcStaticMeshSettings()
        self.set_import_settings()

    #uses unreal default settings.
    def set_compression_settings(self,
                                 merge_meshes = False,
                                 bake_matrix_animation = True,
                                 base_calculation_type = unreal.BaseCalculationType.PERCENTAGE_BASED,
                                 percentage_of_total_bases = 100.0,
                                 max_number_of_bases = 0,
                                 minimum_number_of_vertex_influence_percentage = 0.0):
        
        self.compression_settings.merge_meshes = merge_meshes
        self.compression_settings.bake_matrix_animation = bake_matrix_animation
        self.compression_settings.base_calculation_type = base_calculation_type
        self.compression_settings.percentage_of_total_bases = percentage_of_total_bases
        self.compression_settings.max_number_of_bases = max_number_of_bases
        self.compression_settings.minimum_number_of_vertex_influence_percentage = minimum_number_of_vertex_influence_percentage

        return
    
    def get_compression_settings(self):
        return self.compression_settings
    
    '''
    Create Conversion settings. By default,it uses Maya's friendly settings.
    flip_u (bool): [Read-Write] Flag whether or not to flip the U channel in the Texture Coordinates
    flip_v (bool): [Read-Write] Flag whether or not to flip the V channel in the Texture Coordinates
    rotation (Vector): [Read-Write] Rotation in Euler angles that should be applied
    scale (Vector): [Read-Write] Scale value that should be applied
    '''
    def set_conversion_settings(self,
                                preset = unreal.AbcConversionPreset.MAYA,
                                flip_u = False,
                                flip_v = False,
                                rotation = unreal.Vector(x = 90.0,y=0.0,z=0.0),
                                scale = unreal.Vector(x = 1.0,y=-1.0,z=1.0)):

        self.conversion_settings.preset = preset
        self.conversion_settings.flip_u = flip_u
        self.conversion_settings.flip_v = flip_v
        self.conversion_settings.rotation = rotation
        self.conversion_settings.scale = scale

        return
    
    def get_conversion_settings(self):
        return self.conversion_settings

    def set_geometry_cache_settings(self,
                                    flatten_tracks = True,
                                    store_imported_vertex_numbers = False,
                                    apply_constant_topology_optimizations = False,
                                    motion_vectors = unreal.AbcGeometryCacheMotionVectorsImport.NO_MOTION_VECTORS,
                                    optimize_index_buffers = False,
                                    compressed_position_precision = 0.01,
                                    compressed_texture_coordinates_number_of_bits = 10):
        
        self.geometry_cache_settings.flatten_tracks = flatten_tracks
        self.geometry_cache_settings.store_imported_vertex_numbers = store_imported_vertex_numbers
        self.geometry_cache_settings.apply_constant_topology_optimizations = apply_constant_topology_optimizations
        self.geometry_cache_settings.motion_vectors = motion_vectors
        self.geometry_cache_settings.optimize_index_buffers = optimize_index_buffers
        self.geometry_cache_settings.compressed_position_precision = compressed_position_precision
        self.geometry_cache_settings.compressed_texture_coordinates_number_of_bits = compressed_texture_coordinates_number_of_bits

        return
    
    def get_geometry_cache_settings(self):
        return self.geometry_cache_settings

    def set_material_settings(self,
                              create_materials = False,
                              find_materials = False):
        self.material_settings.create_materials = create_materials
        self.material_settings.find_materials = find_materials

        return
    
    def get_material_settings(self):
        return self.material_settings

    def set_normal_generation_settings(self,
                                       force_one_smoothing_group_per_object = False,
                                       hard_edge_angle_threshold = 0.9,
                                       recompute_normals = False,
                                       ignore_degenerate_triangles = True,
                                       skip_computing_tangents = False):
        
        self.normal_generation_settings.force_one_smoothing_group_per_object = force_one_smoothing_group_per_object
        self.normal_generation_settings.hard_edge_angle_threshold = hard_edge_angle_threshold
        self.normal_generation_settings.recompute_normals = recompute_normals
        self.normal_generation_settings.ignore_degenerate_triangles = ignore_degenerate_triangles
        self.normal_generation_settings.skip_computing_tangents = skip_computing_tangents

        return

    def get_normal_generation_settings(self):
        return self.normal_generation_settings

    def set_sampling_settings(self,
                              sampling_type = unreal.AlembicSamplingType.PER_FRAME,
                              frame_steps = 0,
                              time_steps = 0.0,
                              frame_start = 0,
                              frame_end = 0,
                              skip_empty = False):
        
        self.sampling_settings.sampling_type = sampling_type
        self.sampling_settings.frame_steps = frame_steps
        self.sampling_settings.time_steps = time_steps
        self.sampling_settings.frame_start = frame_start
        self.sampling_settings.frame_end = frame_end
        self.sampling_settings.skip_empty = skip_empty

    def get_sampling_settings(self):
        return self.sampling_settings

    def set_static_mesh_settings(self,
                                 merge_meshes = False,
                                 propagate_matrix_transformations = False,
                                 generate_lightmap_u_vs = False):
        
        self.static_mesh_settings.merge_meshes = merge_meshes
        self.static_mesh_settings.propagate_matrix_transformations = propagate_matrix_transformations
        self.static_mesh_settings.generate_lightmap_u_vs = generate_lightmap_u_vs

    def get_static_mesh_settings(self):
        return self.static_mesh_settings

    def set_import_settings(self,
                           import_type = unreal.AlembicImportType.SKELETAL,
                           static_mesh_settings = None,
                           geometry_cache_settings = None,
                           compression_settings = None,
                           sampling_settings = None,
                           normal_generation_settings=None,
                           material_settings = None,
                           conversion_settings = None,
                           ):
        
        self.import_settings.import_type = import_type
        if import_type == unreal.AlembicImportType.SKELETAL:
            self.import_settings.compression_settings = self.get_compression_settings() if compression_settings is None else compression_settings
        elif import_type == unreal.AlembicImportType.GEOMETRY_CACHE:
            self.import_settings.geometry_cache_settings = self.get_geometry_cache_settings() if geometry_cache_settings is None else geometry_cache_settings
        elif import_type == unreal.AlembicImportType.STATIC_MESH:
            self.import_settings.static_mesh_settings = self.get_static_mesh_settings() if static_mesh_settings is None else static_mesh_settings
        else:
            print("Error: Alembic import type unknown")

        self.import_settings.sampling_settings = self.get_sampling_settings() if sampling_settings is None else sampling_settings
        self.import_settings.normal_generation_settings = self.get_normal_generation_settings() if normal_generation_settings is None else normal_generation_settings
        self.import_settings.material_settings = self.get_material_settings() if material_settings is None else material_settings
        self.import_settings.conversion_settings = self.get_conversion_settings() if conversion_settings is None else conversion_settings
        return

    def get_import_settings(self):
        return self.import_settings