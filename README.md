# Ansible project for managing Comicwiki.dk #

This repository contains code for managing [ComicWiki](https://comicwiki.dk/wiki/Forside)  The website
is meant as a hobby project, initially started by [Joen Asmussen](http://moc.co).  The molecule
tests were mainly meant for finding typos in the Ansible code, and it's on the to do
list to write more than the few auto-generated ones.

Ansible is used to provision and bootstrap the MediaWiki installation.  All of the
configuration is based on a previous installation.  Some parts are controlled by
Ansible, other parts were done manually afterwards, such as the import of the database
and running the upgrade script to deal with schema migrations for a newer MediaWiki version.

The [LESS stylesheet](http://lesscss.org/) was provided by [Joen Asmussen](http://moc.co)
Mediawiki is backed by the [Chameleon skin](https://www.mediawiki.org/wiki/Skin:Chameleon),
using [Bootstrap 3.3](https://getbootstrap.com/docs/3.3/) as the primary frontend framework.

The code is running on a DigitalOcean droplet, with everything running on the same node.
