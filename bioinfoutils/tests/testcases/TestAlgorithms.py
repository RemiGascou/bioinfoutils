# -*- coding: utf-8 -*-

class TestAlgorithms(object):
    """docstring for TestAlgorithms."""
    def __init__(self, parent, tc):
        super(TestAlgorithms, self).__init__()
        self.parent = parent
        self.tc     = tc

    def test(self):
        print("\x1b[1m" + " Testing Algorithms ".center(80, "-") + "\x1b[0m")

        self.tc.test("GC_content(dna)", self._test_GC_content)

    def _test_GC_content(self):
        passed = True
        dataset = [
            ["", 0.0],
            ["GCGCGCGCGCGC", 100.0],
            ["ATATATATATAT", 0.0],
            ["ACGATGATCGAT", 41.66666666666667],
            ["ATCGGCTAGGCTAGGATCG", 57.89473684210527]
        ]
        for d in dataset:
            o = self.parent.algorithms.GC_content(d[0])
            if o != d[1]:
                print(" - Inner test :",self.tc.s_test_failed, o)
                passed = False
        return passed
