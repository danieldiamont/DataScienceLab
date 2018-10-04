#Author Daniel Diamont

# tabular data
import pandas as pd
import numpy as np
import sklearn as sk

# algorithms and helpers
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import KFold
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.stats import skew
from scipy.stats import pearsonr
from pandas.plotting import scatter_matrix
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import seaborn as sns

# visualization
import matplotlib.pyplot as plt

class FeatureExplorer():

    def __init__(self, data=None, size=(12,18)):

        self.data = data
        self.size = size

    def dtype_info(self):
        '''
        return array with data types and frequencies
        return array with features that contain NaN
        
        '''
        
        dtypes_counts = self.data.get_dtype_counts().values
        dtypes_values = self.data.get_dtype_counts().index
        _ = plt.subplot(311)
        fig_size = [self.size[0],self.size[1]]
        plt.rcParams["figure.figsize"] = fig_size
        _ = plt.bar(dtypes_values,dtypes_counts)
        _ = plt.title("Data Types")
        _ = plt.xlabel("Data types of the Features")
        _ = plt.ylabel("Frequency")
        
        list_NaN = []
        for column in self.data:
            if(self.data[column].isnull().sum() > 0):
                list_NaN.append(column)

        # plot columns with NaN vs. columns without NaN
        number_nan = len(list_NaN)
        number_fill = len(self.data.columns) - number_nan
        _ = plt.subplot(312)
        fig_size = [self.size[0],self.size[1]]
        plt.rcParams["figure.figsize"] = fig_size
        _ = plt.bar(['NaN','Filled'],[number_nan, number_fill])
        _ = plt.title("Number of Columns Containing 'NaN' vs. Valid Columns")
        _ = plt.xlabel("NaN vs. Valid")
        _ = plt.ylabel("Frequency")
        _ = plt.tight_layout()
        
        
        ### ADD SOME VISUALIZATION FOR SPARSE FEATURES


    def univariate_analysis(self):
        '''
        return array of description for each feature
        return list of features with missing values
        return list of skewed features
        return list of features with outliers
        
        '''
        # box plots
        # select continuous variables
        tmp = self.data.select_dtypes(exclude=['category','object','bool'])
        # get rid of NaN
        #scale data
        #filling NA's with the mean of the column:
        tmp = tmp.fillna(tmp.mean())
        tmp = pd.DataFrame(StandardScaler().fit_transform(tmp),columns=tmp.columns.values)
        _ = plt.subplot(313)
        _ = plt.tight_layout()
        fig_size = [self.size[0],self.size[1]]
        plt.rcParams["figure.figsize"] = fig_size
        plt.margins(0.2)
        plt.title("Numeric Feature Boxplot")
        plt.ylabel("Values")
        tmp.boxplot(showmeans=True, rot=90, fontsize='large') 
        
    
    def multivariate_analysis(self, num_corr=5):
        '''
        return list of top n correlated variables
        chi square test on categorical variables
        stacked columns (categorical variables)
        z-test (categorical variables)
        
        '''
        # select continuous variables
        tmp = self.data.select_dtypes(exclude=['category','object','bool'])
        # get rid of NaN
        #scale data
        #filling NA's with the mean of the column:
        tmp = tmp.fillna(tmp.mean())
        tmp = pd.DataFrame(StandardScaler().fit_transform(tmp),columns=tmp.columns.values)
#         corr = pd.DataFrame(get_top_abs_correlations(tmp,n=num_corr))
        #display(HTML(corr.to_html()))
        
        # plot heatmap
        corr_matrix = tmp.corr()
        sns.heatmap(corr_matrix,
                    xticklabels=corr_matrix.columns,
                    yticklabels=corr_matrix.columns,
                    cmap='coolwarm',
                    center=0)
        
