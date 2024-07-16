# TODO: refactor for no "undefined" because of definition order errors.
from dataclasses import dataclass
from decimal import Decimal
from typing import ClassVar, List, Dict, Union, Optional

from .allowed_values import (
    ASSET_MAIN_TYPES,
    ASSET_TYPES,
    MARKET_TYPES,
    EXCHANGE_TYPES,
)


@dataclass
class SettlementType:
    allowed_values: ClassVar[List[str]] = [
        "A",
        "P",
    ]
    value: str

    def __post_init__(self):
        if self.asset_type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ExpirationType:
    allowed_values: ClassVar[List[str]] = ["M", "Q", "S", "W"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ExerciseType:
    allowed_values: ClassVar[List[str]] = [
        "A",
        "E",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ContractType:
    allowed_values: ClassVar[List[str]] = ["P", "C"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ReferenceOption:
    contractType: ContractType
    cusip: str
    daysToExpiration: int
    deliverables: str
    description: str
    exchange: str
    exchangeName: str
    exerciseType: ExerciseType
    expirationDay: str
    expirationMonth: str
    expirationType: ExpirationType
    expirationYear: str
    isPennyPilot: bool
    lastTradingDay: int
    multiplier: Decimal
    settlementType: SettlementType
    strikePrice: Decimal
    underlying: str


@dataclass
class QuoteOption:
    FiftyTwoWeekHigh: Decimal
    FiftyTwoWeekLow: Decimal
    askPrice: Decimal
    askSize: int
    bidPrice: Decimal
    bidSize: int
    closePrice: Decimal
    delta: Decimal
    gamma: Decimal
    highPrice: Decimal
    indAskPrice: Decimal
    indBidPrice: Decimal
    indQuoteTime: int
    impliedYield: Decimal
    lastPrice: Decimal
    lastSize: int
    lowPrice: Decimal
    mark: Decimal
    markChange: Decimal
    markPercentChange: Decimal
    moneyIntrinsicValue: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    openInterest: Decimal
    openPrice: Decimal
    quoteTime: int
    rho: Decimal
    securityStatus: str
    theoreticalOptionValue: Decimal
    theta: Decimal
    timeValue: Decimal
    totalVolume: int
    tradeTime: int
    underlyingPrice: Decimal
    vega: Decimal
    volatility: Decimal


@dataclass
class AssetType:
    allowed_values: ClassVar[List[str]] = ASSET_TYPES
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class OptionDeliverables:
    symbol: str
    assetType: AssetType
    deliverableUnits: str
    currencyType: str


@dataclass
class OptionContract:

    put_call_allowed_values: ClassVar[List[str]] = [
        "PUT",
        "CALL",
    ]

    putCall: str
    symbol: str
    description: str
    exchangeName: str
    bidPrice: Decimal
    askPrice: Decimal
    lastPrice: Decimal
    markPrice: Decimal
    bidSize: int
    askSize: int
    lastSize: int
    highPrice: Decimal
    lowPrice: Decimal
    openPrice: Decimal
    closePrice: Decimal
    totalVolume: int
    tradeDate: int
    quoteTimeInLong: int
    tradeTimeInLong: int
    netChange: Decimal
    volatility: Decimal
    delta: Decimal
    gamma: Decimal
    theta: Decimal
    vega: Decimal
    rho: Decimal
    timeValue: Decimal
    openInterest: Decimal
    isInTheMoney: bool
    theoreticalOptionValue: Decimal
    theoreticalVolatility: Decimal
    isMini: bool
    isNonStandard: bool
    optionDeliverablesList: OptionDeliverables
    strikePrice: Decimal
    expirationDate: int
    daysToExpiration: Decimal
    expirationType: ExpirationType
    lastTradingDay: int
    multiplier: Decimal
    settlementType: SettlementType
    deliverableNote: str
    isIndexOption: bool
    percentChange: Decimal
    markChange: Decimal
    markPercentChange: Decimal
    isPennyPilot: bool
    intrinsicValue: Decimal
    optionRoot: str


@dataclass
class OptionContractMap:
    # TODO oneOf?
    optionContractMap: Dict[str, OptionContract]


@dataclass
class Underlying:

    exchange_allowed_types: ClassVar[List[str]] = EXCHANGE_TYPES

    ask: Decimal
    askSize: int
    bid: Decimal
    bidSize: int
    change: Decimal
    close: Decimal
    delayed: bool
    description: str
    exchangeName: str
    fiftyTwoWeekHigh: Decimal
    fiftyTwoWeekLow: Decimal
    highPrice: Decimal
    last: Decimal
    lowPrice: Decimal
    mark: Decimal
    markChange: Decimal
    markPercentChange: Decimal
    openPrice: Decimal
    percentChange: Decimal
    quoteTime: int
    symbol: str
    totalVolume: int
    tradeTime: int

    def __post_init__(self):
        if self.exchangeName not in self.exchange_allowed_types:
            raise ValueError(f"exchangeName must be one of {self.allowed_values}")


@dataclass
class ReferenceMutualFund:
    cusip: str
    description: str
    exchange: str
    exchangeName: str


@dataclass
class Screener:

    direction_allowed_values: ClassVar[List[str]] = [
        "up",
        "down",
    ]

    change: Decimal
    description: str
    direction: str
    last: Decimal
    symbol: str
    totalVolume: int

    def __post_init__(self):
        if self.direction not in self.allowed_values:
            raise ValueError(
                f"direction must be one of {self.direction_allowed_values}"
            )


@dataclass
class ReferenceIndex:
    description: str
    exchange: str
    exchangeName: str


@dataclass
class QuoteIndex:
    FiftyTwoWeekHigh: Decimal
    FiftyTwoWeekLow: Decimal
    closePrice: Decimal
    highPrice: Decimal
    lastPrice: Decimal
    lowPrice: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    openPrice: Decimal
    securityStatus: str
    totalVolume: int
    tradeTime: int


@dataclass
class QuoteMutualFund:
    FiftyTwoWeekHigh: Decimal
    FiftyTwoWeekLow: Decimal
    closePrice: Decimal
    nAV: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    securityStatus: str
    totalVolume: int
    tradeTime: int


@dataclass
class ReferenceFuture:
    description: str
    exchange: str
    exchangeName: str
    futureActiveSymbol: str
    futureExpirationDate: int
    futureIsActive: bool
    futureMultiplier: Decimal
    futurePriceFormat: str
    futureSettlementPrice: Decimal
    futureTradingHours: str
    product: str


@dataclass
class ReferenceFutureOption:
    contractType: ContractType
    description: str
    exchange: str
    exchangeName: str
    multiplier: Decimal
    expirationDate: int
    expirationStyle: str
    strikePrice: Decimal
    underlying: str


@dataclass
class QuoteFutureOption:
    askMICId: str
    askPrice: Decimal
    askSize: int
    bidMICId: str
    bidPrice: Decimal
    bidSize: int
    closePrice: Decimal
    highPrice: Decimal
    lastMICId: str
    lastPrice: Decimal
    lastSize: int
    lowPrice: Decimal
    mark: Decimal
    markChange: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    openInterest: Decimal
    openPrice: Decimal
    quoteTime: int
    securityStatus: str
    settlemetPrice: Decimal
    tick: Decimal
    tickAmount: Decimal
    totalVolume: int
    tradeTime: int


@dataclass
class QuoteFuture:
    askMICId: str
    askPrice: Decimal
    askSize: int
    askTime: int
    bidMICId: str
    bidPrice: Decimal
    bidSize: int
    bidTime: int
    closePrice: Decimal
    futurePercentChange: Decimal
    highPrice: Decimal
    lastMICId: str
    lastPrice: Decimal
    lastSize: int
    lowPrice: Decimal
    mark: Decimal
    netChange: Decimal
    openInterest: Decimal
    openPrice: Decimal
    quoteTime: int
    quotedInSession: bool
    securityStatus: str
    settleTime: int
    tick: Decimal
    tickAmount: Decimal
    totalVolume: int
    tradeTime: int


@dataclass
class ReferenceForex:
    description: str
    exchange: str
    exchangeName: str
    isTradable: bool
    marketMaker: str
    product: str
    tradingHours: str


@dataclass
class QuoteForex:
    FiftyTwoWeekHigh: Decimal
    FiftyTwoWeekLow: Decimal
    askPrice: Decimal
    askSize: int
    bidPrice: Decimal
    bidSize: int
    closePrice: Decimal
    highPrice: Decimal
    lastPrice: Decimal
    lastSize: int
    lowPrice: Decimal
    mark: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    openPrice: Decimal
    quoteTime: int
    securityStatus: str
    tick: Decimal
    tickAmount: Decimal
    totalVolume: int
    tradeTime: int


@dataclass
class RegularMarket:
    regularMarketLastPrice: Decimal
    regularMarketLastSize: int
    regularMarketNetChange: Decimal
    regularMarketPercentChange: Decimal
    regularMarketTradeTime: int


@dataclass
class ReferenceEquity:
    cusip: str
    description: str
    exchange: str
    exchangeName: str
    fsiDesc: str
    htbQuantity: int
    htbRate: Decimal
    isHardToBorrow: bool
    isShortable: bool
    otcMarketTier: str


@dataclass
class QuoteEquity:
    FiftyTwoWeekHigh: Decimal
    FiftyTwoWeekLow: Decimal
    askMICId: str
    askPrice: Decimal
    askSize: int
    askTime: int
    bidMICId: str
    bidPrice: Decimal
    bidSize: int
    bidTime: int
    closePrice: Decimal
    highPrice: Decimal
    lastMICId: str
    lastPrice: Decimal
    lastSize: int
    lowPrice: Decimal
    mark: Decimal
    markChange: Decimal
    markPercentChange: Decimal
    netChange: Decimal
    netPercentChange: Decimal
    openPrice: Decimal
    quoteTime: int
    securityStatus: str
    totalVolume: int
    tradeTime: int
    volatility: Decimal


@dataclass
class FundStrategy:
    allowed_values: ClassVar[List[str]] = [
        "A",
        "L",
        "P",
        "Q",
        "S",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class DivFreq:
    allowed_values: ClassVar[List[int]] = [
        1,
        2,
        3,
        4,
        6,
        11,
        12,
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class Fundamental:
    avg10DaysVolume: Decimal
    avg1YearVolume: Decimal
    declarationDate: str
    divAmount: Decimal
    divExDate: str
    divFreq: DivFreq
    divPayAmount: Decimal
    divPayDate: str
    divYield: Decimal
    eps: Decimal
    fundLeverageFactor: Decimal
    fundStrategy: FundStrategy
    nextDivExDate: str
    nextDividendPayDate: str
    peRatio: Decimal


@dataclass
class AssetMainType:
    allowed_values: ClassVar[List[str]] = ASSET_MAIN_TYPES
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class QuoteType:
    allowed_values: ClassVar[List[str]] = [
        "NBBO",
        "NFL",
    ]
    value: str

    def __post_init__(self):
        if self.asset_type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ExtendedMarket:
    askPrice: Decimal
    askSize: int
    bidPrice: Decimal
    bidSize: int
    lastPrice: Decimal
    lastSize: int
    mark: Decimal
    quoteTime: int
    totalVolume: int
    tradeTime: int


@dataclass
class MarketType:
    allowed_values: ClassVar[List[str]] = MARKET_TYPES
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class Bond:
    cusip: str
    symbol: str
    description: str
    exchange: str
    assetType: AssetType
    bondFactor: str
    bondMultiplier: str
    bondPrice: Decimal
    type: AssetType


@dataclass
class Candle:
    close: Decimal
    datetime: int
    datetimeISO8601: str
    high: Decimal
    low: Decimal
    open: Decimal
    volume: int


@dataclass
class CandleList:
    candles: Candle
    empty: bool
    previousClose: Decimal
    previousCloseDate: int
    symbol: str
    previousCloseDateISO8601: Optional[str] = None


@dataclass
class EquityAssetSubType:
    allowed_values: ClassVar[List[str]] = [
        "COE",
        "PRF",
        "ADR",
        "GDR",
        "CEF",
        "ETF",
        "ETN",
        "UIT",
        "WAR",
        "RGT",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class EquityResponse:
    """Quote info of Equity security"""

    assetMainType: AssetMainType
    assetSubType: EquityAssetSubType
    ssid: int
    symbol: str
    realtime: bool
    quoteType: QuoteType
    extended: ExtendedMarket
    fundamental: Fundamental
    quote: QuoteEquity
    reference: ReferenceEquity
    regular: RegularMarket


@dataclass
class ErrorSource:
    pointer: List[str]  # TODO is this returning a list?
    parameter: str
    header: str


@dataclass
class Error:
    id: str
    status: str
    title: str
    detail: str
    source: ErrorSource


@dataclass
class ErrorResponse:
    errors: List[Error]  # TODO is this returning a list?


@dataclass
class Expiration:
    daysToExpiration: int
    expiration: str
    expirationType: ExpirationType
    standard: bool
    settlementType: SettlementType
    optionRoots: str


@dataclass
class ExpirationChain:
    status: str
    expirationList: List[Expiration]


@dataclass
class ForexResponse:
    assetMainType: AssetMainType
    ssid: int
    symbol: str
    realtime: bool
    quote: QuoteForex
    reference: ReferenceForex


@dataclass
class FundamentalInst:
    symbol: str
    highFiftyTwo: Decimal
    lowFiftyTwo: Decimal
    dividendAmount: Decimal
    dividendYield: Decimal
    dividendDate: str
    peRatio: Decimal
    pegRatio: Decimal
    pbRatio: Decimal
    prRatio: Decimal
    pcfRatio: Decimal
    grossMarginTTM: Decimal
    grossMarginMRQ: Decimal
    netProfitMarginTTM: Decimal
    netProfitMarginMRQ: Decimal
    operatingMarginTTM: Decimal
    operatingMarginMRQ: Decimal
    returnOnEquity: Decimal
    returnOnAssets: Decimal
    returnOnInvestment: Decimal
    quickRatio: Decimal
    currentRatio: Decimal
    interestCoverage: Decimal
    totalDebtToCapital: Decimal
    ltDebtToEquity: Decimal
    totalDebtToEquity: Decimal
    epsTTM: Decimal
    epsChangePercentTTM: Decimal
    epsChangeYear: Decimal
    epsChange: Decimal
    revChangeYear: Decimal
    revChangeTTM: Decimal
    revChangeIn: Decimal
    sharesOutstanding: Decimal
    marketCapFloat: Decimal
    marketCap: Decimal
    bookValuePerShare: Decimal
    shortIntToFloat: Decimal
    shortIntDayToCover: Decimal
    divGrowthRate3Year: Decimal
    dividendPayAmount: Decimal
    dividendPayDate: str
    beta: Decimal
    vol1DayAvg: Decimal
    vol10DayAvg: Decimal
    vol3MonthAvg: Decimal
    avg10DaysVolume: int
    avg1DayVolume: int
    avg3MonthVolume: int
    declarationDate: str
    dividendFreq: int
    eps: Decimal
    corpactionDate: str
    dtnVolume: int
    nextDividendPayDate: str
    nextDividendDate: str
    fundLeverageFactor: Decimal
    fundStrategy: str


@dataclass
class FutureOptionResponse:
    assetMainType: AssetMainType
    ssid: int
    symbol: str
    realtime: bool
    quote: QuoteFutureOption
    reference: ReferenceFutureOption


@dataclass
class FutureResponse:
    assetMainType: AssetMainType
    ssid: int
    symbol: str
    realtime: bool
    quote: QuoteFutureOption
    reference: ReferenceFutureOption


@dataclass
class Hours:
    date: str
    marketType: MarketType


@dataclass
class IndexResponse:
    assetMainType: AssetMainType
    ssid: int
    symbol: str
    realtime: bool
    quote: QuoteIndex
    reference: ReferenceIndex


@dataclass
class Instrument:
    cusip: str
    symbol: str
    description: str
    exchange: str
    assetType: AssetType
    type: AssetType


@dataclass
class InstrumentResponse:
    cusip: str
    symbol: str
    description: str
    exchange: str
    assetType: AssetType
    bondFactor: str
    bondPrice: Decimal
    fundamental: FundamentalInst
    instrumentInfo: Instrument
    bondInstrumentInfo: Bond
    type: AssetType


@dataclass
class Interval:
    start: str
    end: str


@dataclass
class MarketType:
    allowed_values: ClassVar[List[str]] = MARKET_TYPES
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class MutualFundAssetSubType:
    allowed_values: ClassVar[List[str]] = [
        "OEF",
        "CEF",
        "MMF",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class MutualFundResponse:
    assetMainType: AssetMainType
    assetSubType: MutualFundAssetSubType
    ssid: int
    symbol: str
    realtime: bool
    fundamental: Fundamental
    quote: QuoteMutualFund
    reference: ReferenceMutualFund


@dataclass
class OptionChain:
    strategy_allowed_values: ClassVar[List[str]] = [
        "SINGLE",
        "ANALYTICAL",
        "COVERED",
        "VERTICAL",
        "CALENDAR",
        "STRANGLE",
        "STRADDLE",
        "BUTTERFLY",
        "CONDOR",
        "DIAGONAL",
        "COLLAR",
        "ROLL",
    ]

    symbol: str
    status: str
    underlying: Underlying
    strategy: str
    interval: Decimal
    isDelayed: bool
    isIndex: bool
    daysToExpiration: Decimal
    interestRate: Decimal
    underlyingPrice: Decimal
    volatility: Decimal
    callExpDateMap: Dict[str, OptionContractMap]
    putExpDateMap: Dict[str, OptionContractMap]

    def __post_init__(self):
        if self.strategy not in self.strategy_allowed_values:
            raise ValueError(f"strategy must be one of {self.allowed_values}")

    def __post_init__(self):
        if self.putCall not in self.put_call_allowed_values:
            raise ValueError(f"putCall must be one of {self.allowed_values}")


@dataclass
class OptionResponse:
    assetMainType: AssetMainType
    ssid: int
    symbol: str
    realtime: bool
    quote: QuoteOption
    reference: ReferenceOption


@dataclass
class QuoteError:
    invalidCusips: List[str]
    invalidSSIDs: List[int]
    invalidSymbols: List[str]


@dataclass
class QuoteRequest:
    # TODO this is a new pattern for me
    cusips: List[int]
    fields: List[str]
    ssids: List[int]
    symbols: List[str]
    realtime: List[bool]
    indicative: List[bool]


@dataclass
class QuoteResponseObject:
    # TODO oneOf?
    response: Optional[
        Union[
            'EquityResponse',
            'OptionResponse',
            'ForexResponse',
            'FutureResponse',
            'FutureOptionResponse',
            'IndexResponse',
            'MutualFundResponse',
            'QuoteError',
        ]
    ] = None


@dataclass
class QuoteResponse:
    # TODO is this the best naming?
    quoteResponseMap: Dict[str, QuoteResponseObject]
