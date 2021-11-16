def calculate_compass_distance(origin, destination):
    import math
    origin_latitude, origin_longitude = origin
    destination_latitude, destination_longitude = destination
    # 3959 = > Miles and 6371 = > KM
    # unit in meters
    radius = 6371*1000
    dlat = math.radians(destination_latitude-origin_latitude)
    dlon = math.radians(destination_longitude-origin_longitude)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(origin_latitude)) \
        * math.cos(math.radians(destination_latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return radius * c


def calculate_initial_compass_bearing(origin, destination):
    import math
    if (type(origin) != tuple) or (type(destination) != tuple):
        raise TypeError("Only tuples are supported as arguments")
    origin_latitude, origin_longitude = origin
    destination_latitude, destination_longitude = destination
    origin_latitude = math.radians(origin_latitude)
    destination_latitude = math.radians(destination_latitude)
    diff_long = math.radians(destination_longitude - origin_longitude)
    x = math.sin(diff_long) * math.cos(destination_latitude)
    y = math.cos(origin_latitude) * math.sin(destination_latitude) - (
            math.sin(origin_latitude) * math.cos(destination_latitude) * math.cos(diff_long))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing


if __name__ == '__main__':
    # Checked on
    # http: // instantglobe.com / CRANES / GeoCoordTool.html
    pointa = (27.672944, 85.313551)
    # pointb = (27.674198, 85.313379)  # 353.074198377
    # pointb = (27.674312, 85.313701)  # 5.54634422036
    # pointb = (27.673761, 85.314173)  # 33.989047
    # pointb = (27.673723, 85.314581)  # 49.5024397615
    pointb = (27.672792, 85.315011)  # distance: 144.764626263 bearing:96.7043766096
    # pointb = (27.671747, 85.313615)  # distance: 133.249459006 bearing: 177.288978602
    distance = calculate_compass_distance(pointa, pointb)
    bearing = calculate_initial_compass_bearing(pointa, pointb)
    print(distance, bearing)
