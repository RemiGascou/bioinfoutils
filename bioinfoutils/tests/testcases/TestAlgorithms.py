# -*- coding: utf-8 -*-

s_test_passed = "\x1b[1m\x1b[92mPASSED\x1b[0m"
s_test_failed = "\x1b[1m\x1b[91mFAILED\x1b[0m"

class TestAlgorithms(object):
    """docstring for TestAlgorithms."""
    def __init__(self, parent):
        super(TestAlgorithms, self).__init__()
        self.parent = parent

    def test(self):
        print("\x1b[1m" + " Testing Algorithms ".center(80, "-") + "\x1b[0m")
        print("\x1b[1m[\x1b[93mTEST\x1b[0m\x1b[1m]\x1b[0m GC_content(dna)... ", end="")
        o = self._test_GC_content()
        if o == True:
            print(s_test_passed)
        else :
            print(s_test_failed)

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
                print(" - Inner test :",s_test_failed, o)
                passed = False
        return passed
