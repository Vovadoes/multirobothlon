# для первых ворот
import math


def C_to_rad(c: float):
    return c * math.pi / 180


angle_of_target = 45

target_y_m = 0
target_x_m = 0

Latitude_target, Longitude_target = target_y_m, target_x_m

# для лодки
Latitude_current, Longitude_current = -7, 5

# CONST
R_target = 2  # СИ
R_2_target = R_target / 2  # СИ
R_current = 2  # СИ

# if angle_of_target >= 90:

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


# if Latitude_target >= Latitude_current and angle_of_target >= 90:  # y >= y1
#     y1 = target_y_m - math.cos(C_to_rad(angle_of_target)) * R_target
# else:
#     y1 = math.cos(C_to_rad(angle_of_target)) * R_target + target_y_m
# if Longitude_target >= Longitude_current and angle_of_target >= 90:  # x >= x1
#     x1 = target_x_m - math.sin(C_to_rad(angle_of_target)) * R_target
# else:
#     x1 = math.sin(C_to_rad(angle_of_target)) * R_target + target_x_m


print(x1, y1)