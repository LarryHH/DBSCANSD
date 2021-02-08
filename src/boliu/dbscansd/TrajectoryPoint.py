class TrajectoryPoint():
    
    def __init__(self):
        self.mmsi = None
        self.timestamp = None
        self.longitude = None
        self.latitude = None
        self.sog = None
        self.cog = None
        self.is_visited = False
        self.is_core_point = None

    def get_mmsi(self):
        return self.mmsi
    
    def set_mmsi(self, mmsi):
        self.mmsi = mmsi
    
    def get_longitude(self):
        return self.longitude

    def set_longitude(self, lon):
        self.longitude = lon

    def get_latitude(self):
        return self.latitude
    
    def set_latitude(self, lat):
        self.latitude = lat

    def get_sog(self):
        return self.sog
    
    def set_sog(self, sog):
        self.sog = sog

    def get_cog(self):
        return self.cog
    
    def set_cog(self, cog):
        self.cog = cog

    def get_timestamp(self):
        return self.timestamp
    
    def set_timestamp(self, ts):
        self.timestamp = ts

    def get_is_visited(self):
        return self.is_visited
    
    def set_visited(self, iv):
        self.is_visited = iv

    def get_is_core_point(self):
        return self.is_core_point
    
    def set_core_point(self, cp):
        self.is_core_point = cp