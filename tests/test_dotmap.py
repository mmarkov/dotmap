import unittest
from mock import patch
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
        self.assertEqual(d.lol, 1)
        self.assertEqual(d['ba'], 2)

    def test_to_dict(self):
        d = DotMap(self._get_dict())
        o = d.to_dict()
        self.assertEqual(o['a'], 1)

    def test_values(self):
        d = DotMap(self._get_dict())
        v = d.values()
        self.assertEqual(len(v), 3)

    def test_view_values(self):
        d = DotMap(self._get_dict())
        dd = d.to_dict()
        for k, v in d.viewitems():
            self.assertTrue(set(dd).issuperset({k: v}))
        for k in d.viewkeys():
            self.assertTrue(k in dd)
        for v in d.viewvalues():
            self.assertTrue(v in dd.values())

    @patch('pprint.PrettyPrinter.pprint')
    def test_pprint(self, mock_pretty_printer):
        d = DotMap(self._get_dict())
        d.pprint()
        self.assertTrue(mock_pretty_printer.called)

    def test_repr(self):
        d = DotMap(self._get_dict())
        self.assertTrue(repr(d).startswith('DotMap('))
        d = DotMap(a='b')
        self.assertEqual("DotMap(a='b')", repr(d))

    def test_setdefault(self):
        d = DotMap()
        d.a = 'c'
        self.assertEqual('c', d.setdefault('a', 'd'))
        self.assertEqual('d', d.setdefault('b', 'd'))

    def test_iter(self):
        d = DotMap(self._get_dict())
        for k in d:
            if k == 'a':
                self.assertEqual(1, d[k])

    def test_clear(self):
        d = DotMap(self._get_dict())
        self.assertEqual(1, d.a)
        d.clear()
        self.assertEqual(0, len(d))
        self.assertEqual(d.a, DotMap())

    def test_popitem(self):
        m = DotMap()
        m.people.john.age = 32
        m.people.john.job = 'programmer'
        m.people.mary.age = 24
        m.people.mary.job = 'designer'
        m.people.dave.age = 55
        m.people.dave.job = 'manager'
        p = m.people.popitem()
        self.assertEqual(p[0], 'dave')
        i = m.popitem()
        self.assertEqual(i[0], 'people')
        self.assertEqual(0, len(m))

    def test_pop(self):
        d = DotMap(self._get_dict())
        v = d.pop('a', 4)
        self.assertEqual(1, v)
        v = d.pop('a', 4)
        self.assertEqual(4, v)

    def test_eq(self):
        d = DotMap(self._get_dict())
        m = DotMap()
        m.people.john.age = 32
        m.people.john.job = 'programmer'
        m.people.mary.age = 24
        m.people.mary.job = 'designer'
        m.people.dave.age = 55
        m.people.dave.job = 'manager'
        self.assertNotEqual(d, m)
        m.clear()
        m.a = 1
        m.b = 2
        m.subD.c = 3
        m.subD.d = 4
        self.assertEqual(d, m)

if __name__ == '__main__':
    unittest.main()
