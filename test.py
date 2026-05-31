from datetime import datetime, timedelta
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_FX_MAJORS_EUR_USD

start = datetime(2006, 1, 1)
end = datetime(2026, 5, 31)
instrument = INSTRUMENT_FX_MAJORS_EUR_USD
interval = dukascopy_python.INTERVAL_HOUR_1
offer_side = dukascopy_python.OFFER_SIDE_BID
