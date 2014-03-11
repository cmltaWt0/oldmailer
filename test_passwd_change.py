#!/usr/bin/env python3

from passwd_change import passwd_change, shadow_change, mails_delete

from unittest import TestCase, TestLoader, TextTestRunner
import os
import subprocess


class PasswdChange_Test(TestCase):
    def setUp(self):
        """
        Preconditions
        """
        subprocess.call(['mkdir', 'test'])
        subprocess.call(['touch', 'test/rvv', 'test/max',
                         'test/bdv', 'test/mail'])
        #TODO create passwd test file
        #TODO create shadow test file
        #TODO create keys.txt file

    def tearDown(self):
        if os.path.exists('test/rvv'):
            raise Exception('test/rvv must not exist')
        if not (os.path.exists('test/max') and
                os.path.exists('test/bdv') and
                os.path.exists('test/mail')):
            raise Exception('File max, bdv or mail must exist!')
        subprocess.call(['rm', '-r', 'test/'])

    def test_passwd_change(self):
        shadow_change(*passwd_change())
        mails_delete(maildir_path='test')
        if os.path.exists('test/rvv'):
            raise Exception('test/rvv must not exist')
        if not (os.path.exists('test/max') and
                os.path.exists('test/bdv') and
                os.path.exists('test/mail')):
            raise Exception('File max, bdv or mail must exist!')

    def test_passwd_change_2(self):
        shadow_change(*passwd_change())
        mails_delete(maildir_path='test/')


suite = TestLoader().loadTestsFromTestCase(PasswdChange_Test)
TextTestRunner(verbosity=2).run(suite)
