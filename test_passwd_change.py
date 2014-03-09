#!/usr/bin/env python3

from passwd_change import passwd_change, shadow_change, mails_delete

from unittest import TestCase, TestLoader, TextTestRunner
import os


#TODO add command line argument for locating mail directory
#('/var/spool/mail/' or different)


class PasswdChange_Test(TestCase):
    def setUp(self):
        """
        Preconditions
        """
        #TODO create passwd test file
        #TODO create shadow test file
        #TODO create keys.txt file 

    def passwd_change_test(self):
    	shadow_change(*passwd_change)
    	mails_delete


suite = TestLoader().loadTestsFromTestCase(PasswdChange_Test)
TextTestRunner(verbosity=2).run(suite)