from enum import Enum


class MessageType(Enum):
    XML_ACK = 0000
    REQUEST_CONFIGURATION = 1
    SET_FILTER_SPEED = 9
    REQUEST_LOG_CONFIG = 31
    SET_HEATER_ENABLED = 147
    SET_EQUIPMENT = 164
    CREATE_SCHEDULE = 230
    DELETE_SCHEDULE = 231
    GET_TELEMETRY = 300
    GET_ALARM_LIST = 304
    SET_STANDALONE_LIGHT_SHOW = 308
    GET_FILTER_DIAGNOSTIC_INFO = 386
    HANDSHAKE = 1000
    ACK = 1002
    MSP_TELEMETRY_UPDATE = 1004
    MSP_CONFIGURATIONUPDATE = 1003
    MSP_ALARM_LIST = 1304
    MSP_LEADMESSAGE = 1998
    MSP_BLOCKMESSAGE = 1999


class ColorLogicSpeed(Enum):
    ONE_SIXTEENTH = 0
    ONE_EIGHTH = 1
    ONE_QUARTER = 2
    ONE_HALF = 3
    ONE_TIMES = 4
    TWO_TIMES = 5
    FOUR_TIMES = 6
    EIGHT_TIMES = 7
    SIXTEEN_TIMES = 8


class ColorLogicBrightness(Enum):
    TWENTY_PERCENT = 0
    FOURTY_PERCENT = 1
    SIXTY_PERCENT = 2
    EIGHTY_PERCENT = 3
    ONE_HUNDRED_PERCENT = 4


class ColorLogicShow(Enum):
    VOODOO_LOUNGE = 0
    DEEP_BLUE_SEA = 1
    ROYAL_BLUE = 2
    AFTERNOON_SKY = 3
    AQUA_GREEN = 4
    EMERALD = 5
    CLOUD_WHITE = 6
    WARM_RED = 7
    FLAMINGO = 8
    VIVID_VIOLET = 9
    SANGRIA = 10
    TWILIGHT = 11
    TRANQUILITY = 12
    GEMSTONE = 13
    USA = 14
    MARDI_GRAS = 15
    COOL_CABARET = 16
    #### THESE SHOW IN THE APP AFTER SETTING, BUT MAY NOT MATCH ALL LIGHTS
    YELLOW = 17
    ORANGE = 18
    GOLD = 19
    MINT = 20
    TEAL = 21
    BURNT_ORANGE = 22
    PURE_WHITE = 23
    CRISP_WHITE = 24
    WARM_WHITE = 25
    BRIGHT_YELLOW = 26


class ColorLogicPowerStates(Enum):
    OFF = 0
    POWERING_OFF = 1
    CHANGING_SHOW = 3
    FIFTEEN_SECONDS_WHITE = 4
    SHOW_ACTIVE = 6
