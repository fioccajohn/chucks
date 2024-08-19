import pandas as pd

from chucks.utils import get_schwab_client

if __name__ == "__main__":
    c = get_schwab_client()
    r = c.get_instruments(r".*Dow Jones.*", c.Instrument.Projection.DESCRIPTION_REGEX)
    instruments = pd.DataFrame.chucks.from_instruments(r)
    responses = [c.get_price_history(s) for s in instruments[:10].index.get_level_values(0)]
    df = pd.DataFrame.chucks.from_candles(responses)

    for i in df.index.get_level_values('symbol').unique():
        print(i)
        print(df.xs(i, level=1))
