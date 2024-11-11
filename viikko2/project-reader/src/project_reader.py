from urllib import request
from project import Project
import tomllib

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        project = tomllib.loads(content)["tool"]["poetry"]

        #print(project)
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", project['dependencies'], project['group']['dev']['dependencies'], project["authors"], project["license"])
