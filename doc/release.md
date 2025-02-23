How to make a release
=====================

- Sync local `master` and `develop` with Github
  - `for x in master develop; git checkout $x; git pull`
- On `develop` branch
  - Update `src/iminuit/version.py` to the release version
    - For a beta release, add `.betaN`, where N is a number >= 0
    - For a release candidate, add `.rcN`
  - Run `python3 doc/update_changelog.py` or update `doc/changelog.rst` manually
    - Check the output if you used the script
- Merge `develop` into `master`
  - Every push to `master` triggers building wheels, uploading to PyPI, and tagging/publishing on GitHub
  - If there are problems with the wheels, commit fixes to `develop`, then merge again into `master`
  - Note: Upload to PyPI uses API tokens configured in PyPI and Github "Secrets"

- conda-forge should pick up our release automatically and generate conda packages
