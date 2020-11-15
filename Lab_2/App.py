import requests
import ntplib
from datetime import datetime


def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time:", d['time'])
    try:
        print("Date:", d['date'])
    except KeyError:
        print("No date!!!")
        raise KeyError
    try: 
    	print("Good " + home_work(d['time']))
    except RuntimeError as e:
    	print()

def main(url=''):
    if not url:
        print("No URL")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
    else:
        check_time(get_time_if_url_not_work())
    return True


def home_work(currenttime):
	if 'AM' in currenttime:
		return 'Day'
	elif 'PM' in currenttime:
		return 'Night'
	else: 
	     raise RuntimeError("ErrorTime!")
	
if __name__ == "__main__":
    a = "-"
    print(a + "\nResult without parameters: ")
    main()
    print(a + "\nResult with true URL: ")
    main('http://date.jsontest.com/')
