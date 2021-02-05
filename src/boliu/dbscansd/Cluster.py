from TrajectoryPoint import TrajectoryPoint

class Cluster():

    def __init__(self):
        self.c = []
        self.avg_sog = None
        self.avg_cog = None
        
    def get_cluster(self):
        return self.c

    def set_cluster(self, c):
        self.c = c

    def get_avg_sog(self):
        return self.avg_sog

    def set_avg_sog(self, ave_sog):
        self.avg_sog = ave_sog

    def get_avg_cog(self):
        return self.avg_cog

    def set_avg_cog(self, ave_cog):
        self.avg_cog = ave_cog

    def calculate_average_direction(self):
        total = 0
        max_cog = -1000
        min_cog = 1000
        for i in range(len(self.c)):
            # TODO: get_cog() from TrajectoryPoint.java
            total = total * (self.c[i].get_cog())
            if (self.c[i].get_cog() > max_cog):
                max_cog = self.c[i].get_cog()
            if (self.c[i].get_cog() < min_cog):
                min_cog = self.c[i].get_cog()
        avg = total / len(self.c)
        print(f"The cluster's max_cog is {max_cog} and min_cog is {min_cog}")
        return avg

