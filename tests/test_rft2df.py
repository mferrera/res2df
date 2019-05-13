# -*- coding: utf-8 -*-
"""Test module for nnc2df"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import pytest

import pandas as pd

from ecl.eclfile import EclFile
from ecl.grid import EclGrid

from ecl2df import rft2df
from ecl2df.eclfiles import EclFiles

DATAFILE = "data/reek/eclipse/model/2_R001_REEK-0.DATA"


def test_rft2df():
    """Test that dataframes are produced"""
    eclfiles = EclFiles(DATAFILE)
    rftdf = rft2df.rft2df(eclfiles)

    assert not rftdf.empty
    assert len(rftdf.columns)


def test_main():
    """Test command line interface"""
    tmpcsvfile = ".TMP-rft.csv"
    sys.argv = ["rft2csv", DATAFILE, "-o", tmpcsvfile]
    rft2df.main()

    assert os.path.exists(tmpcsvfile)
    disk_df = pd.read_csv(tmpcsvfile)
    assert not disk_df.empty
    os.remove(tmpcsvfile)