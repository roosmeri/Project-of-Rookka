from unittest import TestCase
from Toy_programs.testi.Greeter import Greeter
import io
import sys

class TestGreeter(TestCase):
    def test_greet(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            Greeter().greet()
            output = out.getvalue().strip()
            self.assertEqual(output,"Hello world!")
            print(output)
        finally:
            sys.stdout = saved_stdout

