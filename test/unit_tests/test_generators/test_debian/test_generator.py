import os

from ....utils.common import redirected_stdio

from bloom.generators.debian.generator import get_changelogs

from catkin_pkg.packages import find_packages

test_data_dir = os.path.join(os.path.dirname(__file__), 'test_generator_data')


def test_get_changelogs():
    with redirected_stdio():
        packages = dict([(pkg.name, pkg) for path, pkg in find_packages(test_data_dir).iteritems()])
        assert 'bad_changelog_pkg' in packages
        get_changelogs(packages['bad_changelog_pkg'])
