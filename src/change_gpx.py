# %% 
''' import '''
from datetime import datetime,timedelta
from sys import argv

# %% 
datetime_str = '2021-04-03T16:55:31Z'

datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')

# %% 
print(datetime_obj)
# %%
delta = timedelta(hours= 10)
new = datetime_obj + delta
# %%
print(new)

# %%
import gpxpy
# %%
