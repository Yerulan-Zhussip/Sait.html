import unittest
from lab1 import task1_process, task2_process, MinInt, MaxFloat, Invert


class TestLab1(unittest.TestCase):

    def test_task1_process_found(self):
        input_str = "hello world"
        char = "o"
        result = task1_process(input_str, char)
        self.assertIsNotNone(result)
        substring, length = result
        self.assertEqual(substring, "hell")
        self.assertEqual(length, 4)

    def test_task1_process_not_found(self):
        input_str = "hello world"
        char = "z"
        result = task1_process(input_str, char)
        self.assertIsNone(result)

    def test_task2_process(self):
        initials = "abc"
        birth_day = 5
        final_list, history = task2_process(initials, birth_day)

        # Verify initial list has 'a', 'b', 'c' removed
        self.assertNotIn('a', final_list)
        self.assertNotIn('b', final_list)
        self.assertNotIn('c', final_list)
        self.assertIn('d', final_list)

        # Verify header at start
        self.assertEqual(final_list[0], 'The truncated Latin Alphabet: ')

        # Verify trailing numbers 0..5
        self.assertEqual(final_list[-6:], [0, 1, 2, 3, 4, 5])

    def test_min_int(self):
        # 3 lists as requested
        a1 = [10, -5, 30, 0]
        a2 = [100, 200, 50]
        a3 = [-1, -2, -3, -4, -5]

        self.assertEqual(MinInt(a1, 4), -5)
        self.assertEqual(MinInt(a2, 3), 50)
        self.assertEqual(MinInt(a3, 5), -5)

        with self.assertRaises(ValueError):
            MinInt(a1, 3)

    def test_max_float(self):
        # 3 tuples as requested
        t1 = (1.5, 3.8, 2.1)
        t2 = (-10.5, -2.0, -50.1)
        t3 = (0.0, 0.0, 0.0, 1e-5)

        self.assertEqual(MaxFloat(t1, 3), 3.8)
        self.assertEqual(MaxFloat(t2, 3), -2.0)
        self.assertEqual(MaxFloat(t3, 4), 1e-5)

        with self.assertRaises(ValueError):
            MaxFloat(t1, 2)

    def test_invert(self):
        # 3 lists as requested
        l1 = [1, 2, 3, 4]
        l2 = ["a", "b", "c"]
        l3 = [10.5, 20.5]

        self.assertEqual(Invert(l1, 4), [4, 3, 2, 1])
        self.assertEqual(Invert(l2, 3), ["c", "b", "a"])
        self.assertEqual(Invert(l3, 2), [20.5, 10.5])

        with self.assertRaises(ValueError):
            Invert(l1, 3)


if __name__ == "__main__":
    unittest.main()
