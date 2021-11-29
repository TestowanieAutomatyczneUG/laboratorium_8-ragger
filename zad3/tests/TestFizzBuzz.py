import unittest
from hamcrest import *

from zad3.src.FizzBuzz import *
class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    def testEquals(self):
        assert_that(self.temp.game(5), equal_to("Buzz"))

    def testAnyOf(self):
        assert_that(self.temp.game(5), all_of(equal_to("Buzz"), contains_string("Buzz")))

    def test_FizzBuzz_3(self):
        assert_that(self.temp.game(3), equal_to("Fizz"))

    def test_FizzBuzz_3_7(self):
        assert_that(calling(self.temp.game).with_args(3.7), raises(ValueError))
    def test_FizzBuzz_3_4(self):
        assert_that(calling(self.temp.game).with_args(3.4), raises(ValueError))
    def test_FizzBuzz_5(self):
        assert_that(self.temp.game(5), equal_to("Buzz"))
    def test_FizzBuzz_5_7(self):
        assert_that(calling(self.temp.game).with_args(5.7), raises(ValueError))

    def test_FizzBuzz_5_4(self):
        assert_that(calling(self.temp.game).with_args(5.4), raises(ValueError))
    def test_FizzBuzz_array(self):
        assert_that(calling(self.temp.game).with_args([]), raises(TypeError))

    def test_FizzBuzz_obj(self):
        assert_that(calling(self.temp.game).with_args({}), raises(TypeError))


    def test_FizzBuzz_none(self):
        assert_that(calling(self.temp.game).with_args(None), raises(TypeError))
    def test_FizzBuzz_15(self):
        assert_that(self.temp.game(15), equal_to("FizzBuzz"))
    def test_FizzBuzz_30(self):
        assert_that(self.temp.game(30), equal_to("FizzBuzz"))

    def test_FizzBuzz_7(self):
        assert_that(calling(self.temp.game).with_args(7), raises(ValueError))
    def test_FizzBuzz_14(self):
        assert_that(calling(self.temp.game).with_args(14), raises(ValueError))

    def test_FizzBuzz_1414141(self):
        assert_that(calling(self.temp.game).with_args(1414141), raises(ValueError))
    def test_FizzBuzz_33(self):
        assert_that(self.temp.game(33), is_not("FizzBuzz"))
    def test_FizzBuzz_60(self):
        assert_that(self.temp.game(60), is_not("Fizz"))
    def test_FizzBuzz_45(self):
        assert_that(self.temp.game(45), is_not("Buzz"))

    def test_FizzBuzz_300(self):
        assert_that(self.temp.game(45), is_not("Buzz"))

    def tearDown(self):
        self.temp = None
