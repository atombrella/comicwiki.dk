import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mysql_server_installed(host):
    package = host.package('mysql-server')

    assert package.is_installed


def test_mysql_client_installed(host):
    package = host.package('mysql-client')

    assert package.is_installed


def test_service_enabled(host):
    service = host.server('mysql')

    assert service.is_enabled
    assert service.is_running


def test_configuration(host):
    service = host.server('mysql')

    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize(["file", "mode"], [
    ["/var/lib/mysql/server-cert.pem", 0x0644],
    ["/var/lib/mysql/private-key.pem", 0x0600],
])
def test_certificate(host, file, mode):
    f = host.file(file)

    assert f.exists
    assert f.owner == 'mysql'
    assert f.group == 'mysql'
    assert f.mode == mode
