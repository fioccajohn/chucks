from dataclasses import dataclass
from typing import Optional, List, ClassVar, Union, Dict
from decimal import Decimal

# TODO
# All the collections
# Reordering for import references before breaking out into individual modules.



@dataclass
class OrderStrategyType:
    allowed_values: ClassVar[List[str]] = [
        "SINGLE",
        "CANCEL",
        "RECALL",
        "PAIR",
        "FLATTEN",
        "TWO_DAY_SWAP",
        "BLAST_ALL",
        "OCO",
        "TRIGGER",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class OrderTypeRequest:
    "Same as orderType, but does not have UNKNOWN since this type is not allowed as an input"

    allowed_values: ClassVar[List[str]] = [
        "MARKET",
        "LIMIT",
        "STOP",
        "STOP_LIMIT",
        "TRAILING_STOP",
        "CABINET",
        "NON_MARKETABLE",
        "MARKET_ON_CLOSE",
        "EXERCISE",
        "TRAILING_STOP_LIMIT",
        "NET_DEBIT",
        "NET_CREDIT",
        "NET_ZERO",
        "LIMIT_ON_CLOSE",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class PriceLinkType:
    allowed_values: ClassVar[List[str]] = ["VALUE", "PERCENT", "TICK"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class PriceLinkBasis:
    allowed_values: ClassVar[List[str]] = [
        "MANUAL",
        "BASE",
        "TRIGGER",
        "LAST",
        "BID",
        "ASK",
        "ASK_BID",
        "MARK",
        "AVERAGE",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ServiceError:
    message: str
    errors: List[str]


@dataclass
class Session:
    allowed_values: ClassVar[List[str]] = ["NORMAL", "AM", "PM", "SEAMLESS"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class SettlementInstruction:
    allowed_values: ClassVar[List[str]] = ["REGULAR", "CASH", "NEXT_DAY", "UNKNOWN"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class SpecialInstruction:
    allowed_values: ClassVar[List[str]] = [
        "ALL_OR_NONE",
        "DO_NOT_REDUCE",
        "ALL_OR_NONE_DO_NOT_REDUCE",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")





@dataclass
class StopPriceLinkType:
    allowed_values: ClassVar[List[str]] = ["VALUE", "PERCENT", "TICK"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class StopPriceOffset:
    value: Decimal


@dataclass
class Status:
    allowed_values: ClassVar[List[str]] = [
        "AWAITING_PARENT_ORDER",
        "AWAITING_CONDITION",
        "AWAITING_STOP_CONDITION",
        "AWAITING_MANUAL_REVIEW",
        "ACCEPTED",
        "AWAITING_UR_OUT",
        "PENDING_ACTIVATION",
        "QUEUED",
        "WORKING",
        "REJECTED",
        "PENDING_CANCEL",
        "CANCELED",
        "PENDING_REPLACE",
        "REPLACED",
        "FILLED",
        "EXPIRED",
        "NEW",
        "AWAITING_RELEASE_TIME",
        "PENDING_ACKNOWLEDGEMENT",
        "PENDING_RECALL",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class StopPriceLinkBasis:
    allowed_values: ClassVar[List[str]] = [
        "MANUAL",
        "BASE",
        "TRIGGER",
        "LAST",
        "BID",
        "ASK",
        "ASK_BID",
        "MARK",
        "AVERAGE",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class TransactionType:
    allowed_values: ClassVar[List[str]] = [
        "TRADE",
        "RECEIVE_AND_DELIVER",
        "DIVIDEND_OR_INTEREST",
        "ACH_RECEIPT",
        "ACH_DISBURSEMENT",
        "CASH_RECEIPT",
        "CASH_DISBURSEMENT",
        "ELECTRONIC_FUND",
        "WIRE_OUT",
        "WIRE_IN",
        "JOURNAL",
        "MEMORANDUM",
        "MARGIN_CALL",
        "MONEY_MARKET",
        "SMA_ADJUSTMENT",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class TaxLotMethod:
    allowed_values: ClassVar[List[str]] = [
        "FIFO",
        "LIFO",
        "HIGH_COST",
        "LOW_COST",
        "AVERAGE_COST",
        "SPECIFIC_LOT",
        "LOSS_HARVESTER",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class StopType:
    allowed_values: ClassVar[List[str]] = ["STANDARD", "BID", "ASK", "LAST", "MARK"]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class RequestedDestination:
    allowed_values: ClassVar[List[str]] = [
        "INET",
        "ECN_ARCA",
        "CBOE",
        "AMEX",
        "PHLX",
        "ISE",
        "BOX",
        "NYSE",
        "NASDAQ",
        "BATS",
        "C2",
        "AUTO",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class OrderType:
    allowed_values: ClassVar[List[str]] = [
        "MARKET",
        "LIMIT",
        "STOP",
        "STOP_LIMIT",
        "TRAILING_STOP",
        "CABINET",
        "NON_MARKETABLE",
        "MARKET_ON_CLOSE",
        "EXERCISE",
        "TRAILING_STOP_LIMIT",
        "NET_DEBIT",
        "NET_CREDIT",
        "NET_ZERO",
        "LIMIT_ON_CLOSE",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class AccountNumberHash:
    accountNumber: str
    hashValue: str


@dataclass
class AmountIndicator:
    allowed_values: ClassVar[List[str]] = [
        "DOLLARS",
        "SHARES",
        "ALL_SHARES",
        "PERCENTAGE",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ApiOrderStatus:
    allowed_values: ClassVar[List[str]] = [
        "AWAITING_PARENT_ORDER",
        "AWAITING_CONDITION",
        "AWAITING_STOP_CONDITION",
        "AWAITING_MANUAL_REVIEW",
        "ACCEPTED",
        "AWAITING_UR_OUT",
        "PENDING_ACTIVATION",
        "QUEUED",
        "WORKING",
        "REJECTED",
        "PENDING_CANCEL",
        "CANCELED",
        "PENDING_REPLACE",
        "REPLACED",
        "FILLED",
        "EXPIRED",
        "NEW",
        "AWAITING_RELEASE_TIME",
        "PENDING_ACKNOWLEDGEMENT",
        "PENDING_RECALL",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class APIRuleAction:
    allowed_values: ClassVar[List[str]] = [
        "ACCEPT",
        "ALERT",
        "REJECT",
        "REVIEW",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class AssetType:
    allowed_values: ClassVar[List[str]] = [
        "EQUITY",
        "MUTUAL_FUND",
        "OPTION",
        "FUTURE",
        "FOREX",
        "INDEX",
        "CASH_EQUIVALENT",
        "FIXED_INCOME",
        "PRODUCT",
        "CURRENCY",
        "COLLECTIVE_INVESTMENT",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class Currency:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal

@dataclass
class Forex:
    allowed_values: ClassVar[List[str]] = ["STANDARD", "NBBO", "UNKNOWN"]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str
    baseCurrency: Currency
    counterCurrency: Currency

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class CollectiveInvestment:
    allowed_values: ClassVar[List[str]] = [
        "UNIT_INVESTMENT_TRUST",
        "EXCHANGE_TRADED_FUND",
        "CLOSED_END_FUND",
        "INDEX",
        "UNITS",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class AccountAPIOptionDeliverable:

    allowed_values: ClassVar[List[str]] = ["USD", "CAD", "EUR", "JPY"]

    symbol: str
    deliverableUnits: Decimal
    apiCurrencyType: str
    assetType: AssetType

    def __post_init__(self):
        if self.apiCurrencyType not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class CashBalance:
    cashAvailableForTrading: Decimal
    cashAvailableForWithdrawal: Decimal
    cashCall: Decimal
    longNonMarginableMarketValue: Decimal
    totalCash: Decimal
    cashDebitCallValue: Decimal
    unsettledCash: Decimal


@dataclass
class CashInitialBalance:
    accruedInterest: Decimal
    cashAvailableForTrading: Decimal
    cashAvailableForWithdrawal: Decimal
    cashBalance: Decimal
    bondValue: Decimal
    cashReceipts: Decimal
    liquidationValue: Decimal
    longOptionMarketValue: Decimal
    longStockValue: Decimal
    moneyMarketFund: Decimal
    mutualFundValue: Decimal
    shortOptionMarketValue: Decimal
    shortStockValue: Decimal
    isInCall: Decimal
    unsettledCash: Decimal
    cashDebitCallValue: Decimal
    pendingDeposits: Decimal
    accountValue: Decimal


@dataclass
class ComplexOrderStrategyType:
    allowed_values: ClassVar[List[str]] = [
        "NONE",
        "COVERED",
        "VERTICAL",
        "BACK_RATIO",
        "CALENDAR",
        "DIAGONAL",
        "STRADDLE",
        "STRANGLE",
        "COLLAR_SYNTHETIC",
        "BUTTERFLY",
        "CONDOR",
        "IRON_CONDOR",
        "VERTICAL_ROLL",
        "COLLAR_WITH_STOCK",
        "DOUBLE_DIAGONAL",
        "UNBALANCED_BUTTERFLY",
        "UNBALANCED_CONDOR",
        "UNBALANCED_IRON_CONDOR",
        "UNBALANCED_VERTICAL_ROLL",
        "MUTUAL_FUND_SWAP",
        "CUSTOM",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class DateParam:
    date: str


@dataclass
class Duration:

    allowed_values: ClassVar[List[str]] = [
        "DAY",
        "GOOD_TILL_CANCEL",
        "FILL_OR_KILL",
        "IMMEDIATE_OR_CANCEL",
        "END_OF_WEEK",
        "END_OF_MONTH",
        "NEXT_END_OF_MONTH",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class ExecutionLeg:
    legId: int
    price: Decimal
    quantity: Decimal
    mismarkedQuantity: Decimal
    instrumentId: int
    time: str


@dataclass
class FeeType:
    allowed_values: ClassVar[List[str]] = [
        "COMMISSION",
        "SEC_FEE",
        "STR_FEE",
        "R_FEE",
        "CDSC_FEE",
        "OPT_REG_FEE",
        "ADDITIONAL_FEE",
        "MISCELLANEOUS_FEE",
        "FTT",
        "FUTURES_CLEARING_FEE",
        "FUTURES_DESK_OFFICE_FEE",
        "FUTURES_EXCHANGE_FEE",
        "FUTURES_GLOBEX_FEE",
        "FUTURES_NFA_FEE",
        "FUTURES_PIT_BROKERAGE_FEE",
        "FUTURES_TRANSACTION_FEE",
        "LOW_PROCEEDS_COMMISSION",
        "BASE_CHARGE",
        "GENERAL_CHARGE",
        "GST_FEE",
        "TAF_FEE",
        "INDEX_OPTION_FEE",
        "TEFRA_TAX",
        "STATE_TAX",
        "UNKNOWN",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class Instruction:
    allowed_values: ClassVar[List[str]] = [
        "BUY",
        "SELL",
        "BUY_TO_COVER",
        "SELL_SHORT",
        "BUY_TO_OPEN",
        "BUY_TO_CLOSE",
        "SELL_TO_OPEN",
        "SELL_TO_CLOSE",
        "EXCHANGE",
        "SELL_SHORT_EXEMPT",
    ]
    value: str

    def __post_init__(self):
        if self.value not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class AccountCashEquivalent:
    allowed_values: ClassVar[List[str]] = [
        "SWEEP_VEHICLE",
        "SAVINGS",
        "MONEY_MARKET_FUND",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class AccountEquity:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal


@dataclass
class AccountFixedIncome:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    maturityDate: str
    factor: Decimal
    variableRate: Decimal


@dataclass
class AccountMutualFund:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal


@dataclass
class AccountOption:

    putcall_allowed_values: ClassVar[List[str]] = ["PUT", "CALL", "UNKNOWN"]
    type_allowed_values: ClassVar[List[str]] = [
        "VANILLA",
        "BINARY",
        "BARRIER",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    optionDeliverables: AccountAPIOptionDeliverable
    putCall: str
    optionMultiplier: int
    type: str
    underlyingSymbol: str

    def __post_init__(self):
        if self.putCall not in self.putcall_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class AccountsInstrument:
    oneOf: Union[
        AccountCashEquivalent,
        AccountEquity,
        AccountFixedIncome,
        AccountMutualFund,
        AccountOption,
    ]


@dataclass
class Position:
    shortQuantity: Decimal
    averagePrice: Decimal
    currentDayProfitLoss: Decimal
    currentDayProfitLossPercentage: Decimal
    longQuantity: Decimal
    settledLongQuantity: Decimal
    settledShortQuantity: Decimal
    agedQuantity: Decimal
    instrument: AccountsInstrument
    marketValue: Decimal
    maintenanceRequirement: Decimal
    averageLongPrice: Decimal
    averageShortPrice: Decimal
    taxLotAverageLongPrice: Decimal
    taxLotAverageShortPrice: Decimal
    longOpenProfitLoss: Decimal
    shortOpenProfitLoss: Decimal
    previousSessionLongQuantity: Decimal
    previousSessionShortQuantity: Decimal
    currentDayCost: Decimal




@dataclass
class MarginBalance:
    availableFunds: Decimal
    availableFundsNonMarginableTrade: Decimal
    buyingPower: Decimal
    buyingPowerNonMarginableTrade: Decimal
    dayTradingBuyingPower: Decimal
    dayTradingBuyingPowerCall: Decimal
    equity: Decimal
    equityPercentage: Decimal
    longMarginValue: Decimal
    maintenanceCall: Decimal
    maintenanceRequirement: Decimal
    marginBalance: Decimal
    regTCall: Decimal
    shortBalance: Decimal
    shortMarginValue: Decimal
    sma: Decimal
    isInCall: Decimal
    stockBuyingPower: Decimal
    optionBuyingPower: Decimal


@dataclass
class MarginInitialBalance:
    accruedInterest: Decimal
    availableFundsNonMarginableTrade: Decimal
    bondValue: Decimal
    buyingPower: Decimal
    cashBalance: Decimal
    cashAvailableForTrading: Decimal
    cashReceipts: Decimal
    dayTradingBuyingPower: Decimal
    dayTradingBuyingPowerCall: Decimal
    dayTradingEquityCall: Decimal
    equity: Decimal
    equityPercentage: Decimal
    liquidationValue: Decimal
    longMarginValue: Decimal
    longOptionMarketValue: Decimal
    longStockValue: Decimal
    maintenanceCall: Decimal
    maintenanceRequirement: Decimal
    margin: Decimal
    marginEquity: Decimal
    moneyMarketFund: Decimal
    mutualFundValue: Decimal
    regTCall: Decimal
    shortMarginValue: Decimal
    shortOptionMarketValue: Decimal
    shortStockValue: Decimal
    totalCash: Decimal
    isInCall: Decimal
    unsettledCash: Decimal
    pendingDeposits: Decimal
    marginBalance: Decimal
    shortBalance: Decimal
    accountValue: Decimal

@dataclass
class MarginAccount:
    type_allowed_values: ClassVar[List[str]] = ["CASH", "MARGIN"]

    type: str
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    positions: List[Position]
    initialBalances: MarginInitialBalance
    currentBalances: MarginBalance
    projectedBalances: MarginBalance

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class Offer:
    level2Permissions: bool
    mktDataPermission: str



@dataclass
class OrderActivity:

    activitytype_allowed_values: ClassVar[List[str]] = ["EXECUTION", "ORDER_ACTION"]
    executiontype_allowed_values: ClassVar[List[str]] = ["FILL"]

    activityType: str
    executionType: str
    quantity: Decimal
    orderRemainingQuantity: Decimal
    executionLegs: List[ExecutionLeg]

    def __post_init__(self):
        if self.activityType not in self.activitytype_allowed_values:
            raise ValueError(f"value must be one of {self.activitytype_allowed_values}")
        if self.executionType not in self.executiontype_allowed_values:
            raise ValueError(
                f"value must be one of {self.executiontype_allowed_values}"
            )


@dataclass
class OrderBalance:
    orderValue: Decimal
    projectedAvailableFund: Decimal
    projectedBuyingPower: Decimal
    projectedCommission: Decimal


@dataclass
class OrderLeg:
    askPrice: Decimal
    bidPrice: Decimal
    lastPrice: Decimal
    markPrice: Decimal
    projectedCommission: Decimal
    quantity: Decimal
    finalSymbol: str
    # TODO: $long in docs?
    legId: int
    assetType: AssetType
    instruction: Instruction


@dataclass
class OrderLegCollection:

    orderlegtype_allowed_values: ClassVar[List[str]] = [
        "EQUITY",
        "OPTION",
        "INDEX",
        "MUTUAL_FUND",
        "CASH_EQUIVALENT",
        "FIXED_INCOME",
        "CURRENCY",
        "COLLECTIVE_INVESTMENT",
    ]
    positioneffect_allowed_values: ClassVar[List[str]] = [
        "OPENING",
        "CLOSING",
        "AUTOMATIC",
    ]
    quantitytype_allowed_values: ClassVar[List[str]] = [
        "ALL_SHARES",
        "DOLLARS",
        "SHARES",
    ]
    divcapgains_allowed_values: ClassVar[List[str]] = ["REINVEST", "PAYOUT"]

    orderLegType: str
    legId: int
    instrument: AccountsInstrument
    instruction: Instruction
    positionEffect: str
    quantity: Decimal
    quantityType: str
    divCapGains: str
    toSymbol: str

    def __post_init__(self):
        if self.orderLegType not in self.orderlegtype_allowed_values:
            raise ValueError(f"value must be one of {self.orderlegtype_allowed_values}")
        if self.positionEffect not in self.positioneffect_allowed_values:
            raise ValueError(
                f"value must be one of {self.positioneffect_allowed_values}"
            )
        if self.quantityType not in self.quantitytype_allowed_values:
            raise ValueError(f"value must be one of {self.quantitytype_allowed_values}")
        if self.divCapGains not in self.divcapgains_allowed_values:
            raise ValueError(f"value must be one of {self.divcapgains_allowed_values}")


@dataclass
class Order:

    session_allowed_values: ClassVar[List[str]] = ["NORMAL", "AM", "PM", "SEAMLESS"]
    duration_allowed_values: ClassVar[List[str]] = [
        "DAY",
        "GOOD_TILL_CANCEL",
        "FILL_OR_KILL",
        "IMMEDIATE_OR_CANCEL",
        "END_OF_WEEK",
        "END_OF_MONTH",
        "NEXT_END_OF_MONTH",
        "UNKNOWN",
    ]
    stoppricelinkbasis_allowed_values: ClassVar[List[str]] = [
        "MANUAL",
        "BASE",
        "TRIGGER",
        "LAST",
        "BID",
        "ASK",
        "ASK_BID",
        "MARK",
        "AVERAGE",
    ]
    stoppricelinktype_allowed_values: ClassVar[List[str]] = ["VALUE", "PERCENT", "TICK"]

    session: str
    duration: str
    orderType: OrderType
    cancelTime: str
    complexOrderStrategyType: ComplexOrderStrategyType
    quantity: Decimal
    filledQuantity: Decimal
    remainingQuantity: Decimal
    requestedDestination: RequestedDestination
    destinationLinkName: str
    releaseTime: str
    stopPrice: Decimal
    stopPriceLinkBasis: str
    stopPriceLinkType: str
    stopPriceOffset: Decimal
    stopType: StopType
    priceLinkBasis: PriceLinkBasis
    priceLinkType: PriceLinkType
    price: Decimal
    taxLotMethod: TaxLotMethod
    orderLegCollection: OrderLegCollection
    activationPrice: Decimal
    specialInstruction: SpecialInstruction
    orderStrategyType: OrderStrategyType
    orderId: int
    cancelable: bool
    editable: bool
    status: Status
    enteredTime: str
    closeTime: str
    tag: str
    accountNumber: int
    # TODO: strings for now but to figure out format later
    orderActivityCollection: str
    replacingOrderCollection: str
    childOrderStrategies: str
    statusDescription: str

    def __post_init__(self):
        if self.session not in self.session_allowed_values:
            raise ValueError(f"value must be one of {self.session_allowed_values}")
        if self.duration not in self.duration_allowed_values:
            raise ValueError(f"value must be one of {self.duration_allowed_values}")
        if self.stopPriceLinkBasis not in self.stoppricelinkbasis_allowed_values:
            raise ValueError(
                f"value must be one of {self.stoppricelinkbasis_allowed_values}"
            )
        if self.stopPriceLinkType not in self.stoppricelinktype_allowed_values:
            raise ValueError(
                f"value must be one of {self.stoppricelinktype_allowed_values}"
            )


@dataclass
class OrderRequest:
    duration_allowed_values: ClassVar[List[str]] = [
        "DAY",
        "GOOD_TILL_CANCEL",
        "FILL_OR_KILL",
        "IMMEDIATE_OR_CANCEL",
        "END_OF_WEEK",
        "END_OF_MONTH",
        "NEXT_END_OF_MONTH",
        "UNKNOWN",
    ]

    session: Session
    duration: str
    orderType: OrderTypeRequest
    cancelTime: str
    complexOrderStrategyType: ComplexOrderStrategyType
    quantity: Decimal
    filledQuantity: Decimal
    remainingQuantity: Decimal
    destinationLinkName: str
    releaseTime: str
    stopPrice: Decimal
    stopPriceLinkBasis: StopPriceLinkBasis
    stopPriceLinkType: StopPriceLinkType
    stopPriceOffset: Decimal
    stopType: StopType
    priceLinkBasis: PriceLinkBasis
    priceLinkType: PriceLinkType
    price: Decimal
    taxLotMethod: TaxLotMethod
    orderLegCollection: OrderLegCollection
    activationPrice: Decimal
    specialInstruction: SpecialInstruction
    orderStrategyType: OrderStrategyType
    orderId: int
    cancelable: bool
    editable: bool
    status: Status
    enteredTime: str
    closeTime: str
    accountNumber: int
    orderActivityCollection: OrderActivity
    # TODO: what are these collections?
    replacingOrderCollection: str
    childOrderStrategies: str
    statusDescription: str

    def __post_init__(self):
        if self.duration not in self.duration_allowed_values:
            raise ValueError(f"value must be one of {self.duration_allowed_values}")


@dataclass
class OrderStrategy:

    advancedordertype_allowed_values: ClassVar[List[str]] = [
        "NONE",
        "OTO",
        "OCO",
        "OTOCO",
        "OT2OCO",
        "OT3OCO",
        "BLAST_ALL",
        "OTA",
        "PAIR",
    ]
    duration_allowed_values: ClassVar[List[str]] = [
        "DAY",
        "GOOD_TILL_CANCEL",
        "FILL_OR_KILL",
        "IMMEDIATE_OR_CANCEL",
        "END_OF_WEEK",
        "END_OF_MONTH",
        "NEXT_END_OF_MONTH",
        "UNKNOWN",
    ]

    accountNumber: int
    advancedOrderType: str
    closeTime: str
    enteredTime: str
    orderBalance: OrderBalance
    orderStrategyType: OrderStrategyType
    # TODO: "number" in docs?
    orderVersion: int
    session: Session
    status: ApiOrderStatus
    allOrNone: bool
    discretionary: bool
    duration: str
    filledQuantity: Decimal
    orderType: OrderType
    orderValue: Decimal
    price: Decimal
    quantity: Decimal
    remainingQuantity: Decimal
    sellNonMarginableFirst: bool
    settlementInstruction: SettlementInstruction
    strategy: ComplexOrderStrategyType
    amountIndicator: AmountIndicator
    # TODO: is this better as some kind of dict?
    orderLegs: str




@dataclass
class OrderValidationDetail:
    validationRuleName: str
    message: str
    activityMessage: str
    originalSeverity: APIRuleAction
    overrideName: str
    overrideSeverity: APIRuleAction


@dataclass
class OrderValidationResult:
    alerts: OrderValidationDetail
    accepts: OrderValidationDetail
    rejects: OrderValidationDetail
    reviews: OrderValidationDetail
    warns: OrderValidationDetail


@dataclass
class Product:

    allowed_values: ClassVar[List[str]] = [ "TBD", "UNKNOWN" ]


    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")





@dataclass
class SecuritiesAccountBase:
    type_allowed_values: ClassVar[List[str]] = ["CASH", "MARGIN"]

    type: str
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    positions: List[Position]

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.type_allowed_values}")


@dataclass
class StreamerInfo:
    streamerSocketUrl: str
    schwabClientCustomerId: str
    schwabClientCorrelId: str
    schwabClientChannel: str
    schwabClientFunctionId: str


@dataclass
class UserDetails:
    allowed_values: ClassVar[List[str]] = [
        "ADVISOR_USER",
        "BROKER_USER",
        "CLIENT_USER",
        "SYSTEM_USER",
        "UNKNOWN",
    ]

    cdDomainId: str
    login: str
    type: str
    userId: int
    systemUserName: str
    firstName: str
    lastName: str
    brokerRepCode: str

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class Transaction:

    status_allowed_values: ClassVar[List[str]] = [
        "VALID",
        "INVALID",
        "PENDING",
        "UNKNOWN",
    ]
    subaccount_allowed_values: ClassVar[List[str]] = [
        "CASH",
        "MARGIN",
        "SHORT",
        "DIV",
        "INCOME",
        "UNKNOWN",
    ]
    activitytype_allowed_values: ClassVar[List[str]] = [
        "ACTIVITY_CORRECTION",
        "EXECUTION",
        "ORDER_ACTION",
        "TRANSFER",
        "UNKNOWN",
    ]

    activityId: int
    time: str
    user: UserDetails
    description: str
    accountNumber: str
    type: TransactionType
    status: str
    subAccount: str
    tradeDate: str
    settlementDate: str
    positionId: int
    orderId: int
    netAmount: Decimal
    activityType: str
    transferItems: str

    def __post_init__(self):
        if self.status not in self.status_allowed_values:
            raise ValueError(f"value must be one of {self.status_allowed_values}")
        if self.subAccount not in self.subaccount_allowed_values:
            raise ValueError(f"value must be one of {self.subaccount_allowed_values}")
        if self.activityType not in self.activitytype_allowed_values:
            raise ValueError(f"value must be one of {self.activitytype_allowed_values}")


@dataclass
class TransactionBaseInstrument:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal


@dataclass
class TransactionCashEquivalent:

    allowed_values: ClassVar[List[str]] = [
        "SWEEP_VEHICLE",
        "SAVINGS",
        "MONEY_MARKET_FUND",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class TransactionEquity:

    allowed_values: ClassVar[List[str]] = [
        "COMMON_STOCK",
        "PREFERRED_STOCK",
        "DEPOSITORY_RECEIPT",
        "PREFERRED_DEPOSITORY_RECEIPT",
        "RESTRICTED_STOCK",
        "COMPONENT_UNIT",
        "RIGHT",
        "WARRANT",
        "CONVERTIBLE_PREFERRED_STOCK",
        "CONVERTIBLE_STOCK",
        "LIMITED_PARTNERSHIP",
        "WHEN_ISSUED",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class TransactionFixedIncome:
    allowed_values: ClassVar[List[str]] = [
        "BOND_UNIT",
        "CERTIFICATE_OF_DEPOSIT",
        "CONVERTIBLE_BOND",
        "COLLATERALIZED_MORTGAGE_OBLIGATION",
        "CORPORATE_BOND",
        "GOVERNMENT_MORTGAGE",
        "GNMA_BONDS",
        "MUNICIPAL_ASSESSMENT_DISTRICT",
        "MUNICIPAL_BOND",
        "OTHER_GOVERNMENT",
        "SHORT_TERM_PAPER",
        "US_TREASURY_BOND",
        "US_TREASURY_BILL",
        "US_TREASURY_NOTE",
        "US_TREASURY_ZERO_COUPON",
        "AGENCY_BOND",
        "WHEN_AS_AND_IF_ISSUED_BOND",
        "ASSET_BACKED_SECURITY",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    type: str
    maturityDate: str
    factor: Decimal
    multiplier: Decimal
    variableRate: Decimal

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")


@dataclass
class TransactionMutualFund:

    allowed_values: ClassVar[List[str]] = [
        "NOT_APPLICABLE",
        "OPEN_END_NON_TAXABLE",
        "OPEN_END_TAXABLE",
        "NO_LOAD_NON_TAXABLE",
        "NO_LOAD_TAXABLE",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    fundFamilyName: str
    fundFamilySymbol: str
    fundGroup: str
    type: str
    exchangeCutoffTime: str
    purchaseCutoffTime: str
    redemptionCutoffTime: str

    def __post_init__(self):
        if self.type not in self.allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")



@dataclass
class UserPreferenceAccount:

    allowed_values: ClassVar[List[str]] = ["Green", "Blue"]

    accountNumber: str
    primaryAccount: bool
    type: str
    nickName: str
    accountColor: str
    displayAcctId: str
    autoPositionEffect: bool

    def __post_init__(self):
        if self.accountColor not in self.allowed_values:
            raise ValueError(f"accountColor must be one of {self.allowed_values}")

@dataclass
class UserPreference:
    accounts: UserPreferenceAccount
    streamerInfo: StreamerInfo
    offers: Offer











@dataclass
class AccountsBaseInstrument:
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal


@dataclass
class CashAccount:
    allowed_values: ClassVar[List[str]] = ["CASH", "MARGIN"]

    type: str
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    positions: List[Position]
    initialBalances: CashInitialBalance
    currentBalances: CashBalance
    projectedBalances: CashBalance

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")








@dataclass
class FeeValue:
    value: Decimal
    type: FeeType


@dataclass
class FeeLeg:
    feeValues: FeeValue



@dataclass
class Fees:
    feeLegs: FeeLeg

@dataclass
class CommissionValue:
    value: Decimal
    type: FeeType



@dataclass
class CommissionLeg:
    commissionValues: List[CommissionValue]



@dataclass
class Commission:
    commissionLegs: List[CommissionLeg]


@dataclass
class CommissionAndFee:
    commission: Commission
    fee: Fees
    trueCommission: Commission

@dataclass
class PreviewOrder:
    orderId: int
    orderStrategy: OrderStrategy
    orderValidationResult: OrderValidationResult
    commissionAndFee: CommissionAndFee








@dataclass
class SecuritiesAccount:
    oneOf: Union[
        MarginAccount,
        CashAccount,
    ]


@dataclass
class Account:
    securitiesAccount: SecuritiesAccount

@dataclass
class Future:
    allowed_values: ClassVar[List[str]] = ["STANDARD", "UNKNOWN"]
    activeContract: bool
    type: str
    expirationDate: str
    lastTradingDate: str
    firstNoticeDate: str
    multiplier: Decimal
    oneOf: Union[
        'TransactionCashEquivalent',
        'CollectiveInvestment',
        'Currency',
        'TransactionEquity',
        'TransactionFixedIncome',
        'Forex',
        'Index',
        'TransactionMutualFund',
        'TransactionOption',
        'Product',
    ]

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class Index:
    allowed_values: ClassVar[List[str]] = ["BROAD_BASED", "NARROW_BASED", "UNKNOWN"]
    activeContract: bool
    type: str
    oneOf: Union[
        'TransactionCashEquivalent',
        'CollectiveInvestment',
        'Currency',
        'TransactionEquity',
        'TransactionFixedIncome',
        'Forex',
        'Future',
        'TransactionMutualFund',
        'TransactionOption',
        'Product',
    ]

    def __post_init__(self):
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.allowed_values}")

@dataclass
class TransactionInstrument:
    oneOf: Union[
        'TransactionCashEquivalent',
        'CollectiveInvestment',
        'Currency',
        'TransactionEquity',
        'TransactionFixedIncome',
        'Forex',
        'Future',
        'Index',
        'TransactionMutualFund',
        'TransactionOption',
        'Product',
    ]


@dataclass
class TransactionAPIOptionDeliverable:
    rootSymbol: str
    strikePercent: int
    deliverableNumber: int
    deliverableUnits: Decimal
    deliverable: TransactionInstrument
    assetType: AssetType



@dataclass
class TransactionOption:

    putcall_allowed_values: ClassVar[List[str]] = ["PUT", "CALL", "UNKNOWN"]
    type_allowed_values: ClassVar[List[str]] = [
        "VANILLA",
        "BINARY",
        "BARRIER",
        "UNKNOWN",
    ]

    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: Decimal
    expirationDate: str
    # TODO: What's going on here?
    optionDeliverables: TransactionAPIOptionDeliverable
    optionPremiumMultiplier: int
    putCall: str
    strikePrice: Decimal
    type: str
    underlyingSymbol: str
    underlyingCusip: str
    deliverable: TransactionInstrument

    def __post_init__(self):
        if self.putCall not in self.putcall_allowed_values:
            raise ValueError(f"value must be one of {self.putcall_allowed_values}")
        if self.type not in self.type_allowed_values:
            raise ValueError(f"value must be one of {self.type_allowed_values}")







@dataclass
class TransferItem:

    fee_type_allowed_values: ClassVar[List[str]] = [
        "COMMISSION",
        "SEC_FEE",
        "STR_FEE",
        "R_FEE",
        "CDSC_FEE",
        "OPT_REG_FEE",
        "ADDITIONAL_FEE",
        "MISCELLANEOUS_FEE",
        "FUTURES_EXCHANGE_FEE",
        "LOW_PROCEEDS_COMMISSION",
        "BASE_CHARGE",
        "GENERAL_CHARGE",
        "GST_FEE",
        "TAF_FEE",
        "INDEX_OPTION_FEE",
        "UNKNOWN",
    ]
    positioneffect_type_allowed_values: ClassVar[List[str]] = [
        "OPENING",
        "CLOSING",
        "AUTOMATIC",
        "UNKNOWN",
    ]

    instrument: TransactionInstrument
    amount: Decimal
    cost: Decimal
    price: Decimal
    feeType: str
    positionEffect: str

    def __post_init__(self):
        if self.feeType not in self.fee_type_allowed_values:
            raise ValueError(f"value must be one of {self.fee_type_allowed_values}")
        if self.positionEffect not in self.allowed_values:
            raise ValueError(
                f"value must be one of {self.positioneffect_type_allowed_values}"
            )


