from unittest import TestCase
from Toy_programs.testi import Greeter


class TestGreeter(TestCase):
    def test_greet(self):
        g = Greeter()
        answer = g.greet() #korjaa tämä

