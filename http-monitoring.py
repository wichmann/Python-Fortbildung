#!/usr/bin/env python3

"""

"""

import time
import requests
import datetime


wait_time = 10
url = 'https://bbs-os-brinkstr.de/'
date_file_name = 'http-monitoring.dat'
error_value = 5


def main():
    while True:
        try:
            r = requests.get(url)
            roundtrip = r.elapsed.total_seconds()
        except requests.exceptions.SSLError:
            r = None
            roundtrip = error_value
        except requests.exceptions.ConnectionError:
            r = None
            roundtrip = error_value
        print('Roundtrip time to destination "{}" was {} seconds.'.format(url, roundtrip))
        # write new latency to file
        with open(date_file_name, 'a') as data_file:
            data_file.write('{}, {}\n'.format(datetime.datetime.now().isoformat(), roundtrip))    
        time.sleep(wait_time)
    

if __name__ == '__main__':
    main()
