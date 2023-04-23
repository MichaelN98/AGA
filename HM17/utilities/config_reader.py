import configparser

from HM17.constants import ROOT_DIR

abs_path = f"{ROOT_DIR}/configuration/configuration.ini"
config = configparser.RawConfigParser()
config.read(abs_path)


def get_application_url():
    return config.get('app_data', 'app_url')


def get_application_url_for_main_page():
    return config.get('app_data_main', 'app_url')


def get_application_url_for_pricing_page():
    return config.get('app_data_pricing', 'app_url')


def get_user_creds():
    return (config.get('user_data', 'email'),
            config.get('user_data', 'password'))


def get_browser_id():
    return config.get('browser_data', 'browser_id')


def get_headless_status():
    result = config.get('browser_data', 'headless')
    if result in ['True', 'true', '1']:
        return True
    else:
        return False


def get_invalid_user_creds():
    return (config.get('invalid_user_data', 'email'),
            config.get('invalid_user_data', 'password'))


def get_invalid_user_data_email_creds():
    return (config.get('invalid_user_data_email', 'email'),
            config.get('invalid_user_data_email', 'password'))


def get_invalid_user_data_password_creds():
    return (config.get('invalid_user_data_password', 'email'),
            config.get('invalid_user_data_password', 'password'))


def get_user_creds_facebook():
    return (config.get('user_data_facebook', 'email'),
            config.get('user_data_facebook', 'password'))


def get_user_creds_google():
    return (config.get('user_data_google', 'email'),
            config.get('user_data_google', 'password'))
