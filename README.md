[![CircleCI](https://circleci.com/gh/swilcox/bad-temp-send-cli/tree/master.svg?style=svg)](https://circleci.com/gh/swilcox/bad-temp-send-cli/tree/master)
[![codecov](https://codecov.io/gh/swilcox/bad-temp-send-cli/branch/master/graph/badge.svg)](https://codecov.io/gh/swilcox/bad-temp-send-cli)

# bad-temp-send-cli
1-wire temperature sensor to badash for the Raspberry Pi

## Overview

Simplistic code to read from a 1-Wire temperature device and send the resulting temperature value to BADash (https://github.com/swilcox/badash) as a job event.

## Requirements

* Raspberry Pi
* Python 3.5+
* requests

Install the necessary requirements (really just the requests) into a suitable virtual environment or globally if you intend to use the Pi just for single application.

The following environment variables must be set prior to running the script:

* `BADASH_API_URL` - the API URL endpoint for posting job events typically: `http://your-api-hostname/events`
* `BADASH_API_KEY` - a valid API key for accessing / posting to the API
* `BADASH_JOB_NAME` - the job slug for posting the event (e.g. `my-office-temperature`)
* `W1_FILENAME` - the full path / filename to the W1 device (like: `/sys/devices/w1_bus_master1/28-001454ce00ff/w1_slave`)

Once those values are set, you can execute the script (from the directory it's installed in):

```
$ python ./temp2badash.py
```
