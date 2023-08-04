
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer_data_web = PrettyPrinter()

get_data = get(BASE_URL + ALL_JSON).json()
printer_data_web.pprint(get_data)