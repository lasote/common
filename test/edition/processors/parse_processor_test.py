from biicode.common.test.bii_test_case import BiiTestCase
from nose.core import run
from biicode.common.test import model_creator as mother
from biicode.common.edition.processors.parse_processor import ParseProcessor
from biicode.common.model.bii_type import CPP
from biicode.common.edition.processors.processor_changes import ProcessorChanges
from biicode.common.output_stream import OutputStream


class ParseProcessorTest(BiiTestCase):

    def test_has_main_and_dependency_declarations(self):
        processor = ParseProcessor()
        changes = ProcessorChanges()
        block_holder = mother.get_block_holder(['user/geom/main.cpp'], CPP)
        processor.do_process(block_holder, changes, OutputStream())
        main = block_holder['main.cpp'].cell
        self.assertTrue(main.hasMain, 'Main method not detected by parse processor')
        self.check_dependency_set(main.dependencies, unresolved=['iostream', 'sphere.h'])

        # now remove #include
        load = block_holder['main.cpp'].content.load
        load.replace('#include "sphere.h"', '')
        block_holder['main.cpp'].content.load = load

        processor.do_process(block_holder, changes, OutputStream())
        self.check_dependency_set(main.dependencies, unresolved=['iostream'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    run()
