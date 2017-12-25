#!/usr/bin/env python3
"""
 Copyright (c) 2017, Syslog777

 All rights reserved.

 Redistribution and use in source and binary forms, with or without modification,
 are permitted provided that the following conditions are met:

     * Redistributions of source code must retain the above copyright notice,
       this list of conditions and the following disclaimer.
     * Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.
     * Neither the name of Desktop nor the names of its contributors
       may be used to endorse or promote products derived from this software
       without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import argparse
import errno
import sys

"""
The Psak class only needs the name of the module.
Therefore, the self.parser field will only have module
names as valid args within this class. Additional args
will be added to the parser object in whichever module is
loaded.
"""
usage = ("%(prog)s --module_name ")
description = "psak.py, the Pentester's Swiss Army Knife"
parser = argparse.ArgumentParser(description=description,
                                 usage=usage)
parser.add_argument('--mitm',
                    help=("Usage: --mitm runtime-in-seconds"
                          " [victim-ip] [gate-ip] "
                          "[optional-attack-type]"),
                    required=False, type=int)
parser.add_argument('--slowloris',
                    help="Usage: %(prog)s --slowloris ",
                    required=False, nargs="?")

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if sys.argv[1] == ('-h') or sys.argv[1] == ('--help'):
    parser.print_help()
    sys.exit(0)

def psak_normal_shutdown(self):
    print("[*] Exiting...")
    sys.exit(0)


def main():
    try:
        if sys.argv[1] == '--mitm':
            from modules.mitm_packages.mitm_core.mitm_args import MitmArgs
            from modules.mitm_packages.mitm_core.mitm import Mitm
            mitm_args = MitmArgs(parser)
            mitm = Mitm(mitm_args)
            mitm.connect(runtime=mitm_args.get_runtime())
        if sys.argv[1] == '--slowloris':
            from modules.slowloris_packages.slowloris_core.slowloris import SlowLoris
            slowloris = SlowLoris(parser)
            slowloris.poisen()
    except IOError as e:
        if e[0] == errno.EPERM:
            print(sys.stderr, ("\nYou need root permissions to do this,"
                               " exiting..."))
            sys.exit(1)


if __name__ == '__main__':
    main()