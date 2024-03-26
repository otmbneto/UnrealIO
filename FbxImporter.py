import unreal
from FileImporter import *

class FbxImporter(FileImporter):

    def __init__(self,fbx_path,asset_path,asset_name):
        super(FbxImporter, self).__init__(fbx_path,asset_path,asset_name)
        self.import_settings = unreal.FbxImportUI()
        self.skeleton_mesh_import_data = unreal.FbxSkeletalMeshImportData()

        return
    
    def set_skeletal_mesh_import_data(self,
                                      import_uniform_scale = 1.0):
        self.skeleton_mesh_import_data.import_uniform_scale = import_uniform_scale

        return
    
    def get_skeletal_mesh_import_data(self):
        return self.skeleton_mesh_import_data

    def set_import_settings(self,import_mesh = False,
                           create_physics_asset = False,
                           import_rigid_mesh=False,
                           import_animations = True,
                           import_materials= False,
                           import_textures = False,
                           import_as_skeletal = False,
                           mesh_type_to_import = unreal.FBXImportType.FBXIT_ANIMATION,
                           skeleton = None,
                           automated_import_should_detect_type = False,
                           skeletal_mesh_import_data = None):
        
        self.import_settings.import_mesh = import_mesh
        self.import_settings.create_physics_asset = create_physics_asset
        self.import_settings.import_rigid_mesh = import_rigid_mesh
        self.import_settings.import_animations = import_animations
        self.import_settings.import_materials = import_materials
        self.import_settings.import_textures = import_textures
        self.import_settings.import_as_skeletal = import_as_skeletal
        self.import_settings.mesh_type_to_import = mesh_type_to_import
        self.import_settings.skeleton = skeleton
        self.import_settings.automated_import_should_detect_type = automated_import_should_detect_type 
        
        self.import_settings.skeletal_mesh_import_data = self.skeleton_mesh_import_data if skeletal_mesh_import_data is None else skeletal_mesh_import_data

        return

    #by default,only import animation sequences
    def get_import_settings(self):
        return self.import_settings