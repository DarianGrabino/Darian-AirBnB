"""the __init__.py of models"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
