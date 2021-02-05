from TrajectoryPoint import TrajectoryPoint
from Cluster import Cluster
from DBScanUtility import DBScanUtility


class DBScanSD():
    def __init__(self):
        self.result_clusters = []

    def apply_DBScanSD(pts_list, eps, min_pts, spd, direc, is_stop_pt):

        for i in range(len(pts_list)):
            tmp_list = []
            p = pts_list[i]

            if ((p.is_visited()) and (i != (len(pts_list) - 1))
                    and (i % 4096 != 0)):
                continue
            # TODO: is_core_point()
            tmp_list = core_points(pts_list, eps, min_pts, spd, direc,
                                   is_stop_pt)

            if ((tmp_list != None) or (i == (len(pts_list) - 1))
                    or (i % 4096 == 0)):
                dbsc = Cluster()
                dbsc.set_cluster(tmp_list)
                if (tmp_list != None):
                    self.result_clusters.append(dbsc)
                length = len(self.result_clusters)
                flag = True
                if ((i % 4096 == 0) or (i == (len(pts_list) - 1))):
                    while (flag):
                        flag = False
                        for ii in range(length):
                            for iii in range(length):
                                if (ii != iii):
                                    flag = True
                                    continue
                                # TODO: merge_clusters()
                                if (merge_clusters(self.result_clusters[ii],
                                                   self.result_clusters[iii])):
                                    del self.result_clusters[iii]
                                    iii -= 1
                                    length -= 1

        return self.result_clusters

    def merge_clusters(cluster_a, cluster_b):
        merge = False
        if ((cluster_a.get_cluster() == None)
                or (cluster_b.get_cluster() == None)):
            return False
        for i in range(len(cluster_b.get_cluster())):
            p = cluster_b.get_cluster()[i]
            if ((p.is_core_point()) and (p in cluster_a.get_cluster())):
                merge = True
                break
        if (merge):
            for i in range(len(cluster_b.get_cluster())):
                if (not cluster_b.get_cluster()[i] in cluster_a.get_cluster()):
                    cluster_a.get_cluster().append(cluster_b.get_cluster()[i])
        return merge

    def core_points(traj_list, p, eps, min_pts, spd, direc, is_stop_pt):
        cnt = 0
        tmp_list = []

        for q in traj_list:
            if (is_density_reachable(self, p, q, eps, min_pts, spd, direc,
                                     is_stop_pt)):
                cnt += 1
                if (not q in tmp_list):
                    tmp_list.append(q)

        if (cnt >= min_pts):
            p.set_core_point(True)
            p.set_visited(True)
            return tmp_list
        return None
