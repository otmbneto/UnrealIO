import unreal
from FileImporter import *

class AlembicImporter(FileImporter):

    def __init__(self,alembic_path,asset_path,asset_name):
        super(AlembicImporter, self).__init__(alembic_path,asset_path,asset_name)

    '''
    Create Conversion settings. By default,it uses Maya's friendly settings.
    flip_u (bool): [Read-Write] Flag whether or not to flip the U channel in the Texture Coordinates
    flip_v (bool): [Read-Write] Flag whether or not to flip the V channel in the Texture Coordinates
    rotation (Vector): [Read-Write] Rotation in Euler angles that should be applied
    scale (Vector): [Read-Write] Scale value that should be applied
    '''
    def get_conversion_settings(self,flip_u = False,
                                flip_v = True,
                                rotation = unreal.Vector(x = 90.0,y=0.0,z=0.0),
                                scale = unreal.Vector(x = 1.0,y=-1.0,z=1.0)):

        settings = unreal.AbcConversionSettings()
        settings.flip_u = flip_u
        settings.flip_v = flip_v
        settings.rotation = rotation
        settings.scale = scale

        return settings

    def get_import_options(self,import_type = unreal.AlembicImportType.SKELETAL,
                           conversion_settings = None,
                           frame_start = 0,
                           frame_end = 50):

        options = unreal.AbcImportSettings()
        options.import_type = import_type
        options.conversion_settings = self.get_conversion_settings() if conversion_settings is None else conversion_settings 
        #options.sampling_settings.frame_start = frame_start
        #options.sampling_settings.frame_end = frame_end

        return options