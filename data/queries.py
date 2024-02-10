from data.config_loader import config_data

def create_list_of_street_queries():
    queries = []
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
        queries.append(query)
    return queries

osm_street_queries = create_list_of_street_queries()
