import join_iterables
import unittest


join = join_iterables

class Test(unittest.TestCase):

    def test_outer(self):
        i1 = [1, 2]
        i2 = [2, 3]
        result = list(join.generic_join(i1, i2, 'outer'))
        expected = [(1, None), (2,2), (None, 3)]
        self.assertEqual(expected, result)

    def test_left(self):
        i1 = [1, 2]
        i2 = [2, 3]
        result = list(join.generic_join(i1, i2, 'left'))
        expected = [(1, None), (2,2)]
        self.assertEqual(expected, result)

    def test_right(self):
        i1 = [1, 2]
        i2 = [2, 3]
        result = list(join.generic_join(i1, i2, 'right'))
        expected = [(2,2), (None, 3)]
        self.assertEqual(expected, result)

    def test_inner(self):
        i1 = [1, 2]
        i2 = [2, 3]
        result = list(join.generic_join(i1, i2, 'inner'))
        expected = [(2, 2)]
        self.assertEqual(expected, result)

    def test_outer_1_common(self):
        i1 = [1, 2]
        i2 = [2, 3]
        result = list(join.generic_join(i1, i2, 'outer'))
        expected = [(1, None), (2,2), (None, 3)]
        self.assertEqual(expected, result)

    def test_outer_no_intersection(self):
        i1 = [1, 3]
        i2 = [2, 4]
        result = list(join.generic_join(i1, i2, 'outer'))
        expected = [(1, None), (None, 2), (3, None), (None, 4)]
        self.assertEqual(expected, result)

    def test_outer_right_empty(self):
        i1 = [1, 3]
        i2 = []
        result = list(join.generic_join(i1, i2, 'outer'))
        expected = [(1, None), (3, None)]
        self.assertEqual(expected, result)

    def test_outer_left_empty(self):
        i1 = []
        i2 = [1]
        result = list(join.generic_join(i1, i2, 'outer'))
        expected = [(None, 1)]
        self.assertEqual(expected, result)

    def test_left_left_empty(self):
        i1 = []
        i2 = [1]
        result = list(join.generic_join(i1, i2, 'left'))
        expected = []
        self.assertEqual(expected, result)

    def test_left_right_is_empty(self):
        i1 = [1]
        i2 = []
        result = list(join.generic_join(i1, i2, 'left'))
        expected = [(1, None)]
        self.assertEqual(expected, result)


class GenericTest(unittest.TestCase):

    def configure(self, name, left, right, type, expected):
        self.name = name
        self.left = left
        self.right = right
        self.type = type
        self.expected = expected
        self._testMethodName = f'test-{name}'

    def testGeneric(self):
        result = list(join.generic_join(self.left, self.right, self.type))
        self.assertEqual(self.expected, result)

    def __getattr__(self, name):
        if name.startswith('test'):
            return self.testGeneric




def suite():
    from . import tests_definitions
    suite = unittest.TestSuite()
    for definition in tests_definitions.definitions:
        name = definition['name']
        left = definition['left']
        right = definition['right']
        expected = definition['expected']
        for type, result in expected.items():
            params = {
                'name': f'{name}-{type}',
                'left': left,
                'right': right,
                'type': type,
                'expected': result
            }
            test = GenericTest()
            test.configure(**params)
            suite.addTest(test)
    return suite

if __name__ == '__main__':
    import sys
    runner = unittest.TextTestRunner(stream=sys.stdout, failfast=False)
    runner.run(suite())

