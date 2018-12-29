import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_renewal_job_exists(host):
    job = host.file('/etc/cron.daily/cert-renew.sh')

    assert job.exists
    assert job.user == 'root'
    assert job.group == 'root'
    assert job.mode == '0755'


def test_certbot_installed(host):
    package = host.package('certbot')
    assert package.is_installed


def test_certbot_configuration(host):
    configuration = host.file('/etc/letsencrypt/renewal/www.comicwiki.dk.conf')

    assert configuration.exists
    assert configuration.user == 'root'
    assert configuration.group == 'root'
    assert configuration.mode == '0644'

    assert configuration.readlines().contains('')


def test_certbot_configuration(host):
    cli = host.file('/etc/letsencrypt/cli.ini')

    assert cli.exists
    assert cli.user == 'root'
    assert cli.group == 'root'
    assert cli.mode == '0644'

    assert cli.readlines().contains('max-log-backups = 50')
