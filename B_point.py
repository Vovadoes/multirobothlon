import math


def C_to_rad(c: float):
    return c * math.pi / 180


current_heading = -180
R_current = 2  # СИ

current_x_m, current_y_m = 0, 0

# if -180 >= current_heading <= -90:
#     x = math.sin(C_to_rad(current_heading)) * R_current + current_x_m
#     y = math.cos(C_to_rad(current_heading)) * R_current + current_y_m
# elif current_heading <= 0:
#     x = current_x_m - math.sin(C_to_rad(current_heading)) * R_current
#     y = math.cos(C_to_rad(current_heading)) * R_current + current_y_m
# elif current_heading <= 90:
#     x = current_x_m - math.sin(C_to_rad(current_heading)) * R_current
#     y = current_y_m - math.cos(C_to_rad(current_heading)) * R_current
# elif current_heading <= 180:
#     x = math.sin(C_to_rad(current_heading)) * R_current + current_x_m
#     y = current_y_m - math.cos(C_to_rad(current_heading)) * R_current
# else:
#     raise ValueError("-180 <= current_heading >= 180")


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