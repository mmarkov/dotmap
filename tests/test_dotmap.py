import unittest
from dotmap import DotMap


class DotMapTestCase(unittest.TestCase):

    def _get_dict(self):
        return {
            'a': 1,
            'b': 2,
            'subD': {'c': 3, 'd': 4}
        }

    def test_init(self):
        d = DotMap(self._get_dict())
        self.assertEqual(len(d), 3)
        self.assertEqual(d.a, 1)
        self.assertEqual(d.subD.c, 3)

    def test_init_kwargs(self):
        d = DotMap(self._get_dict(), test1=5, test2=6)
        self.assertEqual(d.test1, 5)
        self.assertEqual(d.test2, 6)
        dm = DotMap(name='Steve', job='programmer')
        self.assertEqual(dm.name, 'Steve')
        self.assertEqual(dm['job'], 'programmer')

    def test_copy(self):
        d = DotMap(self._get_dict())
        c = d.copy()
        self.assertEqual(d, c)

    def test_del(self):
        am = DotMap()
        am.some.deep.path.cuz.we = 'can'
        del am.some.deep
        self.assertEqual(len(am), 1)

    def test_fromkeys(self):
        d = DotMap.fromkeys(['a', 'b', 'c'], 'd')
        self.assertEqual(d.a, 'd')
        self.assertEqual(d.c, 'd')

    def test_get(self):
        d = DotMap(self._get_dict())
        self.assertEqual(d.get('a'), 1)
        self.assertEqual(d.get('f', 33), 33)
        self.assertEqual(d.get('f'), None)

    def test_has_key(self):
        d = DotMap(self._get_dict())
        self.assertTrue(d.has_key('a'))
        self.assertTrue('a' in d)
        self.assertFalse(d.has_key('f'))
        self.assertFalse('f' in d)

    def test_update(self):
        d = DotMap(self._get_dict())
        d.update([('rat', 5), ('bum', 4)], dog=7, cat=9)
        self.assertEqual(d.rat, 5)
        self.assertEqual(d['bum'], 4)
        self.assertEqual(d.dog, 7)
        self.assertEqual(d['cat'], 9)
        d.update({'lol': 1, 'ba': 2})
        self.assertEqual(d.rat, 5)
        self.assertEqual(d['bum'], 4)
        self.assertEqual(d.dog, 7)
        self.assertEqual(d['cat'], 9)

    def test_to_dict(self):
        d = DotMap(self._get_dict())
        o = d.to_dict()
        self.assertEqual(o['a'], 1)

    def test_values(self):
        d = DotMap(self._get_dict())
        v = d.values()
        self.assertEqual(len(v), 3)

if __name__ == '__main__':
    unittest.main()
