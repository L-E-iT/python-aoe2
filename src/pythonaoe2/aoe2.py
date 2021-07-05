import requests
from types import SimpleNamespace
import json

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
        for unit in data.units:
            unit.created_in = self._recurse_unit_building(unit)
        return data.units

    def get_unit(self, id):
        """Returns single unit object by ID or Name"""
        api_endpoint = "/unit/" + id
        data = self._request(api_endpoint)
        data.created_in = self._recurse_unit_building(data)
        return data

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
        for tech in data.technologies:
            tech.develops_in = self._recurse_tech_building(tech)
            tech.applies_to = self._recurse_tech_applies(tech)
        return data.technologies

    def get_technology(self, id):
        """Returns single technology by ID or Name"""
        api_endpoint = "/technology/" + id
        data = self._request(api_endpoint)
        data.develops_in = self._recurse_tech_building(data)
        data.applies_to = self._recurse_tech_applies(data)
        return data

    def _recurse_civ_unit(self, civilization):
        unique_units = []
        if len(civilization.unique_unit) > 1:
            for unit in civilization.unique_unit:
                unique_units.append(unit.split("/")[-1].lower().replace(" ","_"))
        elif len(civilization.unique_unit) == 0:
            return unique_units
        else:
            unique_units.append(civilization.unique_unit[0].split("/")[-1].lower().replace(" ","_"))

        return unique_units

    def _recurse_civ_tech(self, civilization):
        unique_techs = []
        if len(civilization.unique_tech) > 1:
            for tech in civilization.unique_tech:
                unique_techs.append(tech.split("/")[-1].lower().replace(" ","_"))
        elif len(civilization.unique_tech) == 0:
            return unique_techs
        else:
            unique_techs.append(civilization.unique_tech[0].split("/")[-1].lower().replace(" ","_"))

        return unique_techs

    def _recurse_unit_building(self, unit):
        if unit.created_in == "":
            return ""
        return unit.created_in.split("/")[-1].lower().replace(" ","_")

    def _recurse_tech_building(self, tech):
        if tech.develops_in == "":
            return ""
        return tech.develops_in.split("/")[-1].lower().replace(" ","_")

    def _recurse_tech_applies(self, tech):
        applies_to = []
        if len(tech.applies_to) > 1:
            for applied in tech.applies_to:
                applies_to.append(applied.split("/")[-1].lower().replace(" ","_"))
        elif len(tech.applies_to) == 0:
            return applies_to
        else:
            applies_to.append(tech.applies_to[0].split("/")[-1].lower().replace(" ","_"))
        return applies_to