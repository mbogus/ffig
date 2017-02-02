#!/usr/bin/env python
import sys
import os
import subprocess


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", help="run tests", action="store_true", dest="run_tests")
    parser.add_argument(
        "-v", help="verbose", action="store_true", dest="verbose")
    parser.add_argument(
        "-o",
        help="output dir (relative to source dir)",
        default="build",
        dest="out_dir")
    parser.add_argument(
        "-c",
        help="config (Debug or Release)",
        default="Debug",
        dest="config")
    args = parser.parse_args()

    src_dir = os.path.dirname(os.path.dirname(__file__))

    cmake_invocation = "cmake . -B{} -DCMAKE_BUILD_TYPE={}".format(args.out_dir, args.config)    
    if args.verbose:
        cmake_invocation = cmake_invocation + " -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON"

    subprocess.check_call(cmake_invocation.split(), cwd=src_dir)
    subprocess.check_call(
        "cmake --build ./{}".format(args.out_dir).split(), cwd=src_dir)

    if args.run_tests:
        rc = subprocess.call(
            "ctest . --output-on-failure -c {}".format(args.config).split(),
            cwd=os.path.join(src_dir, args.out_dir))
        if rc != 0:
            sys.exit(1)


if __name__ == "__main__":
    main()
