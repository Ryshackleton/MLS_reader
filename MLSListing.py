#!/usr/bin/env python3

__author__ = 'ryshackleton'

import sys


class MLSListing():
    """Models a listing on the MLS with associated data members"""

    def __init__(self, line ):
        """
        Initializes an MLS listing from a text line

        :param line: line from text file representing the listing, parsed here with RegEx
        """
        try:
            self._traceId = int(traceId)
            self._vlist2 = []
        except (ValueError,TypeError) as e:
            print("Conversion error: {}" \
                  .format(str(e)),file=sys.stderr)

