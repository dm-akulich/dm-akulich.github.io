#!/usr/bin/env python3
import unittest
import add_new_post


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_new_post.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(add_new_post.sub(4, 2), 2)

    def test_mul(self):
        self.assertEqual(add_new_post.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(add_new_post.div(8, 4), 2)


if __name__ == "__main__":
    unittest.main()
