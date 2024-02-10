#!/usr/bin/python3
"""initilization of the base"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
