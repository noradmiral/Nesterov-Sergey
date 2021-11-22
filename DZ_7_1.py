import os

ROOT = os.path.dirname(__file__)
project_name = 'домашка'
paths = [os.path.join(project_name, 'settings'), os.path.join(project_name, 'minnapp'),
         os.path.join(project_name, 'adminapp'), os.path.join(project_name, 'authapp')]
for _path in paths:
    os.makedirs(os.path.join(ROOT, _path), exist_ok=True)