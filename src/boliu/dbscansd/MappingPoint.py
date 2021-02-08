from TrajectoryPoint import TrajectoryPoint

import numpy as np

class MappingPoint(TrajectoryPoint):
    # extends TrajectoryPoint

    def __init__(self, lon, lat, cog, sog, mt):
        self.latitude = lat
        self.longitude = lon
        self.cog = cog
        self.sog = sog
        self.mappingtude = mt
    
    def get_mappingtude(self):
        return mappingtude
        
    def set_mappingtude(self, mt):
        self.mappingtude = mt

    def convert_point_to_mapping_point(self, p, avg_cog):
        mt = 0
        angle = (avg_cog/180) * np.pi
        
        if (avg_cog >= 0 and avg_cog < 90):
            mt = (p.get_longitude()+(1.0/np.tan(angle))*p.get_latitude())*np.sin(angle)
        elif (avg_cog >= 270 and avg_cog < 360):
            mt = (p.get_latitude()-(np.tan(np.pi*2-angle))*p.get_longitude())*np.cos(np.pi*2-angle)
        elif (avg_cog >= 90 and avg_cog < 180):
            mt = ((np.tan(np.pi-angle))*p.get_longitude()-p.get_latitude())*np.cos(np.pi-angle)
        elif (avg_cog >= 180 and avg_cog < 270):
            mt = -((1/np.tan(angle - np.pi))*p.get_latitude()+p.get_longitude())*np.sin(angle-np.pi)
        
        mp = MappingPoint(p.get_longitude(), p.get_latitude(), p.get_cog(), p.get_sog(), mt)
        return mp