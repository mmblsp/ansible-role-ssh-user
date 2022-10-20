"""test role ssh_user"""
import os

import testinfra.utils.ansible_runner

TST_USER = 'hdfs'

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('cluster')


def test_sshd_running_and_enabled(host):
    """test sshd """
    ssh_server = host.service("sshd")
    assert ssh_server.is_running
    assert ssh_server.is_enabled


def test_user_create(host):
    """test user"""
    assert host.user(TST_USER).exists


def test_exists_file_authorized_keys(host):
    """test exists file"""
    assert host.file(f"/home/{TST_USER}/.ssh/authorized_keys").exists
