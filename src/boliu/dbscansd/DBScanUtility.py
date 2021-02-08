from TrajectoryPoint import TrajectoryPoint
import numpy as np

class DBScanUtility():

    # TODO: p1, p2 are TrajectoryPoint
    
    def calculate_dist_between_two_points(self, p1, p2):
        
        dx = p1.get_longitude() - p2.get_longitude()
        dy = p1.get_latitude() - p2.get_latitude()
        dist = np.sqrt((dx*dx)+(dy*dy))
        return dist

    def is_density_reachable(self, p1, p2, eps, min_pts, max_spd, max_dir, is_stop_point): 
        result = False
        if (self.calculate_dist_between_two_points(p1, p2) <= eps):
            if (is_stop_point):
                return True
            if (np.abs(p1.get_cog()-p2.get_cog())<max_dir):
                result = True
        return result

        

