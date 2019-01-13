import os
import os.path

import pytest
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("package", [
    "apache2",
    "mod_pagespeed"
])
def test_package(host, package):
    pkg = host.package(package)

    assert pkg.is_installed


def test_service(host):
    service = host.service("apache2")

    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize("conf_file", [
    "/etc/apache2/sites-available/default-ssl.conf",
    "/etc/apache2/sites-available/000-default.conf"
])
def test_available_sites(host, conf_file):
    file = host.file(conf_file)

    assert file.exists
    assert file.owner == 'root'
    assert file.group == 'root'
    assert file.mode == '0644'


@pytest.mark.parametrize("conf_file", [
    "/etc/apache2/sites-enabled/default-ssl.conf",
    "/etc/apache2/sites-enabled/000-default.conf"
])
def test_enabled_sites(host, conf_file):
    file = host.file(conf_file)

    assert os.path.islink(file)
    assert file.owner == 'root'
    assert file.group == 'root'
    assert file.mode == '0644'
