import requests
from typing import List, Dict, Optional

class CitiBikeAngelsClient:
    def __init__(self):
        self.base_url = "https://layer.bicyclesharing.net/map/v1/nyc/stations"
        self.angels_url = "https://layer.bicyclesharing.net/map/v1/nyc/map"

    def get_station_data(self) -> Optional[List[Dict]]:
        """
        Retrieve all station data from the Citi Bike API.
        """
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()['features']
        except requests.RequestException as e:
            print(f"Error retrieving station data: {e}")
            return None

    def get_bike_angels_points(self) -> Optional[Dict]:
        """
        Retrieve Bike Angels points data.
        """
        try:
            response = requests.get(self.angels_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error retrieving Bike Angels data: {e}")
            return None

    def analyze_bike_angels_stations(self) -> List[Dict]:
        """
        Analyze stations with Bike Angels points.
        """
        stations = self.get_station_data()
        angels_data = self.get_bike_angels_points()
        
        if not stations or not angels_data:
            return []
        
        angels_stations = []
        
        for station in stations:
            station_id = station['properties']['station_id']
            
            angels_station = next(
                (s for s in angels_data['stations'] if s['id'] == station_id), 
                None
            )
            
            if angels_station:
                station_info = {
                    'name': station['properties']['name'],
                    'station_id': station_id,
                    'latitude': station['geometry']['coordinates'][1],
                    'longitude': station['geometry']['coordinates'][0],
                    'pickup_points': angels_station.get('pickupPoints', 0),
                    'dropoff_points': angels_station.get('dropoffPoints', 0),
                    'total_points': angels_station.get('pickupPoints', 0) + angels_station.get('dropoffPoints', 0)
                }
                angels_stations.append(station_info)
        
        return sorted(angels_stations, key=lambda x: x['total_points'], reverse=True)
