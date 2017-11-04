from unittest import TestCase
from Greeter import Greeter
import io
import sys

class TestGreeter(TestCase):
    def test_greet(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        g = Greeter()
        g.greet()
        sys.stdout = sys.__stdout__
        print("captured", capturedOutput.getvalue())

