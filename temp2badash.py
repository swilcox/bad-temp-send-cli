from decimal import Decimal
import logging
import os
import re

import requests


log = logging.getLogger()


FILENAME = os.environ.get('W1_FILENAME', default='')
BADASH_API_URL = os.environ.get('BADASH_API_URL', default='')
BADASH_API_KEY = os.environ.get('BADASH_API_KEY', default='xxx')
JOB_NAME = os.environ.get('BADASH_JOB_NAME')


def _read_temp():
    with open(FILENAME, 'rt') as f:
        lines = f.readlines()
        if lines[0].strip()[-3:] == 'YES':
            srch = re.search(r't=([0-9]+)', lines[1])
            print(srch.group(1))
            return (((Decimal(srch.group(1)) / 1000) * 9) / 5) + 32 if srch else None
    return None


def _send_to_badash(job_name, temp):
    data = {
        'job': job_name,
        'result': 0 if temp else -1,
        'temperature': float(round(temp, 1)) if temp else 0.0
    }
    log.info('data: ' + str(data))
    result = requests.post(
        BADASH_API_URL,
        json=data,
        headers={'X-Api-Key': BADASH_API_KEY}
    )
    log.info('result: ' + str(result))

    return result


def main():
    temp_decimal = _read_temp()
    if JOB_NAME:
        _send_to_badash(JOB_NAME, temp_decimal)


if __name__ == "__main__":
    main()
