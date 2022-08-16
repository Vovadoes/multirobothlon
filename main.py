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
R_E = 1
R_C = 1


def get_lat_lot_to_m(lat, lot):
    y_m = geopy.distance.geodesic((lat, lot), (0, lot)).m

    x_m = geopy.distance.geodesic((lat, lot), (lat, 0)).m
    return x_m, y_m


def C_to_rad(c: float):
    return c * math.pi / 180


def distance(a: tuple[float, float], b: tuple[float, float]):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def calculateAngleAndPower(*args):
    if not args:
        return None
    target, target_coordinates, current_coordinates, current_speed, current_heading = args
    if not target:
        return None
    type_target, target_bearing, angle_of_target, distance_to_target = target

    # current_heading = (current_heading + 360) % 360  # преобразуем все углы в положительные
    # angle_of_target = (angle_of_target + 360) % 360  # преобразуем все углы в положительные

    # для первых ворот
    Latitude_target, Longitude_target = target_coordinates[0]

    # для лодки
    Latitude_current, Longitude_current = current_coordinates[0]

    # D point start

    target_x_m, target_y_m = get_lat_lot_to_m(Latitude_target, Longitude_target)

    if Latitude_target >= Latitude_current:
        y1 = target_y_m - math.cos(C_to_rad(abs(angle_of_target))) * R_target
        if angle_of_target >= 0:
            x1 = target_x_m - math.sin(C_to_rad(abs(angle_of_target))) * R_target
        else:
            x1 = math.sin(C_to_rad(abs(angle_of_target))) * R_target + target_x_m
    else:
        y1 = math.cos(C_to_rad(abs(angle_of_target))) * R_target + target_y_m
        if angle_of_target >= 0:
            x1 = math.sin(C_to_rad(abs(angle_of_target))) * R_target + target_x_m
        else:
            x1 = target_x_m - math.sin(C_to_rad(abs(angle_of_target))) * R_target

    print(x1, y1)
    R_target_x_m = round(x1, 6)
    R_target_y_m = round(y1, 6)
    del x1, y1
    # D point finish
    # E point start
    R_2_target_x_m = round((target_x_m + R_target_x_m) / 2, 6)
    R_2_target_y_m = round((target_y_m + R_target_y_m) / 2, 6)
    # E point finish

    # A point start
    current_x_m, current_y_m = get_lat_lot_to_m(Latitude_current, Longitude_current)
    # A point finish

    # B point start

    if -180 >= current_heading <= -90:
        x = math.sin(C_to_rad(180 - abs(current_heading))) * R_current + current_x_m
        y = current_y_m - math.cos(C_to_rad(180 - abs(current_heading))) * R_current
    elif current_heading <= 0:
        x = current_x_m - math.sin(C_to_rad(abs(current_heading))) * R_current
        y = math.cos(C_to_rad(abs(current_heading))) * R_current + current_y_m
    elif current_heading <= 90:
        x = math.sin(C_to_rad(current_heading)) * R_current + current_x_m
        y = math.cos(C_to_rad(current_heading)) * R_current + current_y_m
    elif current_heading <= 180:
        x = math.sin(C_to_rad(180 - current_heading)) * R_current + current_x_m
        y = current_y_m - math.cos(C_to_rad(180 - current_heading)) * R_current
    else:
        raise ValueError("-180 <= current_heading >= 180")

    print(x, y)

    R_current_x_m = x
    R_current_y_m = y
    del x, y

    # B point finish

    # C point start

    C_point_x_m = round((R_target_x_m + R_current_x_m) / 2, 6)
    C_point_y_m = round((R_target_y_m + R_current_y_m) / 2, 6)

    # C point finish

    # вычисление угла между current_heading и курсом который нам нужен

    D_BC = distance((R_current_x_m, R_current_y_m), (C_point_x_m, C_point_y_m))
    print(f"{D_BC=}")
    D_AC = distance((current_x_m, current_y_m), (C_point_x_m, C_point_y_m))
    print(f"{D_AC=}")

    delta = math.acos((D_AC ** 2 + R_current ** 2 - D_BC ** 2) / (
                2 * D_AC * R_current))  # перевести радианы в градусы

    print(delta)
    # if delta == 0:
    #     return 0, 0
    # elif delta > 0:
    #     return 1, 35
    # else:
    #     return 1, -35
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
