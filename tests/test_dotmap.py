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

    def test_init_kwargs(self):
        d = DotMap(self._get_dict(), test1=5, test2=6)
        self.assertEqual(d.test1, 5)
        self.assertEqual(d.test2, 6)

    def test_copy(self):
        d = DotMap(self._get_dict())
        c = d.copy()
        self.assertEqual(d,c)

    def test_del(self):
        am = DotMap()
        am.some.deep.path.cuz.we = 'can'
        del am.some.deep
        self.assertEqual(len(am), 1)

    def test_fromkeys(self):
        d = DotMap.fromkeys(['a','b','c'], 'd')
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


if __name__ == '__main__':
    unittest.main()

a = """	


    dd.update([('rat',5),('bum',4)], dog=7,cat=9)
    dd.update({'lol':1,'ba':2})
    print(dd)
    print
    for k in dd:
        print(k)
    print('a' in dd)
    print('c' in dd)
    dd.c.a = 1
    print(dd.toDict())
    dd.pprint()
    print
    print(dd.values())
    dm = DotMap(name='Steve', job='programmer')
    print(dm)
    print(issubclass(dm.__class__, dict))

"""