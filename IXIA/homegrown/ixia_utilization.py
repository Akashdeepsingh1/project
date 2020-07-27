#!/tools/build/bin/python3
#
# DELL PROPRIETARY INFORMATION
#
# This software is confidential.  Dell Inc., or one of its
# subsidiaries, has supplied this software to you under the terms of
# a license agreement, nondisclosure agreement or both.  You may not
# copy, disclose, or use this software except in accordance with those
# terms.
#
# Copyright 2019 Dell Inc.  All Rights Reserved.
#
# DELL INC. MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. DELL SHALL
# NOT BE LIABLE FOR ANY DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
# USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.
#

import os, sys
import subprocess
import tsapiInstanceFactory
import argparse

from subprocess import STDOUT, check_output


def get_args():
    '''
    to manage user arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", dest="file", help="enter the input csv file...\n which defines connect_id's")
    parser.add_argument("-o","--ofile", dest="output", help="enter the output filename")

    return parser.parse_args()

def ts_instance(domain_name):
    return tsapiInstanceFactory.APIFactory().getInstance(domain=domain_name)

def IXIA(ip_addr, outfile, owner, connectid):
    outFlag = False
    os.environ["IXIA_VERSION"] = "6.90"
    owner = owner.replace(" ", "_")
    cmd = "./ixia_reader_set00.tcl {} {} {} {}".format(ip_addr, outfile, owner, connectid)
    print(cmd)
    try:
        output = check_output(cmd, stderr=STDOUT, timeout=30, shell=True)
        output = output.decode("utf-8")
        print("Output of IXIA : " + output)
        outFlag = True
    except:
        output = "Error: Some issue on execution...May be Timeout!"
        print("JC_Timeout")
        outFlag = False
    return output, outFlag

def filehandler(file, logger=None):
    if not os.path.isfile(file):
        print("error: inputfile not found...")
        sys.exit(0)
    else:
        return [line.rstrip('\n').strip() for line in open(file)]

def main(filename, outfile):
    forSummary = {}
    ll = filehandler(filename)[1:]
    ts = ts_instance('Global')
    print(ll, ts)
    for item in ll:
        if item.strip() == "JC":
            print("do nothis for JC header")
        else:
            qresult = ts.find_resources(item.strip(), "", "", True, True, False, "", "", 100, None)
            if len(qresult) != 1:
                print("quli more than one or no device found.. skipping for {} --> {} ".format(item, len(qresult)))
            else:
                dd = ts.get_resource_details(qresult[0].name)
                owner_name = dd.owner
                ip = dd.address
                print("======= ======= ======= ======= ======= ======= ======= =======")
                jlog = IXIA(ip.strip(), outfile, dd.owner, item.strip())[1]
                print(jlog)
                forSummary [item.strip()] = jlog
                if not jlog:
                    kk = "{},{},{},Couldn'tFetch,Couldn'tFetch,Couldn'tFetch,Couldn'tFetch,Couldn'tFetch,Couldn'tFetch,Couldn'tFetch,Couldn'tFetch\n".format(item.strip(), dd.owner, ip.strip())
                    FILE = open(outfile, "a+")
                    FILE.write(kk)
                    FILE.close()
                print("======= ======= ======= ======= ======= ======= ======= =======")
                print("")
                print("")

    #summary report
    print(forSummary)
    for key in forSummary:
        if not forSummary[key]:
            print(forSummary[key])

if __name__ == "__main__":
    args = get_args()
    sys.exit(main(args.file, args.output))
