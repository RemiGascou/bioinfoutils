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
        self.tc.test("dna_to_protein(dna)", self._test_dna_to_protein)
        self.tc.test("protein_mass(prot)", self._test_protein_mass)

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

    def _test_dna_to_protein(self):
        passed = True
        dataset = [
            ['GAAGGGGUAAAGCUAGCAUACAUAGUUGAGUAUCAGCUAACACGCUGAAUCCAUGGUACUUCACAUGGCGUCCUCUGUUAGUUG', 'EGVKLAYIVEYQLTRStopIHGTSHGVLCStopL'],
            ['UCGGGCUUUCUACGAAGUCCGAACGAGCUGGCG', 'SGFLRSPNELA'],
            ['CCUGAAAGA', 'PER'],
            ['CACAGUUUAGAGUUAACUUUCCCCAAACAGAGCCAUUGAGUCCGUGGUCAAACGAUUUAACCGGUUUUCGCCUCGCUCAACAUAUAGCGUGCGGAAAGCAUAACGGGACAAGUAGUUAGGACGGCCCGA', 'HSLELTFPKQSHStopVRGQTIStopPVFASLNIStopRAESITGQVVRTAR'],
            ['ACGAUCUAGGUCGGAGAUCACUUGGCUCAGUCCUAACGCGACUCGGAC', 'TIStopVGDHLAQSStopRDSD'],
            ['GAAUUUGUUGAACAAUGGACCCAU', 'EFVEQWTH'],
            ['GUGGAAGAAGCAUGUUGGUUUUACGUC', 'VEEACWFYV'],
            ['GCAGGAACUGAUUCCGCAUAAUACGGACCCACCUGCUGGAAUGGCUCGCCUGGUUAUCGACCUCACCUGUCAGCUUGCGCGCCAUUCCGGCAACAACGCAUUUUAGUUGCGAAGCAAAAGAAAUAUUAACUACUGGUG', 'AGTDSAStopYGPTCWNGSPGYRPHLSACAPFRQQRILVAKQKKYStopLLV'],
            ['GCCAUUCGCAAAUUUGGUGAAAGUCCAGCCCCCUCCAUUGAGGUACACGCCCCUCGGCAAUCUUGGUGUAUUAGUGCUGAAGGAAACCGC', 'AIRKFGESPAPSIEVHAPRQSWCISAEGNR'],
            ['CAGACGACCUCCACAGCGUAAAAUGACUUUGUAACCGCUCCAACCCCUUGA', 'QTTSTAStopNDFVTAPTPStop'],
            ['UAGCUUUUUGAUGGCGCCUUCGAGCGUAACAGCUCUGGGUACCUCUACACAAGGCGCGGAUAAUACCUGUGUAUCACCCAGAGUGCUGUUUAUCUAACCGGCUUAGUGAUGACCGUGAGGCAUCUCACGUGAGCG', 'StopLFDGAFERNSSGYLYTRRGStopYLCITQSAVYLTGLVMTVRHLTStopA'],
            ['UAUUAGGCAACUUCGCAAACGUGUCUGGUUGAGUCCAUCAGUAGGAAAUCUCCUCUUACAAUGUACGUGGCUUCAGUGCUAGUAACAUACAGAGCUGAGUUCCUAGGGCUGCUGCGUAGGGUCGUU', 'YStopATSQTCLVESISRKSPLTMYVASVLVTYRAEFLGLLRRVV'],
            ['UCGAGAUAAAUUUGUCUGUGCGCAUGGUAUCGCUCAACAUAAAAGGCGAUUCUACCACGGCCUGACUGCCAAAGGUGGUUUGGC', 'SRStopICLCAWYRSTStopKAILPRPDCQRWFG'],
            ['UUUUGCAUAGUUGGGAAUGUCGAU', 'FCIVGNVD'],
            ['GCUAUCGGAGAAAAUAAUUCACGGGGCUGAAAU', 'AIGENNSRGStopN']
        ]
        for d in dataset:
            o = self.parent.algorithms.dna_to_protein(d[0])
            if o != d[1]:
                print(" - Inner test :",self.tc.s_test_failed, o)
                passed = False
        return passed

    def _test_protein_mass(self):
        passed = True
        dataset = [
            ['YG', 220.08479],
            ['VStopSNStopKVVCPQFARIALIEYCGAStopGLLKISAGVPTHFR', 3739.0217600000005],
            ['LRAGSStopStopGLRWPLLCKVPGStopYFRTRRRRQIRSSVRPRFSStopALIPTE', 4933.79424],
            ['CTSVTLRRHAGTTYSQIStopLRQRASVLEYFVYIVMDSM', 4176.107069999999],
            ['CRStopStopSLLTIRYSQELHCDAIFPRRHTVStopGStopVLRYARVLSWVPWHStopDTE', 5160.655489999999],
            ['StopKKINEYLST', 1076.5865999999999],
            ['PSTQVEERLPPSRFVRRNPLTPVR', 2812.5572200000006],
            ['FCSStopNANStopV', 735.30101], ['PAHSFLPAQHPHARMSLRLENIStopNPSTLEQTQSRPIRYARGWM', 4875.48263],
            ['MCQKLWLTLLHWEYEAPAL', 2326.16422], ['VVTVSLNSLLLLAHRS', 1703.0093599999998],
            ['GRLIYSANDMVNTIPQKQFTStopAVLNNRHStopMDGSStopMKALTPT', 4214.11869],
            ['FSRVEIGHLQLPPGDRWELALRI', 2683.4710100000007],
            ['ETGTSLPDSKSVFRYFSI', 2014.9999800000003],
            ['FMNSPDRLT', 1061.49641]
        ]
        for d in dataset:
            o = self.parent.algorithms.protein_mass(d[0])
            if o != d[1]:
                print(" - Inner test :",self.tc.s_test_failed, o)
                passed = False
        return passed
