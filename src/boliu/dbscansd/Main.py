from TrajectoryPoint import TrajectoryPoint
from GravityVector import GravityVector
from GravityVectorExtraction import GravityVectorExtraction
from FileIO import FileIO
from DBScanSD import DBScanSD

import argparse
import pandas as pd
import numpy as np
import os
import sys

class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, '%s: error: %s\n' % (self.prog, message))

def exec_algorithm(in_path, out_path, line_num, eps, min_points, max_spd, max_dir, is_stopping_point):

    f = FileIO()
    points = f.read_file(in_path, line_num, is_stopping_point)
    dbs = DBScanSD()
    clustering_results = dbs.apply_dbscansd(points, eps, min_points, max_spd, max_dir, is_stopping_point)

    #df_stopping = []

    for i in range(len(clustering_results)):
        if (is_stopping_point):
            ppl = clustering_results[i]
            print("yeppers")
            #print(ppl)
        if (not is_stopping_point):
            ppl = extract_gravity_vector(clustering_results[i])
            print("yeppers")
            #print(ppl)


if __name__ == '__main__':
    parser = ArgumentParser(description="args for DBSCANSD")
    parser.add_argument('in_path', type=str, help="the input file path")
    parser.add_argument('out_path', type=str, help="the output file path")
    parser.add_argument('line_num', type=int, help="the designated number of trajectory points for clustering")
    parser.add_argument('eps', type=float, help="1st parameter of DBSCANSD, the radius")
    parser.add_argument('min_points', type=float, help="2nd parameter of DBSCANSD, the minimum number of points")
    parser.add_argument('max_spd', type=float, help="3rd parameter of DBSCANSD, the maximum Speeds' difference")
    parser.add_argument('max_dir', type=float, help="4th parameter of DBSCANSD, the maximum Directions' difference")
    parser.add_argument('is_stopping_pt', type=int, help="if you would like to cluster stopping points (1) or moving points (0)")
    
    args = parser.parse_args()
    args.is_stopping_pt = True if args.is_stopping_pt == 1 else False

    exec_algorithm(args.in_path, args.out_path, args.line_num, args.eps, args.min_points, 
                    args.max_spd, args.max_dir, args.is_stopping_pt)




