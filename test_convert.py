import pytest
from convert_time import convert
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%I:%M:%S%p")
tested_time = now.strftime("%I:%M:%S")

def test_convert_time():
    assert convert(current_time) == tested_time