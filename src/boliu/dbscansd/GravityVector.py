from TrajectoryPoint import TrajectoryPoint

class GravityVector(TrajectoryPoint):
    # extends TrajectoryPoint

    def __init__(self, lon, lat, cog, sog, md):
        self.latitude = lat
        self.longitude = lon
        self.cog = cog
        self.sog = sog
        self.median_distance = md

    def get_median_distance(self):
        return self.median_distance

    def set_median_distance(self, md):
        self.median_distance = md
    


