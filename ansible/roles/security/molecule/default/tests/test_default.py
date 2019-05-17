import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("package", [
    "iptables",
    "iptables-persistent",
    "fail2ban",
    "unattended-upgrades",
    "apparmor",
])
def test_packages_installed(host, package):
    pkg = host.package(package)

    assert pkg.is_installed


def test_unattended_upgrades(host):
    file = host.file('/etc/apt/apt.conf.d/20auto-upgrades')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert 'APT::Periodic::Unattended-Upgrade "1";' in file.content_string

    file = host.file('/etc/apt/apt.conf.d/50unattended-upgrades')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_unattended_service(host):
    service = host.service('unattended-upgrades')

    assert service.is_enabled


@pytest.mark.parametrize("setting,value", [
    ("net.ipv4.ip_forward", "0"),
    ("net.ipv4.icmp_echo_ignore_broadcasts", "1"),
    ("net.ipv4.conf.all.rp_filter", "1"),
    ("net.ipv4.conf.default.rp_filter", "1"),
    ("net.ipv4.conf.lo.rp_filter", "1"),
    ("net.ipv4.conf.eth0.rp_filter", "1"),
    ("net.ipv6.conf.all.forwarding", "1"),
    ("net.ipv4.conf.all.log_martians", "1"),
    ("net.ipv4.conf.default.accept_source_route", "0"),
    ("net.ipv4.conf.default.accept_redirects", "0"),
    ("net.ipv4.conf.default.secure_redirects", "0"),
    ("net.ipv4.conf.all.send_redirects", "0"),
    ("net.ipv4.conf.default.send_redirects", "0"),
    ("net.ipv4.icmp_echo_ignore_broadcasts", "1"),
    ("net.ipv6.conf.all.accept_ra", "0"),
    ("net.ipv6.conf.default.accept_ra", "0"),
    ("net.ipv6.conf.default.router_solicitations", "0"),
    ("net.ipv6.conf.all.router_solicitations", "0"),
    ("net.ipv6.conf.default.max_addresses", "1"),
])
def test_sysctl(host, setting, value):
    command = host.command(f"sysctl {setting}")

    assert command.stdout == f"{setting} = {value}"


def test_securetty(host):
    file = host.file('/etc/securetty')

    assert file.exists
    assert file.owner == 'root'
    assert file.group == 'root'
