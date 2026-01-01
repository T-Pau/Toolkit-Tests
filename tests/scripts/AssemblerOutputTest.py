#!/usr/bin/env python3

import os
import sys
import pathlib

_root_dir = pathlib.Path(__file__).resolve().parents[2]
_toolkit_dir = os.environ["TOOLKIT_DIR"] if "TOOLKIT_DIR" in os.environ else os.path.join(_root_dir, "Toolkit")
sys.path.append(os.path.join(_root_dir, "python-packages"))
sys.path.append(os.path.join(_toolkit_dir, "python-packages"))

import AssemblerOutput

def main():
    with open("test.s", "w") as f:
        assembler = AssemblerOutput.AssemblerOutput(f)

        assembler.header("test.txt")

        assembler.begin_object("object_1", section="test_section", visibility="public", alignment=0x100)
        assembler.label("start_object_1", visibility="private")
        assembler.byte(0x12)
        assembler.word(0x1234)
        assembler.bytes(bytes([0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0, 0x11, 0x22]))
        assembler.data(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        assembler.string("test", encoding="screen", nul_terminate=True)
        assembler.end_object()


main()