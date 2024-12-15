from .api_client import CitiBikeAngelsClient

def display_top_stations(client, top_n: int = 10) -> None:
    """
    Display top stations with Bike Angels points.
    
    Args:
        client: CitiBikeAngelsClient instance
        top_n: Number of top stations to display
    """
    stations = client.analyze_bike_angels_stations()
    
    print(f"\n--- Top {top_n} Bike Angels Stations ---")
    print("{:<40} {:<10} {:<10} {:<10}".format("Station Name", "Station ID", "Pickup Pts", "Dropoff Pts"))
    print("-" * 70)
    
    for station in stations[:top_n]:
        print("{:<40} {:<10} {:<10} {:<10}".format(
            station['name'][:40], 
            station['station_id'], 
            station['pickup_points'], 
            station['dropoff_points']
        ))
