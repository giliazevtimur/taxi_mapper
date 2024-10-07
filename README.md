# Taxi Mapper

## Description
Taxi Mapper is a Python library designed to help calculate taxi routes at airports using OpenStreetMap data. It supports complex route calculations for arrival and departure routes, providing detailed coordinates along the path.

### Example Usage

```
from taxi_mapper.route_mapper import TaxiRouteMapper

# Example: Arrival route for EHAM
mapper = TaxiRouteMapper("EHAM")
mapper.load_airport_data()
route = mapper.calculate_route((4.768274, 52.3086), (4.76343, 52.3079), ["W6", "A", "A9C"])
print(route)
```

## Installation
Install the library using:

```
pip install -e .
```

