#Made by Ottoni Bastos 03/18/24
#Base object for importing asset files to unreal.
import unreal

class FileImporter():

    def __init__(self,filename,destination_path,destination_name):

        self.filename = filename
        self.destination_path = destination_path
        self.destination_name = destination_name
        self.import_task = unreal.AssetImportTask()

    def get_import_settings(self):
        #override this method.
        return

    def set_import_task(self,filename = None,
                        destination_path = None,
                        destination_name = None,
                        save = True,
                        automated = True,
                        replace_existing = True,
                        replace_existing_settings = False,
                        options = None):
        
        # Set base properties on the task.
        self.import_task.filename = self.filename if filename is None else filename
        self.import_task.destination_path = self.destination_path if destination_path is None else destination_path
        self.import_task.destination_name = self.destination_name if destination_name is None else destination_name
        self.import_task.save = save
        self.import_task.automated = automated # Suppress UI.
        self.import_task.replace_existing = replace_existing
        self.import_task.replace_existing_settings = replace_existing_settings
        self.import_task.options = self.get_import_settings() if options is None else options        

        return

    def get_import_task(self):
        return self.import_task
    
    def import_file(self,task = None):

        # Create an import task.
        import_task = self.get_import_task() if task is None else task
        print(import_task)
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        asset_tools.import_asset_tasks([import_task])
        imported_asset = import_task.get_editor_property('imported_object_paths')
        
        return imported_asset