"""
IP Geolocation Distance Calculator
Purpose: E-commerce fraud detection by measuring geographic distance between IP locations
Use Case: Flag suspicious transactions where purchase location differs significantly from base location
"""

# Note: In order for this to work you need to generate an access key from ipstack.com
# Get your free API key at: https://ipstack.com/

import requests
import pandas as pd
from geopy.distance import geodesic
import os

# Configuration
API_KEY = os.environ.get('IPSTACK_API_KEY', 'YOUR_API_KEY_HERE')
DATA_URL = "https://www.dropbox.com/s/56njnjab3m159wb/D4-ipstack.csv?dl=0"


def get_ip_location(ip_address, api_key):
    """
    Retrieve latitude and longitude for a given IP address using IPStack API

    Args:
        ip_address (str): IP address to geolocate
        api_key (str): IPStack API key

    Returns:
        tuple: (latitude, longitude) or (None, None) if error
    """
    try:
        url = f'http://api.ipstack.com/{ip_address}?access_key={api_key}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'latitude' in data and 'longitude' in data:
            return data['latitude'], data['longitude']
        else:
            print(f"Warning: No location data for IP {ip_address}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location for IP {ip_address}: {e}")
        return None, None


def calculate_distance_miles(coord1, coord2):
    """
    Calculate geodesic distance between two coordinates

    Args:
        coord1 (tuple): (latitude, longitude) of first location
        coord2 (tuple): (latitude, longitude) of second location

    Returns:
        float: Distance in miles, or None if coordinates are invalid
    """
    try:
        if None in coord1 or None in coord2:
            return None
        return geodesic(coord1, coord2).miles
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return None


def main():
    """Main function to process IP addresses and calculate distances"""

    # Validate API key
    if API_KEY == 'YOUR_API_KEY_HERE':
        print("ERROR: Please set your IPStack API key!")
        print("Get a free key at: https://ipstack.com/")
        print("Set it as environment variable: export IPSTACK_API_KEY='your_key'")
        return

    try:
        # Load dataset
        print("Loading dataset...")
        data_set = pd.read_csv(DATA_URL)
        print(f"Loaded {len(data_set)} transactions\n")

        # Initialize new columns
        data_set['loan_lat'] = None
        data_set['loan_lng'] = None
        data_set['payment_lat'] = None
        data_set['payment_lng'] = None
        data_set['distance_miles'] = None

        # Process each transaction
        print("Fetching geolocation data...")
        for idx, row in data_set.iterrows():
            print(f"Processing transaction {idx + 1}/{len(data_set)}...", end='\r')

            # Get loan IP location
            loan_ip = row['loan_ipaddress']
            loan_lat, loan_lng = get_ip_location(loan_ip, API_KEY)
            data_set.at[idx, 'loan_lat'] = loan_lat
            data_set.at[idx, 'loan_lng'] = loan_lng

            # Get payment IP location
            payment_ip = row['payment_ipaddress']
            payment_lat, payment_lng = get_ip_location(payment_ip, API_KEY)
            data_set.at[idx, 'payment_lat'] = payment_lat
            data_set.at[idx, 'payment_lng'] = payment_lng

            # Calculate distance
            loan_coords = (loan_lat, loan_lng)
            payment_coords = (payment_lat, payment_lng)
            distance = calculate_distance_miles(loan_coords, payment_coords)
            data_set.at[idx, 'distance_miles'] = distance

        print("\nProcessing complete!\n")

        # Display results
        print("=" * 80)
        print("FRAUD DETECTION ANALYSIS - IP DISTANCE RESULTS")
        print("=" * 80)
        print(data_set.to_string())
        print("\n" + "=" * 80)

        # Summary statistics
        valid_distances = data_set['distance_miles'].dropna()
        if len(valid_distances) > 0:
            print("\nSUMMARY STATISTICS:")
            print(f"Average distance: {valid_distances.mean():.2f} miles")
            print(f"Maximum distance: {valid_distances.max():.2f} miles")
            print(f"Minimum distance: {valid_distances.min():.2f} miles")

            # Flag suspicious transactions (>500 miles as example threshold)
            suspicious_threshold = 500
            suspicious = data_set[data_set['distance_miles'] > suspicious_threshold]
            print(f"\nSuspicious transactions (>{suspicious_threshold} miles): {len(suspicious)}")
            if len(suspicious) > 0:
                print("\nFlagged Transactions:")
                print(suspicious[['loan_ipaddress', 'payment_ipaddress', 'distance_miles']])

        # Save results
        output_file = "fraud_detection_results.csv"
        data_set.to_csv(output_file, index=False)
        print(f"\nResults saved to: {output_file}")

    except Exception as e:
        print(f"Error processing data: {e}")
        raise


if __name__ == "__main__":
    main()
