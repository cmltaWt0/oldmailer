#!/usr/bin/env python3

from oldmailer import passwd_change, shadow_change, mails_delete

from unittest import TestCase, TestLoader, TextTestRunner
import os
import subprocess


class PasswdChange_Test(TestCase):
    def setUp(self):
        """
        Preconditions
        """
        subprocess.call(['mkdir', 'test'])
        subprocess.call(['touch', 'test/test', 'test/max',
                         'test/root', 'test/mail', 'test/test_alive'])
        # Create passwd test file
        pt = open('passwd_test', 'w')
        pt.write('root:x:0:0:root:/dir:/shell\n')
        pt.write('max:x:1234:777:Account Max:/home/max:/bin/bash\n')
        pt.write('mail:x:8:12:mail:/var/spool/mail:/sbin/nologin\n')
        pt.write('test:x:9:12:test for deleting:/maildir:/shell\n')
        pt.write('test_alive:x:9:12:test NOT deleting:/maildir:/shell\n')
        pt.close()
        # Create shadow test file
        st = open('shadow_test', 'w')
        st.write('root:testhash:12345:6:7777:8:::\n')
        st.write('max:testhash:12345:6:7777:8:::\n')
        st.write('mail:testhash:12345:6:7777:8:::\n')
        st.write('test:testhash:12345:6:7777:8:::\n')
        st.write('test_alive:testhash:12345:6:7777:8:::\n')
        st.close()
        # Create keys.txt file
        kt = open('keys_test.txt', 'w')
        kt.write('test_alive\n')
        kt.write('mail\n')
        kt.write('missing_name\n')
        kt.close()

    def tearDown(self):
        try:
            if os.path.exists('test/test'):
                raise Exception('test/test must not exist')
            if not (os.path.exists('test/max') and
                    os.path.exists('test/root') and
                    os.path.exists('test/mail') and
                    os.path.exists('test/test_alive')):
                raise Exception('File test_alive, max, root, mail must exist!')
        except Exception:
            raise
        finally:
            subprocess.call(['rm', '-r', 'test/'])

    def test_passwd_change(self):
        """
        Testing according to test passwd, shadow and keys.txt file.
        Test to remove from test directory.
        """
        shadow_change(*passwd_change(keys_file='keys_test.txt',
                      passwd_orig='passwd_test', passwd_new='passwd_test_new',
                      passwd_log='passwd_test.log',
                      missing_log='missing_test.log'),
                      shadow_orig='shadow_test', shadow_new='shadow_test_new',
                      shadow_log='shadow_test.log')
        mails_delete(passwd_log='passwd_test.log', maildir_path='test',
                     deleted_log='deleted_test.log',
                     not_deleted_log='not_deleted_test.log')

    def test_passwd_change_2(self):
        """
        Testing according to test passwd, shadow and keys.txt file.
        Test to remove from test/ directory.
        """
        shadow_change(*passwd_change(keys_file='keys_test.txt',
                       passwd_orig='passwd_test', passwd_new='passwd_test_new',
                       passwd_log='passwd_test.log',
                       missing_log='missing_test.log'),
                       shadow_orig='shadow_test', shadow_new='shadow_test_new',
                       shadow_log='shadow_test.log')
        mails_delete(passwd_log='passwd_test.log', maildir_path='test/',
                     deleted_log='deleted_test.log',
                     not_deleted_log='not_deleted_test.log')


suite = TestLoader().loadTestsFromTestCase(PasswdChange_Test)
TextTestRunner(verbosity=2).run(suite)
