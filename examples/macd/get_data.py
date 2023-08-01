from vnpy_mysql import Database
from vnpy_rqdata import Datafeed
from vnpy.trader.object import HistoryRequest, BarData
from vnpy.trader.database import DB_TZ
from vnpy.trader.constant import Exchange, Interval
from datetime import datetime
from typing import Dict, List, Set, Optional, Callable

datefeed = Datafeed()
datefeed.init()


def get_data_to_db(start: datetime, end: datetime,
                   symbol: str, exchange: Exchange, internal: Interval) -> Optional[List[BarData]]:
    hr = HistoryRequest(symbol, exchange, start, end, internal)
    return datefeed.query_bar_history(hr)
