import sys
sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')

from utils.config_loader import config_data
from data.load_data import poi_key_value_dic
from urllib.parse import quote
from typing import List, Dict

city = config_data["city_name"]

def list_of_street_queries():
  
    street_queries = []
    # Loop through combinations of cities and street types
    for street_type in config_data["street_types_list"]:
        query = f"""
        area["ISO3166-1"="DE"][admin_level=2]->.country;
        area[name="{city}"]->.city;
        way[highway={street_type}](area.city)(area.country);
        (._;>;);
        out body;
        """
        street_queries.append(query)
    return street_queries

def list_of_poi_queries():
    
    poi_queries = []

    for keys in poi_key_value_dic.keys():
        osm_key = quote(poi_key_value_dic[keys]["Key"])
        osm_value = quote(poi_key_value_dic[keys]["value"])
        
        # Use a list comprehension to generate queries for each value of the key
        queriy = f"""
            area["ISO3166-1"="DE"][admin_level=2]->.country;
            area[name="{city}"]->.city;
            node[{osm_key}={osm_value}](area.city)(area.country);
            (._;>;);
            out body;
            """
        query_info = {"query":queriy,'key': osm_key, 'value': osm_value}    

        # Extend poi_queries with the generated queries
        poi_queries.append(query_info)


    return poi_queries
        
osm_street_queries = list_of_street_queries()
osm_poi_queries = list_of_poi_queries()


