import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_local_settings(host):
    f = host.file('/var/vww/html/LocalSettings.php')

    assert f.exists
    assert f.user == 'www'
    assert f.group == 'www'
    assert f.mode == 0x400
