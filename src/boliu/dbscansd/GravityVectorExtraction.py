from Cluster import Cluster
from MappingPoint import MappingPoint
import copy
import numpy as np

class GravityVectorExtraction():

    def extract_gravity_vector(cluster):
        avg_cog = cluster.calculate_average_direction()
        mp_list = []
        for i in range(len(cluster)):
            mp = convert_point_to_mapping_point(cluster[i], avg_cog)
            mp_list.append(mp)

            # TODO: insertion_sort()

        insertion_sort(mp_list)

        ppl = []
        trajectory_points = []
        cnt = 0
        k = 0
        median_distance = 0
        sum_x = 0
        sum_y = 0
        sum_sog = 0
        sum_cog = 0

        while (cnt <= len(mp_list)):
            if ((cnt <= len(mp_list)) and (mp_list[cnt].get_mappingtude() - mp_list[k].get_mappingtude() < 0.01)):
                sum_x = sum_x + mp_list[cnt].get_longitude()
                sum_y = sum_y + mp_list[cnt].get_latitude()
                sum_SOG = sum_SOG + mp_list[cnt].get_sog()
                sum_COG = sum_COG + mp_list[cnt].get_cog()
                trajectory_points.append(mp_list[cnt])
                cnt += 1
            else:
                x = sum_x / (cnt - k)
                y = sum_y / (cnt - k)
                sog = sum_sog / (cnt - k)
                cog = sum_cog / (cnt - k)
                distances = []
                for i in range(len(trajectory_points)):
                    lon = trajectory_points[i].get_longitude()
                    lat = trajectory_points[i].get_latitude()
                    dist = gps_distance(lat, lon, y, x) # TODO: gps_distance()
                    distances.append(dist)
                median_distance = quartile(distances, 50) # TODO: why 50?
                gv = GravityVector(x, y, cog, sog, median_distance)
                ppl.append(gv)
                sum_x = 0
                sum_y = 0
                sum_cog = 0
                sum_sog = 0
                k = cnt
                trajectory_points.clear()
                if (count == len(mp_list)):
                    break

        return ppl

    def insertion_sort(mpl):
        for i in range(len(mpl)):
            k = i
            mp = mpl[i]
            insert_already = False
            while (mpl[i].get_mappingtude() < mpl[i].get_mappingtude()):
                if (k == 1):
                    del mpl[i]
                    mpl.insert(0, mp)
                    insert_already = True
                    break
                k -= k
            if (not insert_already):
                del mpl[i]
                mpl.insert(k, mp)
    
    def quartile(values, lower_percent):
        if ((values == None) or (len(values) == 0)):
            raise ValueError("The data array either is null or does not contain any data.")

        v = [copy.deepcopy(x) for x in values]
        v = sorted(v)
        n = 0 if len(v) == 1 else round(len(v) * lower_percent / 100)
        #print(f"{len(v)},{n}")
        return v[n]


    def gps_distance(lat_1, lon_1, lat_2, lon_2):
        earth_radius = 3958.75
        d_lat = np.radians(lat_2 - lat_1)
        d_lon = np.radians(lon_2 - lon_1)
        a = np.sin(d_lat/2) * np.sin(d_lat/2) + np.cos(np.radians(lat_1)) * np.cos(np.radians(lat_2)) * np.sin(d_lon/2) * np.sin(d_lon/2)
        c = 2 * np.atan2(np.sqrt(a), np.sqrt(1 - a))
        dist = earth_radius * c

        meter_conversion = 1609

        return dist * meter_conversion


        
    
        