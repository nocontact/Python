import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken='4UR73rH3GtsvR1h66Eef')
        df = df.pct_change()
        df.columns = [abbv]
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    #print(main_df.head())
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

#grab_initial_state_data()

HPI_data = pd.read_pickle('fiddy_states.pickle')
HPI_data.plot()
plt.legend().remove()
plt.show()