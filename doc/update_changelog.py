from pathlib import PurePath as Path
import re
import subprocess as subp
from pkg_resources import parse_version
import datetime
import warnings

cwd = Path(__file__).parent

with open(cwd.parent / "src/iminuit/version.py") as f:
    version = {}
    exec(f.read(), version)
    new_version = parse_version(version["version"])

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    latest_tag = next(
        iter(
            sorted(
                (
                    parse_version(x)
                    for x in subp.check_output(["git", "tag"])
                    .decode()
                    .strip()
                    .split("\n")
                ),
                reverse=True,
            )
        )
    )

with open(cwd / "changelog.rst") as f:
    content = f.read()

# find latest entry
m = re.search(r"([0-9]+\.[0-9]+\.[0-9]+) \([^\)]+\)\n-*", content, re.MULTILINE)
previous_version = parse_version(m.group(1))
position = m.span(0)[0]

# sanity checks
assert new_version > previous_version, f"{new_version} > {previous_version}"

git_log = re.findall(
    r"[a-z0-9]+ ([^\n]+ \(#[0-9]+\))",
    subp.check_output(
        ["git", "log", "--oneline", f"v{previous_version}..HEAD"]
    ).decode(),
)

today = datetime.date.today()
header = f"{new_version} ({today.strftime('%B %d, %Y')})"

new_content = f"{header}\n{'-' * len(header)}\n"
if git_log:
    for x in git_log:
        new_content += f"- {x.capitalize()}\n"
else:
    new_content += "- Minor improvements\n"
new_content += "\n"

print(new_content, end="")

with open(cwd / "changelog.rst", "w") as f:
    f.write(f"{content[:position]}{new_content}{content[position:]}")
