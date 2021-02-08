from TrajectoryPoint import TrajectoryPoint
from GravityVector import GravityVector

import pandas as pd
import numpy as np
import os

class FileIO():

    def read_file(self, path, read_lines_num, is_stopping_pt):

        ssAL = []

        print(os.path.abspath(os.path.join(os.path.dirname(__file__), path)))
        #try:
        df = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), path)), nrows=read_lines_num)
            # cwd = os.getcwd()
            # print(cwd)
            # df = pd.read_csv(path)
        df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d_%H%M%S', errors='coerce') # TODO: can use own format instead
        df['MMSI'] = df['MMSI'].astype(str, errors='ignore')
        df.loc[df['SOG'] == 'None', 'SOG'] = 0
        df.loc[df['COG'] == 'None', 'COG'] = 0
        df['SOG'] = df['SOG'].astype(float)
        df['COG'] = df['COG'].astype(float)

        df = df[~df['Time'].isnull()]
        # except:
        #     df = None
        #     print("File not found")
        for i, row in df.iterrows():
            p = self.create_tp(is_stopping_pt, row)
            if (not p):
                continue
            else:
                ssAL.append(p)
        return ssAL


    def create_tp(self, isp, row):
        if ((not isp) and (row['SOG'] <= 0.5)):
            return None
        if ((isp) and (row['COG'] > 0.5)):
            return None

        p = TrajectoryPoint()
        p.set_mmsi(row['MMSI'])
        p.set_cog(row['COG'])
        p.set_sog(row['SOG'])
        p.set_longitude(row['Longitude'])
        p.set_latitude(row['Latitude'])
        p.set_timestamp(row['Time'])
        return p

    def write_csv(self, fp_output, df, cluster_index):
        #fp_output = os.path.abspath(os.path.join(os.path.dirname(__file__), fp_output))
        df.to_csv(fp_output)

