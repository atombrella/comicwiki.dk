# Ansible project for managing Comicwiki.dk #

This repository contains code for managing [ComicWiki](https://comicwiki.dk/wiki/Forside)  The website
is meant as a hobby project, initially started by [Joen Asmussen](http://moc.co).  The molecule
tests were mainly meant for finding typos in the Ansible code, and it's on the to do
list to write more than the few auto-generated ones.

Ansible is used to provision and bootstrap the MediaWiki installation.  All of the
configuration is based on a previous installation.  Some parts are controlled by
Ansible, other parts were done manually afterwards, such as the import of the database
and running the upgrade script to deal with schema migrations for a newer MediaWiki version.

The [SASS stylesheet](https://sass-lang.com/) was provided by [Joen Asmussen](http://moc.co)
Mediawiki is backed by the [Chameleon skin](https://www.mediawiki.org/wiki/Skin:Chameleon),
using [Bootstrap 4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) as the
primary frontend framework.

The code is running on a [DigitalOcean](https://www.digitalocean.com) droplet, with everything
running on the same node.

## Notes on local development

It is possible to get the project running locally if you have a dump of the database, and the
following installed:

* Linux or WSL2. Debian or Ubuntu should be good.
* Docker and docker-compose. Under WSL2, Docker Desktop is probably the easiest to deal with.

You will probably need to edit the `LocalSettngs.php` so it reflects the database connection,
and holds a value for the `$wgSecretKey` and `$wgUpgradeKey` variables.

For the database, you can create a folder `db` where you can place the dump file.

## The tests

Because the tests for the infrastructure take a bit of time to run, they are left out of the
Github workflow.  Instead, you can run the tests for a single role, which may have dependencies
to some of the other roles in this repository.

Note that since there are some Ansible vault secrets needed for sensitive data, you either need to
add this vault password to a file, which **must** never be committed to this repository, or add
an environment variable with the content.

```
export ANSIBLE_VAULT_PASSWORD="...."
# or
export ANSIBLE_VAULT_PASSWORD_FILE=${HOME}/comicwiki-vault.pw
```

You can run the tests for a role with:

```bash
molecule test
```

This will create the required container, run the Ansible tasks against it, and lastly run the
[testinfra](https://testinfra.readthedocs.io/)

## Running the Ansible configuration

You need to create a virtual environment and then install the `requirements.txt`:

```bash
pip install -r requirements.txt
```

The playbooks use some community modules that require installation of those Ansible dependencies.

```bash
ansible-galaxy collection install -r requirements.yml -p ./
```

Synchronizing or running the playbook against a server is performed with:

```bash
ansible-playbook
```
