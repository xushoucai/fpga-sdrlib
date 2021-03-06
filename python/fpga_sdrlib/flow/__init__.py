"""
Utility functions to help with generation and verification of
verilog message stream code.
"""

from fpga_sdrlib.generate import copyfile

blocks = {
    # The basic modules.
    'split.v': (None, copyfile, {}),
    # Test module.
    'dut_split.v': (None, copyfile, {}),
    # A qa_wrapper that returns the first output from the splitter.
    'qa_split.v': (None, copyfile, {}),
    # A buffer. Can read every second clock cycle.
    'buffer_AA.v': (None, copyfile, {}),
    # A buffer. Can read every clock cycle.
    'buffer_BB.v': (None, copyfile, {}),
    # A qa_wrapper for buffer_AA
    'qa_buffer_AA.v': (('buffer_AA.v',), copyfile, {}),
    # A qa_wrapper for buffer_AA that empties the buffer in bursts.
    'qa_buffer_AA_burst.v': (('buffer_AA.v',), copyfile, {}),
    # A qa_wrapper for buffer_AA
    'qa_buffer_BB.v': (('buffer_BB.v',), copyfile, {}),
    }

# compatible with running on the B100
compatibles = {
    'split_return_one':
        ('qa_split.v', 'split.v'),
    'buffer_AA':
        ('qa_buffer_AA.v', ),
    'buffer_AA_burst':
        ('qa_buffer_AA_burst.v', ),
    'buffer_BB':
        ('qa_buffer_BB.v', ),
}

# Not compatible with running on the B100
incompatibles = {
    'split':
        ('split.v', 'dut_split.v'),
}
