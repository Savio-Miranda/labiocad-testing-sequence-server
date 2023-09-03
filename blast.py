import os
import re
from flask import current_app
from atexit import register

"""
        :param index: the standard sequences server URL
        :param image: docker image to pull
        :param database: your local directory containing ntbs-databases
"""
def init_app(app):
    with app.app_context():
        port = current_app.config['PORT']
        image = current_app.config['IMAGE']
        database = current_app.config['DATABASE']
        Container(port, image, database)


class Container():
    def __init__(self, port:int, image:str, database:str, id:str | None = None):
        self.id = id
        self.port = port
        self.image = image
        self.database = database
        self.init_docker()
        register(self.shutdown_docker)

    
    def init_docker(self):
        if self.container_exists():
            return

        os.system(f'docker run -d -p {self.port}:{self.port} -v {self.database}:/db {self.image}')
        return


    def get_container_id(self):
        if not self.container_exists():
            print("Container doesn't exist...")
            return

        docker_pattern = r'\w \s \w | \s+'
        lines = os.popen('docker container ls').read().strip().split('\n')
        titles = re.split(docker_pattern, lines[0]) #len() == 7

        for container in range(1, len(lines)):
            if self.image in lines[container]:
                full_container = re.split(docker_pattern, lines[container])
                bioinfo_container = {titles[i]: full_container[i] for i in range(len(titles))}
                self.id = bioinfo_container['CONTAINER ID']
                return



    def container_exists(self):
        lines = os.popen('docker container ls').read()
        return True if self.image in lines else False


    def shutdown_docker(self):
        if not self.container_exists():
            return
        self.get_container_id()
        os.system('sudo aa-remove-unknown')
        os.system(f'make remove id={self.id}')
        return
