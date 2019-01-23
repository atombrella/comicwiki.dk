import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_renewal_job_exists(host):
    job = host.file('/etc/cron.daily/cert-renew.sh')

    assert job.exists
    assert job.user == 'root'
    assert job.group == 'root'
    assert job.mode == 755


def test_certificate_requested(host):
    package = host.package('certbot')
    assert package.is_installed


def test_certbot_configuration(host):
    cli = host.file('/etc/letsencrypt/cli.ini')

    assert cli.exists
    assert cli.user == 'root'
    assert cli.group == 'root'
    assert cli.mode == 644

    assert cli.readlines().contains('max-log-backups = 50')
