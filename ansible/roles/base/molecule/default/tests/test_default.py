import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_hostname(host):
    command = host.run('hostname')

    assert 'comicwiki.dk' in command.stdout


def test_group(host):
    group = host.group('wheel')

    assert group.exists


@pytest.mark.parametrize("user", [
    "mads",
    "joen",
])
def test_users(host, user):
    user = host.user(user)

    assert user.exists
    assert 'wheel' in user.groups
    # password-less login
    assert user.password == '!'


def test_wheel_sudo(host):
    sudoers = host.file('/etc/sudoers')

    assert b'%wheel ALL=(ALL) NOPASSWD: ALL' in sudoers.content


def test_ntp_activated(host):
    file = host.file('/etc/cron.hourly/ntpdate.sh')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o0755
    assert b'ntpdate -s europe.pool.ntp.org' in file.content


@pytest.mark.parametrize("package", [
    "ca-certificates",
    "git",
    "python",
    "openssl",
    "zip",
    "imagemagick",
    "openssh-server",
    "rsync",
    "ntpdate",
    "cron",
])
def test_installed_packages(host, package):
    pkg = host.package(package)

    assert pkg.is_installed


def test_domain_name_sysctl(host):
    command = host.run('sysctl kernel.domainname')

    assert 'kernel.domainname = comicwiki.dk' == command.stdout
