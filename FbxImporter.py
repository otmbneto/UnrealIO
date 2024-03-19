import unreal
from FileImporter import *

class FbxImporter(FileImporter):

    def __init__(self,fbx_path,asset_path,asset_name):
        super(FbxImporter, self).__init__(fbx_path,asset_path,asset_name)

        return
    
    #by default,only import animation sequences
    def get_import_options(self,import_mesh = False,
                           create_physics_asset = False,
                           import_rigid_mesh=False,
                           import_animations = True,
                           import_materials= False,
                           import_textures = False,
                           import_as_skeletal = False,
                           mesh_type_to_import = unreal.FBXImportType.FBXIT_ANIMATION,
                           skeleton = None,
                           automated_import_should_detect_type = False):

        import_options = unreal.FbxImportUI()
        import_options.import_mesh = import_mesh
        import_options.create_physics_asset = create_physics_asset
        import_options.import_rigid_mesh = import_rigid_mesh
        import_options.import_animations = import_animations
        import_options.import_materials = import_materials
        import_options.import_textures = import_textures
        import_options.import_as_skeletal = import_as_skeletal
        import_options.mesh_type_to_import = mesh_type_to_import
        import_options.skeleton = skeleton
        import_options.automated_import_should_detect_type = automated_import_should_detect_type 

        return import_options