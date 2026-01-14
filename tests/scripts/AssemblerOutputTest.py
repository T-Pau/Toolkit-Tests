#!/usr/bin/env python3

import os
import sys
import pathlib

_root_dir = pathlib.Path(__file__).resolve().parents[2]
_toolkit_dir = os.environ["TOOLKIT_DIRECTORY"] if "TOOLKIT_DIRECTORY" in os.environ else os.path.join(_root_dir, "Toolkit")
sys.path.append(os.path.join(_root_dir, "python-packages"))
sys.path.append(os.path.join(_toolkit_dir, "python-packages"))

import AssemblerOutput
import Test

class AssemblerOutputTest(Test.Test):
    def execute_sub(self):
        with open("test.s", "w") as f:
            assembler = AssemblerOutput.AssemblerOutput(f)

            assembler.header("test.txt")

            self.raises("duplicate header", 
                lambda: assembler.header("another.txt"), 
                RuntimeError, "duplicate header")

            self.raises("object outside section", 
                lambda: assembler.begin_object("outside_section"), 
                RuntimeError, "object outside of section not allowed")

            def create_object():
                assembler.begin_object("object_1", section="test_section", visibility="public", alignment=0x100)
                assembler.label("start_object_1", visibility="private")
                assembler.byte(0x12)
                assembler.word(0x1234)
                assembler.bytes(bytes([0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0, 0x11, 0x22]))
                assembler.data(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
                assembler.string("test", encoding="screen", nul_terminate=True)
                assembler.end_object()
            self.ok("create object", create_object)

            self.raises("end object outside object", 
                lambda: assembler.end_object(), 
                RuntimeError, "can't end object outside an object")
            self.raises("label outside object", 
                lambda: assembler.label("outside_object"), 
                RuntimeError, "can't add label outside an object")
            self.raises("byte outside object", 
                lambda: assembler.byte(0x00), 
                RuntimeError, "can't add data outside an object")
            
            assembler.begin_object("object_2")
            self.raises("begin object inside object", 
                lambda: assembler.begin_object("inside_object"), 
                RuntimeError, "nested objects are not allowed")
            assembler.end_object()


AssemblerOutputTest().run()