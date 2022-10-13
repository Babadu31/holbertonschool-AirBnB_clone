#!/usr/bin/python3
"""unique filestorage instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()                 # à modifiier pour la suite
storage.reload()