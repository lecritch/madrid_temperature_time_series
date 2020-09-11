import re
import matplotlib.pyplot as plt

def make_pythonic(name):
    '''
    Turns camel case into snake case and lowers it. 
    It also removes all whitespaces to get it in true pythonic form. 
    '''
    # get rid of spaces
    name = name.replace(' ', '')
    # isolate capitals from lower cases using regex
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # make all lower case
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    return name

def plot_series(dfs, cols_or_labels, *args, **kwargs):
    """
    plot one or more Series or DataFrame objects on one figure
    default x values: DATE
    optional kwargs {'xlabel','ylabel'}
    pass other args/kwargs directly to plt.plot()
    
    Code from Robert's notebook. 
    """
    if not(isinstance(dfs,list)):
        plot_series([dfs],cols_or_labels,*args,**kwargs)
    elif not(isinstance(cols_or_labels,list)):
        plot_series(dfs,[cols_or_labels],*args, **kwargs)
    else:
        if ('figsize' in kwargs):
            plt.figure(figsize=kwargs.pop('figsize'))
        else:
            plt.figure(figsize=(16,6))
        if ('xlabel' in kwargs):
            plt.xlabel(kwargs.pop('xlabel'))
        if ('ylabel' in kwargs):
            plt.ylabel(kwargs.pop('ylabel'))
        elif (len(cols_or_labels)==1):
            plt.ylabel(cols_or_labels[0])
        if (len(dfs)<len(cols_or_labels)):
            assert (len(dfs)==1)
            dfs = dfs*len(cols_or_labels)
        elif (len(dfs)>len(cols_or_labels)):
            assert (len(cols_or_labels)==1)
            cols_or_labels = cols_or_labels*len(dfs)
        for j in range(len(dfs)):
            try:
                t=dfs[j].date
                plt.xlabel('date')
            except:
                t=dfs[j].index
            if (isinstance(dfs[j],pd.DataFrame)):
                series = dfs[j][cols_or_labels[j]]
            else:
                series = pd.Series(dfs[j])
                cols_or_labels[j] = (cols_or_labels[j] if (cols_or_labels[j]) else series.name)
            plt.plot(t,series,label=cols_or_labels[j],*args,**kwargs)
        plt.legend()
        plt.grid(True)
        plt.show()
        
def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):    
        fig = plt.figure(figsize=figsize)
        #mpl.rcParams['font.family'] = 'Ubuntu Mono'
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))
        
        y.plot(ax=ts_ax,linestyle='none',marker='o',markersize=4)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax,alpha=0.05)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.05)
        sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')        
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
        plt.show();