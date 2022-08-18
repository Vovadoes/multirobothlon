if Latitude_target >= Latitude_current:
            y1 = target_y_m - math.cos(C_to_rad(abs(angle_of_sever))) * R_target
            if angle_of_sever >= 0:
                x1 = target_x_m - math.sin(C_to_rad(abs(angle_of_sever))) * R_target
            else:
                x1 = math.sin(C_to_rad(abs(angle_of_sever))) * R_target + target_x_m
        else:
            y1 = math.cos(C_to_rad(abs(angle_of_sever))) * R_target + target_y_m
            if angle_of_sever >= 0:
                x1 = math.sin(C_to_rad(abs(angle_of_sever))) * R_target + target_x_m
            else:
                x1 = target_x_m - math.sin(C_to_rad(abs(angle_of_sever))) * R_target