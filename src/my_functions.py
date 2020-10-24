import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

def test_func(x):
    return x

def preprocess_training_data(X_train):
    # Split Data into Continuous and Categorical
    X_train_cat = X_train.select_dtypes(include='object')
    X_train_cont = X_train.select_dtypes(exclude='object')
    
    # Simple Imputer to fill NA numeric values using fit and transform
    si = SimpleImputer()
    X_train_imp = pd.DataFrame(si.fit_transform(X_train_cont), index = X_train_cont.index, columns = X_train_cont.columns)
    
    # Standard Scaler to scale numeric values
    ss = StandardScaler()
    X_train_sc = pd.DataFrame(ss.fit_transform(X_train_imp), index = X_train_imp.index, columns = X_train_imp.columns)
    
    # OneHotEncoder to create features from categorcal data
    ohe = OneHotEncoder(drop = 'if_binary', sparse = False)
    X_train_ohe = pd.DataFrame(ohe.fit_transform(X_train_cat),
                               columns = ohe.get_feature_names(X_train_cat.columns), index = X_train_cat.index)
    
    X_train_fin = X_train_sc.join(X_train_ohe)
    
    return X_train_fin, si, ss, ohe

def preprocess_testing_data(X_test, si, ss, ohe):
    # Split Data into Continuous and Categorical
    X_test_cat = X_test.select_dtypes(include='object')
    X_test_cont = X_test.select_dtypes(exclude='object')
    
    # Simple Imputer to fill NA numeric values using transform (NOT FITTING ON TESTING DATA)
    X_test_imp = pd.DataFrame(si.transform(X_test_cont), index = X_test_cont.index, columns = X_test_cont.columns)
    
    # Standard Scaler to scale numeric values
    X_test_sc = pd.DataFrame(ss.transform(X_test_imp), index = X_test_imp.index, columns = X_test_imp.columns)
    
    # OneHotEncoder to create features from categorcal data
    X_test_ohe = pd.DataFrame(ohe.transform(X_test_cat),
                              columns = ohe.get_feature_names(X_test_cat.columns), index = X_test_cat.index)
    
    # Join back numeric and categorical dataframes
    X_test_fin = X_test_sc.join(X_test_ohe)
    
    return X_test_fin

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

def mapp(x):
    if x > 50000:
        return '50k+'
    elif x > 40000:
        return '40 - 50k'
    elif x > 30000:
        return '30 - 40k'
    elif x > 20000:
        return '20 - 30k'
    elif x > 10000:
        return '10 - 20k'
    else:
        return '0 - 10k'

def plot_model_score(x):
    # data entries

    # first simple model
    fsm = ['FSM', 0.75, 0.68, 0.56, 0.57, 0.74, 0.75, 0.73]
    # logistic regression
    lr = ['LR', 0.64, 0.59, 0.66, 0.58, 0.75, 0.64, 0.68]
    # decision tree
    dt = ['DT', 0.74, 0.63, 0.66, 0.64, 0.76, 0.74, 0.75]
    # knn
    knn = ['KNN', 0.75, 0.64, 0.68, 0.66, 0.77, 0.75, 0.76]
    # voting ensemble
    ve = ['VE', 0.76, 0.66, 0.70, 0.67, 0.78, 0.76, 0.77]
    # light gradient boost
    lgb = ['LGB', 0.78, 0.68, 0.71, 0.69, 0.79, 0.78, 0.79]
    # random forest ensemble
    rf = ['RF', 0.78, 0.68, 0.70, 0.69, 0.79, 0.78, 0.79]

    # ada boost
    ab = ['AB', 0.64, 0.58, 0.64, 0.57, 0.73, 0.64, 0.67]
    # averaging ensemble
    ae = ['AE', 0.76, 0.65, 0.69, 0.66, 0.78, 0.76, 0.77]
    # cat boost
    cb = ['CB', 0.75, 0.65, 0.71, 0.66, 0.79, 0.75, 0.77]
    # gradient boost
    gb = ['GB', 0.69, 0.61, 0.66, 0.60, 0.75, 0.69, 0.71]
    # stacking all 11 models
    st = ['ST', 0.75, 0.65, 0.69, 0.66, 0.77, 0.75, 0.76]

        # order of our presentation slides
    scores = [fsm, lr, dt, knn, ve, ae, rf, ab, gb, lgb, cb, st]
    ds = pd.DataFrame(data = scores, columns = ['model', 'accuracy', 'precision_macro_avg', 'recall_macro_avg', 'f1-score_macro_avg', 'precision_weighted_avg', 'recall_weighted_avg', 'f1-score_weighted_avg'])
    
    sns.set(context = 'poster', style = 'whitegrid')
    if x > ds.shape[0]: return False
    plt.figure(figsize = (10,5))
    title = 'Model Score'
    xlabel = ''
    ylabel = ''
    ylim = (0.55, 0.8)
    colors = [ 'black', '#f48328', '#4eb4ac', '#c7ad82', '#f48328', '#4eb4ac', '#c7ad82']
    plot_cols = ['accuracy', 'precision_macro_avg', 'recall_macro_avg', 'f1-score_macro_avg']
    marker_size = 7
    if x == 1: marker_size = 10
    counter = 0
    fg, ax = plt.subplots(figsize = (20,10))
    plot_df = ds.head(x)
    
    for i in plot_cols:
        sns.lineplot(x = 'model', y= i, data = plot_df, color = colors[counter], linewidth = 4, ax = ax)
        sns.swarmplot(x = 'model', y= i, data = plot_df, size = marker_size, color = colors[counter], ax = ax)
        counter += 1

    ax.set(title = title, xlabel = xlabel, ylabel = ylabel, ylim = ylim)
#     plt.savefig(f'{x}_model_{plot_df.model[x-1]}', dpi=300, bbox_inches='tight')

    plt.show()
    return True