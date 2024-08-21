import pandas as pd
import chucks
from chucks.utils import get_schwab_client

if __name__ == "__main__":
    c = get_schwab_client()
    r = c.get_instruments(r".*Dow Jones.*", c.Instrument.Projection.DESCRIPTION_REGEX)
    chucks.ChucksAccessor.set_client(c)

    instruments = c.get_instruments(('SPY', 'DIA', 'QQQ',), c.Instrument.Projection.FUNDAMENTAL)
    i = pd.DataFrame.chucks.read_instruments(instruments)
    q = i.chucks.get_quotes()
