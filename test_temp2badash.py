from decimal import Decimal

import requests_mock
import temp2badash


def test_read_temp():
    temp2badash.FILENAME = './test_fixtures/good_example.data'
    assert temp2badash._read_temp() == Decimal('68.9')
    temp2badash.FILENAME = './test_fixtures/bad_example.data'
    assert temp2badash._read_temp() is None


def test_send_temp():
    temp2badash.BADASH_API_KEY = 'xxxx42xxxx'
    temp2badash.BADASH_API_URL = 'http://badash-api.example.com/events'
    with requests_mock.mock() as m:
        m.post('http://badash-api.example.com/events', status_code=201)
        temp2badash._send_to_badash('test-job-slug', Decimal('42.0'))
        assert m.called is True
        assert m.call_count == 1
        call_info = m.request_history[0]
        assert call_info.method == 'POST'
        assert call_info.url == 'http://badash-api.example.com/events'
        assert call_info.json() == {'job': 'test-job-slug', 'result': 0, 'temperature': 42.0}
        temp2badash._send_to_badash('test-job-slug', None)
        call_info = m.request_history[-1]
        assert call_info.json() == {'job': 'test-job-slug', 'result': -1, 'temperature': 0.0}


def test_main():
    temp2badash.BADASH_API_KEY = 'xxxx42xxxx'
    temp2badash.BADASH_API_URL = 'http://badash-api.example.com/events'
    temp2badash.JOB_NAME = 'test-job-slug'
    temp2badash.FILENAME = './test_fixtures/good_example.data'
    with requests_mock.mock() as m:
        m.post('http://badash-api.example.com/events', status_code=201)
        temp2badash.main()
        assert m.called is True
        assert m.call_count == 1
        call_info = m.request_history[0]
        assert call_info.json() == {'job': 'test-job-slug', 'result': 0, 'temperature': 68.9}

