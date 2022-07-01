iminuit logo
============

The iminuit logo uses glyphs generated from the free Gentium Plus font.

How to make a release
=====================

- On develop
  - Check that `src/iminuit/version.py` has the right version
  - Update `doc/changelog.rst` to released version and add today's date
  - Note: A prerelease can be published simply by adding `.rcN` to `version`,
    where N is a number >= 0
- Merge develop into master, this triggers job to build wheels and upload to PyPI
  - If there are problems with the wheels, commit fixes to a branch,
    squash-merge to develop and then again develop to master
  - Note: Upload uses API tokens configured in PyPI and Github "Secrets"
- Create release on Github
  - tag: vX.Y.Z (matching `src/iminuit/version.py`)
  - title: vX.Y.Z
  - Message: [Link to changelog](https://iminuit.readthedocs.io/en/stable/changelog.html)
  - Note: conda-forge should pick this up automatically and generate conda packages
- Update `src/iminuit/version.py` beyond released version
