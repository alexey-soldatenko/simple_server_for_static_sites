import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(base_dir, 'templates/')
STATIC = os.path.join(base_dir, 'static/')
