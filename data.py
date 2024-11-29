class SetupData:
    WAIT_TIME = 5


class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = 'login'
    FORGOT_PASSWORD_PAGE = 'forgot-password'
    RESET_PASSWORD_PAGE = 'reset-password'
    PERSONAL_ACCOUNT_PAGE = 'account/profile'
    ORDER_HISTORY_PAGE = 'account/order-history'
    ORDER_FEED_SECTION = 'feed'


class ApiUrls:
    CREATE_USER = 'api/auth/register'
    DELETE_USER = 'api/auth/user'


class AssertFlags:
    PASSWORD_FIELD_ACTIVE_STATUS = "input_status_active"


class StaticData:
    INGREDIENT_COUNT = '2'
    DEFAULT_ORDER_ID = '9999'