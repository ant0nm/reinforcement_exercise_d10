# define the function for retrieving specific venues
def find_venues(venues, accessible, city, capacity):
    found_venues = []
    for venue in venues:
        if venue['wheelchair_accessible'] and venue['city'] == city and venue['capacity'] >= capacity:
            found_venues.append(venue)
    return found_venues

def display_venues(venues):
    for venue in venues:
        print('*', venue)

# all the venues
venues = [
{ 'address': "123 Main Street", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 100 },
{ 'address': "567 Centre Street", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 400 },
{ 'address': "9B Ontario Street", 'city': "Montreal", 'wheelchair_accessible': True, 'capacity': 1000 },
{ 'address': "56 Road Avenue", 'city': "Ottawa", 'wheelchair_accessible': True, 'capacity': 650 },
{ 'address': "938 Avenue Way East", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 90 },
{ 'address': "34 Main Street West", 'city': "London", 'wheelchair_accessible': False, 'capacity': 300 },
{ 'address': "44 Quebec Road", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 200 },
{ 'address': "10 Spruce Avenue Ouest", 'city': "Montreal", 'wheelchair_accessible': False, 'capacity': 525 }
]

# find venues that are wheelchair accessible, in Toronto, and can fit at least 150 people
v = find_venues(venues, True, "Toronto", 150)
print("Here are the venues that were found:")
display_venues(v)
