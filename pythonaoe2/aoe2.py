import requests
from types import SimpleNamespace
import json

#TODO Account for nested api calls that might need to be made to have a complete data object

class Client:
    def __init__(self, url="https://age-of-empires-2-api.herokuapp.com/api/", version="v1"):
        self.url = url
        self.version = version
        self.fullurl = self.url + self.version

    def _request(self, api_endpoint):
        try:
            response = requests.get(self.fullurl + api_endpoint)

            if response.status_code == 404:
                print(response.content)
                raise requests.exceptions.RequestException
            else:
                return json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

        except requests.exceptions.RequestException as e:
            print(e)
            raise e


    def get_all_civilizations(self):
        """Returns all civilizations as objects"""
        api_endpoint = "/civilizations"
        data = self._request(api_endpoint)
        for civ in data.civilizations:
            civ.unique_unit = self._recurse_civ_unit(civ)
            civ.unique_tech = self._recurse_civ_tech(civ)
        return data.civilizations

    def get_civilization(self, id):
        """Returns single civilization object by ID or Name"""
        api_endpoint = "/civilization/" + id
        data = self._request(api_endpoint)
        data.unique_unit = self._recurse_civ_unit(data)
        data.unique_tech = self._recurse_civ_tech(data)
        return data

    def get_all_units(self):
        """Returns all untis as objects"""
        api_endpoint = "/units"
        data = self._request(api_endpoint)
        return data.units

    def get_unit(self, id):
        """Returns single unit object by ID or Name"""
        api_endpoint = "/unit/" + id
        return self._request(api_endpoint)

    def get_all_structures(self):
        """Returns all structures as objects"""
        api_endpoint = "/structures"
        data = self._request(api_endpoint)
        return data.structures
    
    def get_structure(self, id):
        """Returns single structure object by ID or Name"""
        api_endpoint = "/structure/" + id
        return self._request(api_endpoint)
    
    def get_all_technologies(self):
        """Returns all technologies as objects"""
        api_endpoint = "/technologies"
        data = self._request(api_endpoint)
        return data.technologies

    def get_technology(self, id):
        """Returns single technology by ID or Name"""
        api_endpoint = "/technology/" + id
        return self._request(api_endpoint)

    def _recurse_civ_unit(self, civilization):
        unique_units = []
        if len(civilization.unique_unit) > 1:
            for unit in civilization.unique_unit:
                unique_units.append(self.get_unit(unit.split("/")[-1]))
        else:
            unit = civilization.unique_unit[0].split("/")[-1]
            unique_units.append(self.get_unit(unit))

        return unique_units

    def _recurse_civ_tech(self, civilization):
        unique_techs = []
        if len(civilization.unique_tech) > 1:
            for tech in civilization.unique_tech:
                unique_techs.append(self.get_technology(tech.split("/")[-1]))
        else:
            tech = civilization.unique_tech[0].split("/")[-1]
            unique_techs.append(self.get_technology(tech))

        return unique_techs

    def _recurse_unit_building(self, unit):
        #TODO Finish this
        return True

    def _recurse_tech_building(self, tech):
         #TODO Finish this
        return True

    def _recurse_tech_applies(self, tech):
         #TODO Finish this
        return True