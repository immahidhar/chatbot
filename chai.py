{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import math\n",
    "from scipy.spatial import distance as dis\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe_1 = pd.DataFrame(data = {'time':[0,0,0,1,1,1,2,2,2],'index':[0,1,2,0,1,2,0,1,2],'p1':[10,12,14,23,6,-1,12,32,99],'p2':[11,150,-19,14,22,48,102,-10,2],'p3':[22,67,93,17,77,23,98,105,49]})\n",
    "dataframe_2 = pd.DataFrame(data = {'time':[0,0,0,1,1,1,2,2,2],'index':[0,1,2,0,1,2,0,1,2],'p1':[27,-4,13,17,9,11,37,104,14],'p2':[16,52,155,-15,24,14,5,109,-12],'p3':[19,27,69,97,31,27,51,102,107]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>17.972201</td>\n",
       "      <td>43.611925</td>\n",
       "      <td>151.505775</td>\n",
       "      <td>79.686887</td>\n",
       "      <td>15.842980</td>\n",
       "      <td>5.916080</td>\n",
       "      <td>40.074930</td>\n",
       "      <td>157.607106</td>\n",
       "      <td>88.147603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>143.125819</td>\n",
       "      <td>107.051390</td>\n",
       "      <td>5.477226</td>\n",
       "      <td>167.779617</td>\n",
       "      <td>131.076314</td>\n",
       "      <td>141.763888</td>\n",
       "      <td>148.006757</td>\n",
       "      <td>106.630202</td>\n",
       "      <td>166.877200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>82.885463</td>\n",
       "      <td>98.595132</td>\n",
       "      <td>175.650221</td>\n",
       "      <td>6.403124</td>\n",
       "      <td>75.617458</td>\n",
       "      <td>73.851202</td>\n",
       "      <td>53.563047</td>\n",
       "      <td>156.732256</td>\n",
       "      <td>15.652476</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>4.898979</td>\n",
       "      <td>47.675990</td>\n",
       "      <td>150.615404</td>\n",
       "      <td>85.305334</td>\n",
       "      <td>22.181073</td>\n",
       "      <td>15.620499</td>\n",
       "      <td>37.854986</td>\n",
       "      <td>151.033109</td>\n",
       "      <td>94.111636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>61.975802</td>\n",
       "      <td>59.160798</td>\n",
       "      <td>133.424136</td>\n",
       "      <td>43.474130</td>\n",
       "      <td>46.141088</td>\n",
       "      <td>50.882217</td>\n",
       "      <td>43.886217</td>\n",
       "      <td>133.409145</td>\n",
       "      <td>46.043458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>42.708313</td>\n",
       "      <td>6.403124</td>\n",
       "      <td>117.307289</td>\n",
       "      <td>98.838252</td>\n",
       "      <td>27.202941</td>\n",
       "      <td>36.276714</td>\n",
       "      <td>63.851390</td>\n",
       "      <td>144.868906</td>\n",
       "      <td>104.312032</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>117.736995</td>\n",
       "      <td>88.300623</td>\n",
       "      <td>60.423505</td>\n",
       "      <td>117.111058</td>\n",
       "      <td>102.868849</td>\n",
       "      <td>113.075196</td>\n",
       "      <td>110.648091</td>\n",
       "      <td>92.352585</td>\n",
       "      <td>114.372199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>89.983332</td>\n",
       "      <td>105.943381</td>\n",
       "      <td>169.947051</td>\n",
       "      <td>17.720045</td>\n",
       "      <td>84.622692</td>\n",
       "      <td>84.267431</td>\n",
       "      <td>56.267220</td>\n",
       "      <td>139.118654</td>\n",
       "      <td>18.220867</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>79.246451</td>\n",
       "      <td>116.589022</td>\n",
       "      <td>176.649370</td>\n",
       "      <td>96.524608</td>\n",
       "      <td>94.382202</td>\n",
       "      <td>91.498634</td>\n",
       "      <td>62.104750</td>\n",
       "      <td>119.511506</td>\n",
       "      <td>103.850855</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            0           1           2           3           4           5  \\\n",
       "0   17.972201   43.611925  151.505775   79.686887   15.842980    5.916080   \n",
       "1  143.125819  107.051390    5.477226  167.779617  131.076314  141.763888   \n",
       "2   82.885463   98.595132  175.650221    6.403124   75.617458   73.851202   \n",
       "3    4.898979   47.675990  150.615404   85.305334   22.181073   15.620499   \n",
       "4   61.975802   59.160798  133.424136   43.474130   46.141088   50.882217   \n",
       "5   42.708313    6.403124  117.307289   98.838252   27.202941   36.276714   \n",
       "6  117.736995   88.300623   60.423505  117.111058  102.868849  113.075196   \n",
       "7   89.983332  105.943381  169.947051   17.720045   84.622692   84.267431   \n",
       "8   79.246451  116.589022  176.649370   96.524608   94.382202   91.498634   \n",
       "\n",
       "            6           7           8  \n",
       "0   40.074930  157.607106   88.147603  \n",
       "1  148.006757  106.630202  166.877200  \n",
       "2   53.563047  156.732256   15.652476  \n",
       "3   37.854986  151.033109   94.111636  \n",
       "4   43.886217  133.409145   46.043458  \n",
       "5   63.851390  144.868906  104.312032  \n",
       "6  110.648091   92.352585  114.372199  \n",
       "7   56.267220  139.118654   18.220867  \n",
       "8   62.104750  119.511506  103.850855  "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matching_distance  = dis.cdist(dataframe_1.iloc[0:,2:],dataframe_2.iloc[0:,2:], metric='euclidean')\n",
    "matching_distance_df = pd.DataFrame(matching_distance)\n",
    "matching_distance_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "row = matching_distance_df.iloc[1]\n",
    "row.plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dataframe_1[['time']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "matching_distance_df.set_index('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "for time in range(0,3):\n",
    "    #when time = 0\n",
    "    if dataframe_1['time']==time:\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>time</th>\n",
       "      <th>index</th>\n",
       "      <th>p1</th>\n",
       "      <th>p2</th>\n",
       "      <th>p3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>27</td>\n",
       "      <td>16</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>-4</td>\n",
       "      <td>52</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>13</td>\n",
       "      <td>155</td>\n",
       "      <td>69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>17</td>\n",
       "      <td>-15</td>\n",
       "      <td>97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "      <td>24</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>11</td>\n",
       "      <td>14</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>37</td>\n",
       "      <td>5</td>\n",
       "      <td>51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>104</td>\n",
       "      <td>109</td>\n",
       "      <td>102</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>14</td>\n",
       "      <td>-12</td>\n",
       "      <td>107</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   time  index   p1   p2   p3\n",
       "0     0      0   27   16   19\n",
       "1     0      1   -4   52   27\n",
       "2     0      2   13  155   69\n",
       "3     1      0   17  -15   97\n",
       "4     1      1    9   24   31\n",
       "5     1      2   11   14   27\n",
       "6     2      0   37    5   51\n",
       "7     2      1  104  109  102\n",
       "8     2      2   14  -12  107"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dataframe_2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
