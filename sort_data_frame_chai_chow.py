import math

import pandas as pd
from scipy.spatial import distance as dis


dataframe_1 = pd.DataFrame(data={'time': [0, 0, 0, 1, 1, 1, 2, 2, 2],
                                 'index': [0, 1, 2, 0, 1, 2, 0, 1, 2],
                                 'p1': [10, 12, 14, 23, 6, -1, 12, 32, 99],
                                 'p2': [11, 150, -19, 14, 22, 48, 102, -10, 2],
                                 'p3': [22, 67, 93, 17, 77, 23, 98, 105, 49]})

dataframe_2 = pd.DataFrame(data = {'time':[0,0,0,1,1,1,2,2,2],
                                   'index':[0,1,2,0,1,2,0,1,2],
                                   'p1':[27,-4,13,17,9,11,37,104,14],
                                   'p2':[16,52,155,-15,24,14,5,109,-12],
                                   'p3':[19,27,69,97,31,27,51,102,107]})

print('\n')
print("dataframe_1 : supposed to be the real df")
print(dataframe_1)
print('\n')
print("dataframe_2 : supposed to be the simulated df to be re-simulated")
print(dataframe_2)
print('\n')

noOfIndexFramesPerSecond = 3
noOfTimeFrames = 3

def custom_cdist(df1, df2):
    print(df1)
    print(df2)
    result_arr = []
    for row_mdf1 in df1.itertuples(index=True, name='Pandas'):
        df1_p1 = row_mdf1[1]
        df1_p2 = row_mdf1[2]
        dist_arr = []
        for row_mdf2 in df2.itertuples(index=True, name='Pandas'):
            df2_p1 = row_mdf2[1]
            df2_p2 = row_mdf2[2]
            dist = math.sqrt( ((df1_p1-df2_p1)**2) + ((df1_p2-df2_p2)**2) )
            dist_arr.append(dist)
        result_arr.append(dist_arr)
    result_df = pd.DataFrame(result_arr)
    return result_df

for timeFrame_df1 in range(0,noOfTimeFrames):
    print("Going through time frame -",timeFrame_df1)
    dataframe_1_part = dataframe_1.iloc[(timeFrame_df1*noOfIndexFramesPerSecond):
                                        (noOfIndexFramesPerSecond+timeFrame_df1*noOfIndexFramesPerSecond)]
    print("dataframe_1_part :")
    print(dataframe_1_part)
    dataframe_2_part = dataframe_2.iloc[(timeFrame_df1 * noOfIndexFramesPerSecond):
                                        (noOfIndexFramesPerSecond + timeFrame_df1 * noOfIndexFramesPerSecond)]
    print("dataframe_2_part :")
    print(dataframe_2_part)
    # getting features p1, p2 from the df parts
    df1_features = dataframe_1_part.iloc[0:3,2:4]
    print("df1_features : ")
    print(df1_features)
    df2_features = dataframe_2_part.iloc[0:3,2:4]
    print("df2_features : ")
    print(df2_features)
    # Finding euclidean distance
    matching_dist = dis.cdist(df1_features, df2_features, metric='euclidean')
    matching_distance_df = pd.DataFrame(matching_dist)
    print("matching_distance_df using cdist :")
    print(matching_distance_df)

    custom_matching_dist_df = custom_cdist(df1_features, df2_features)
    print("matching_distance_df using custom method :")
    print(custom_matching_dist_df)

    dist_arr = []
    index_arr = []
    # looping through sparse matrix rows
    for row_mdf in custom_matching_dist_df.itertuples(index=True, name='Pandas'):
        # print(row_mdf)
        dist_arr.append(row_mdf[1])
        dist_arr.append(row_mdf[2])
        dist_arr.append(row_mdf[3])
        print("Distance array = ",dist_arr)
        #min_dist = min(dist_arr)
        #min_index = dist_arr.index(min_dist)
        #print("For index - ",getattr(row_mdf, "Index"), " of df_1 found matching distance of ", min_dist," at index ", min_index, " of df_2")
        close_index_arr = []
        close_dist_arr = []
        for dist in dist_arr:
            if dist>=0:
                if dist<=2:
                    close_index_arr.append(dist_arr.index(dist))
                    close_dist_arr.append(dist)
        print("For index - ", getattr(row_mdf, "Index"), " of df_1 found this array of dist at", close_dist_arr, " whose dist between 0 & 2  at indexes ",close_index_arr, " of df_2")

        # Here is where you do your weighted distance calc with the arr close_dist_arr

        #index_arr.append(min_index)
        dist_arr = []
    #print("Sorted index array of Re-simulated df - ",index_arr)
    index_arr = []
    print('\n')

print('\n')
    