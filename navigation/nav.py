from regulator import CourseRegulator
import math


# import geopy.distance


# def get_lat_lot_to_m(lat, lot):
#     y_m = geopy.distance.geodesic((lat, lot), (0, lot)).m
#
#     x_m = geopy.distance.geodesic((lat, lot), (lat, 0)).m
#     return x_m, y_m


def C_to_rad(c: float):
    return c * math.pi / 180


def Rad_to_c(c: float):
    return c * 180 / math.pi


def distance(a: tuple[float, float], b: tuple[float, float]):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def find_current_degree(x1, y1, x2, y2):  # широта, долгота
    return math.degrees(math.atan2((y2 - y1) * math.cos(math.radians(x1)), (x2 - x1)))


# -----
old_target = None


def calculateAngleAndPower(
        target: tuple[int, float, float, float],
        target_coordinates: tuple[float, float],
        current_coordinates: tuple[float, float],
        current_speed: float, current_heading: float,
        course_regulator: CourseRegulator
):
    # # для первых ворот
    # Latitude_target, Longitude_target = target_coordinates
    #
    # # для лодки
    # Latitude_current, Longitude_current = current_coordinates

    # target_x_m, target_y_m = get_lat_lot_to_m(Latitude_target, Longitude_target)
    #
    # target_x_m, target_y_m = get_lat_lot_to_m(Latitude_target, Longitude_target)

    global old_target

    power = 0.5

    distance_target_to_current = distance(current_coordinates, target_coordinates)

    R_target = distance_target_to_current / 2
    print(f"{distance_target_to_current=}")

    if not target and not old_target:
        print("target is None")
        target_course = find_current_degree(*target_coordinates,
                                            *current_coordinates)
        print(f"{target_course=}")
        # target_course = 180  # угол куда хотим двигаться от -180 до 180
        angle = course_regulator.calculateAngle(current_heading, target_course)
    else:
        if old_target:
            target_bearing = old_target["bearing_heading"] - current_heading
            angle_of_target = old_target["angle_of_target"]
            type_target = old_target["type_target"]
        else:
            type_target, target_bearing, angle_of_target, distance_to_target = target

            # angle_of_target_sever = angle_of_target + current_heading

        x = math.sin(angle_of_target + target_bearing) * distance_target_to_current
        y = math.cos(angle_of_target + target_bearing) * distance_target_to_current

        angle = math.atan(x / (y - R_target)) - angle_of_target - target_bearing

        angle = course_regulator.calculateAngle(0, angle)
        old_target = {"bearing_heading": target_bearing + current_heading,
                      "angle_of_target": angle_of_target,
                      "type_target": type_target}
        if type_target:
            a1 = -1  # м/с ускорение
            dis = (-(current_speed ** 2)) / (2 * a1)
            if distance_target_to_current < dis:
                power = -1
            else:
                power = 1

    # target_course = find_current_degree(x1, y1, *current_coordinates) - current_heading

    """Расчет угла руля и мощности мотора
    
    Args:
        target (tuple[int, float, float, float] | None): локальное положение цели - (type_target, target_bearing, angle_of_target, distance_to_target)
        target_coordinates (tuple[float, float]): (Latitude, Longitude) - координаты цели
        current_coordinates (tuple[float, float]): (Latitude, Longitude) - текущие координаты беспилотника
        current_speed (float): скорость беспилотника в м/c
        current_heading (float): курс беспилотника относительно севера от -180 до 180 в градусах
        course_regulator (CourseRegulator): регулятор курса
    
    Returns:
        angle: угол мотора в градусах от -35 до 35
        power: мощность двигателя от -1 до 1
    """

    return angle, power

# # Тест
# regulator = CourseRegulator()
# print(calculateAngleAndPower((0, 0), (0, 0), 0, 0, regulator))
# Latitude_target = 0
# Latitude_current = 0
#
# distance_target_to_current = 9
#
# c = 180 - Rad_to_c(
#     math.asin((Latitude_target - Latitude_current) / distance_target_to_current))
