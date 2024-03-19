#Made by Ottoni Bastos 03/18/24
#Base object for importing asset files to unreal.
import unreal

class FileImporter():

    def __init__(self,filename,destination_path,destination_name):

        self.filename = filename
        self.destination_path = destination_path
        self.destination_name = destination_name

    def get_import_options(self):
        #override this method.
        return

    def get_import_task(self,filename = None,
                        destination_path = None,
                        destination_name = None,
                        save = True,
                        automated = True,
                        replace_existing = True,
                        replace_existing_settings = False,
                        options = None):
        
        # Create an import task.
        import_task = unreal.AssetImportTask()
        # Set base properties on the task.
        import_task.filename = self.filename if filename is None else filename
        import_task.destination_path = self.destination_path if destination_path is None else destination_path
        import_task.destination_name = self.destination_name if destination_name is None else destination_name
        import_task.save = save
        import_task.automated = automated # Suppress UI.
        import_task.replace_existing = replace_existing
        import_task.replace_existing_settings = replace_existing_settings
        import_task.options = self.get_import_options() if options is None else options
        
        return import_task
    
    def import_file(self,task = None):

        # Create an import task.
        import_task = self.get_import_task() if task is None else task
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([import_task])
        imported_asset = import_task.get_editor_property('imported_object_paths')
        
        return imported_asset