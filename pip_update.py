#!/usr/bin/env bash
#######################################################################
#Author: kellanfan
#Created Time : Tue 24 Oct 2017 03:00:14 PM CST
#File Name: pip_update.sh
#Description:
#######################################################################
import pip
from subprocess import call
 
for dist in pip.get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell=True)
