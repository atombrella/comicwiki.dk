import json
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


def test_hosts_file(host):
    f = host.file('/var/www/html/LocalSettings.php')

    assert f.exists
    assert f.user == 'www-data'
    assert f.group == 'www-data'


@pytest.mark.parametrize("image", [
    "btn_oversigt_inner.png",
    "btn_oversigt.png",
    "discussionitem_icon.gif",
    "icon_cleanup.gif",
    "Icon_ddfr.gif",
    "icon_disambiguation.gif",
    "icon_disambiguation_micro.gif",
    "icon_disputed.gif",
    "Icon_inducks.gif",
    "icon_info.gif",
    "icon_merge.gif",
    "Icon_Nummer_9_MM.gif",
    "Icon_Planet_Pulp.gif",
    "icon_stub.gif",
    "logo.png",
])
def test_comicwiki_mw_image_skin(host, image):
    f = host.file(f'/var/www/html/images/{image}')

    assert f.exists
    assert f.user == 'www-data'
    assert f.group == 'www-data'


def test_composer_local_json(host):
    f = host.file("/var/www/html/composer.local.json")

    content = json.loads(f.content)

    assert content == """{
    "require": {
        "mediawiki/bootstrap-components": "^5.0.0",
        "mediawiki/bootstrap": "~4.5.0",
        "mediawiki/chameleon-skin": "~4.3.0"
    },
    "extra": {
        "merge-plugin": {
            "include": [
                "extensions/*/composer.json",
                "skins/*/composer.json"
            ]
        }
    }
}"""


# test the map and the other files comicwiki
