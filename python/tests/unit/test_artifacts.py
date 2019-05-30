# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from semver import VersionInfo

from dazl.damlsdk.artifacts import load_artifacts, get_artifact_url, ArtifactLocation

ZERO_VERSION = VersionInfo(0, 0, 0)
DUMMY_ARTIFACT = ArtifactLocation('com.something', 'somewhere', ZERO_VERSION)
DUMMY_NATIVE_ARTIFACT = ArtifactLocation('com.something', 'somewhere', ZERO_VERSION, native=True)
DUMMY_TAR_GZ_ARTIFACT = ArtifactLocation('com.something', 'somewhere', ZERO_VERSION, 'tar.gz')
DUMMY_NATIVE_TAR_GZ_ARTIFACT = ArtifactLocation('com.something', 'somewhere', ZERO_VERSION, 'tar.gz', native=True)


class TestArtifacts(TestCase):

    def test_artifacts_yaml_can_parse(self):
        """
        Verify that the artifacts manifest is syntactically correct.
        """
        load_artifacts()

    def test_artifacts_yaml_are_valid(self):
        """
        Verify that all artifacts resolve to correct URLs.
        """
        repository = load_artifacts()
        for platform in ('osx', 'linux'):
            for name, artifact in repository.artifacts.items():
                url = get_artifact_url(repository.root_url, artifact, platform=platform)
                from urllib.request import urlopen, Request, HTTPError

                try:
                    with urlopen(Request(url, method='HEAD')) as response:
                        if response.status != 200:
                            print(f'{url}: {response.status}')
                except HTTPError as err:
                    print(f'{url}: {err.code}')

    def test_artifact_url_no_root_slash(self):
        expected = 'http://nowhere/repo/com/something/somewhere/0.0.0/somewhere-0.0.0.jar'
        actual = get_artifact_url('http://nowhere/repo', DUMMY_ARTIFACT)
        self.assertEqual(expected, actual)

    def test_artifact_url_root_slash(self):
        expected = 'http://nowhere/repo/com/something/somewhere/0.0.0/somewhere-0.0.0.jar'
        actual = get_artifact_url('http://nowhere/repo/', DUMMY_ARTIFACT)
        self.assertEqual(expected, actual)

    def test_artifact_url_native(self):
        expected = 'http://nowhere/repo/com/something/somewhere/0.0.0/somewhere-0.0.0-osx.jar'
        actual = get_artifact_url('http://nowhere/repo/', DUMMY_NATIVE_ARTIFACT, platform='osx')
        self.assertEqual(expected, actual)

    def test_artifact_url_packaging(self):
        expected = 'http://nowhere/repo/com/something/somewhere/0.0.0/somewhere-0.0.0.tar.gz'
        actual = get_artifact_url('http://nowhere/repo/', DUMMY_TAR_GZ_ARTIFACT)
        self.assertEqual(expected, actual)

    def test_artifact_url_packaging_native(self):
        expected = 'http://nowhere/repo/com/something/somewhere/0.0.0/somewhere-0.0.0-osx.tar.gz'
        actual = get_artifact_url('http://nowhere/repo/', DUMMY_NATIVE_TAR_GZ_ARTIFACT, platform='osx')
        self.assertEqual(expected, actual)
