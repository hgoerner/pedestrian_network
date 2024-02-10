import sys
sys.path.append('C:\\Users\\Hendr\\OneDrive\\Desktop\\pedestrian_network')

from utils.config_loader import config_data

def list_of_street_queries():
    street_queries = []
    city = config_data["city_name"]
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
    city = config_data["city_name"]
    poi_dictionaries = config_data["pois_dictioanry"]
    poi_queries = []

    for key, values in poi_dictionaries.items():
        # Use a list comprehension to generate queries for each value of the key
        queries = [
            f"""
            area["ISO3166-1"="DE"][admin_level=2]->.country;
            area[name="{city}"]->.city;
            node[{key}={value}](area.city)(area.country);
            (._;>;);
            out body;
            """
            for value in values
        ]

        # Extend poi_queries with the generated queries
        poi_queries.extend(queries)


    return poi_queries
        
osm_street_queries = list_of_street_queries()
osm_poi_queries = list_of_poi_queries()



