import math


def C_to_rad(c: float):
    return c * math.pi / 180

def Rad_to_c(c: float):
    return c * 180 / math.pi

def get_angle_of_target(coords_mark_1: tuple[float, float], coords_mark_2: tuple[float, float]):
	a = coords_mark_2[1] - coords_mark_1[1]
	b = coords_mark_2[0] - coords_mark_1[0]
	c = Rad_to_c(math.atan2(a, b))
	if 90 < c <= 180:
		return -180 + c
	else:
		return c # возвращает градусы

if __name__ == "__main__":
	lst = [{}, {}]

	if len(lst) >= 2:
		dct1 = lst[0]
		dct2 = lst[1]
		get_angle_of_target((dct1["tvecs"][0], dct1["tvecs"][2]), (dct2["tvecs"][0], dct2["tvecs"][2]))

