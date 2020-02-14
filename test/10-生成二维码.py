#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Feb 2019 09:31:23 PM CST

# File Name: 10-生成二维码.py
# Description:

"""
import sys
import qrcode 
from optparse import OptionParser
def make_qr(output,msg):
    qr = qrcode.QRCode(     
        version=1,     
        error_correction=qrcode.constants.ERROR_CORRECT_L,     
        box_size=10,     
        border=4, 
    ) 
    qr.add_data(msg) 
    qr.make(fit=True)  
    img = qr.make_image()
    img.save('{}.png'.format(output))
    print("make pic [{}.png] successful...".format(output))

def main(args):
    usage = '%prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-o", "--output",action="store", type="string",metavar="OUT_PUT",
        dest="output", help="the output image name"
    )
    parser.add_option(
        "-m", "--message", action="store", type="string",metavar="MESSAGE",
        dest="message", help="message to the code"
    )
    parser.add_option(
        "-f", "--message_file", action="store", type="string",metavar="MESSAGE_FILE",
        dest="message_file", help="the message file"
    )
    options, args = parser.parse_args()
    if len(args) != 0:
        print("Error: Arguments [{0}] can not be parsed.".format(args))
        exit(1)
    if options.output is None:
        print("Error: The OUT_PUT argument can not be None")
        exit(1)
    if options.message is not None and options.message_file is not None:
        print("Error: Arguments [-m] and [-f] conflict")
        exit(1)
    elif options.message is not None and options.message_file is None:
        make_qr(options.output,options.message)
    elif options.message is None and options.message_file is not None:
        with open(options.message_file,'r') as f:
            make_qr(options.output,f.read())
    else:
        print("Error: The Message argument can not be None")
        exit(1)

if __name__ == '__main__':
    main(sys.argv)