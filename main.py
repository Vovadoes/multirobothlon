import math

import geopy.distance


def imageProcessing(img, input_shape):
    """Preprocess an image with Aruco markers.
    # Args:
         img: int8 numpy array of shape (img_h, img_w, 3)
         input_shape: a tuple of (H, W)
    # Returns
         type_target: int value 0 - gates, 1 - finish
         target_bearing: float value in degree
         angle_of_target: float value in degree
         distance_to_target: float value in meters
         OR
         None: if there is no markers on image
    """


# CONST
R_target = 2  # СИ
R_2_target = R_target / 2  # СИ
R_current = 2  # СИ


def get_lat_lot_to_m(lat, lot):
    y_m = geopy.distance.geodesic((lat, lot), (0, lot)).m

    x_m = geopy.distance.geodesic((lat, lot), (lat, 0)).m
    return x_m, y_m


def C_to_rad(c: float):
    return c * math.pi / 180


def calculateAngleAndPower(*args):
    if not args:
        return None
    target, target_coordinates, current_coordinates, current_speed, current_heading = args
    if not target:
        return None
    type_target, target_bearing, angle_of_target, distance_to_target = target

    current_heading = (current_heading + 360) % 360  # преобразуем все углы в положительные
    angle_of_target = (angle_of_target + 360) % 360  # преобразуем все углы в положительные

    # для первых ворот
    Latitude_target, Longitude_target = target_coordinates[0]

    # для лодки
    Latitude_current, Longitude_current = current_coordinates[0]

    target_x_m, target_y_m = get_lat_lot_to_m(Latitude_target, Longitude_target)

    if Latitude_target >= Latitude_current:  # y >= y1
        y1 = target_y_m - math.cos(C_to_rad(angle_of_target)) * R_target
    else:
        y1 = math.cos(C_to_rad(angle_of_target)) * R_target + target_y_m
    if Longitude_target >= Longitude_current:  # x >= x1
        x1 = target_x_m - math.sin(C_to_rad(angle_of_target)) * R_target
    else:
        x1 = math.sin(C_to_rad(angle_of_target)) * R_target + target_x_m

    print(x1, y1)
    R_target_x_m = x1
    R_target_y_m = y1
    R_2_target_x_m = (target_x_m + R_target_x_m) / 2
    R_2_target_y_m = (target_y_m + R_target_y_m) / 2

    # 2 этап
    current_x_m, current_y_m = get_lat_lot_to_m(Latitude_current, Longitude_current)

    """Calculation of steering direction and engine power.
    # Args
       target: a tuple of (type_target, target_bearing, angle_of_target, distance_to_target) OR None
       (если будет None, то ориентируемя по координатам!)
       target_coordinates: a tuple of (Latitude, Longitude)
       current_coordinates: a tuple of (Latitude, Longitude)
       current_speed: float value in m/s
       current_heading: float value in degree
    # Returns
       angel: float value in degree between -35 and 35
       power: float value between -1 and 1
    """


calculateAngleAndPower()
