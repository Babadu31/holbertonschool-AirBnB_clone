#!/usr/bin/python3
"""unique filestorage instance"""
from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()