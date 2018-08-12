import pandas_datareader.data as web
import fix_yahoo_finance as yf
yf.pdr_override()
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

df = web.get_data_yahoo('055550.KS', '2017-01-01')