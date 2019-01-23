# -*- coding: utf-8 -*-

s_test_passed = "\x1b[1m\x1b[92mPASSED\x1b[0m"
s_test_failed = "\x1b[1m\x1b[91mFAILED\x1b[0m"

class TestIO(object):
    """docstring for TestIO."""
    def __init__(self, parent, tc):
        super(TestIO, self).__init__()
        self.parent = parent
        self.tc     = tc

    def test(self):
        print("\x1b[1m" + " Testing IO ".center(80, "-") + "\x1b[0m")

        self.tc.test("read_fasta(filename)", self._test_file_read_fasta)
        self.tc.test("write_fasta(filename, data)", self._test_file_write_fasta)
        self.tc.test("read_fastq(filename)", self._test_file_read_fastq)
        self.tc.test("write_fastq(filename, data)", self._test_file_write_fastq)
        self.tc.test("fasta_to_fastq(data)", self._test_fasta_to_fastq)
        self.tc.test("fastq_to_fasta(data)", self._test_fastq_to_fasta)
        self.tc.test("file_fasta_to_fastq(fasta_in, fastq_out)", self._test_file_fasta_to_fastq)
        self.tc.test("file_fastq_to_fasta(fastq_in, fasta_out)", self._test_file_fastq_to_fasta)


    #===========================================================================

    def _test_file_read_fasta(self):
        dataset = []
        passed = False
        return passed

    def _test_file_write_fasta(self):
        passed = False
        return passed

    def _test_file_read_fastq(self):
        passed = False
        return passed

    def _test_file_write_fastq(self):
        passed = False
        return passed

    def _test_fasta_to_fastq(self):
        passed = False
        return passed

    def _test_fastq_to_fasta(self):
        passed = False
        return passed

    def _test_file_fasta_to_fastq(self):
        passed = False
        return passed

    def _test_file_fastq_to_fasta(self):
        passed = False
        return passed
