import re
import os
import sys

# Input version string
version_string = sys.argv[1]

# Define the regular expression pattern
pattern = r'^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'

# Use re.match to extract version parts
match = re.match(pattern, version_string)

if match:
    github_output_file = os.getenv('GITHUB_OUTPUT')
    if github_output_file:
        with open(github_output_file, 'a') as f:
            f.write(f"version={match.group('major')}.{match.group('minor')}.{match.group('patch')}\n")
            f.write(f"major={match.group('major')}\n")
            f.write(f"minor={match.group('minor')}\n")
            f.write(f"patch={match.group('patch')}\n")
            f.write(f"prerelease={match.group('prerelease') or ''}\n")
            f.write(f"buildmetadata={match.group('buildmetadata') or ''}\n")

    print("Major:", match.group('major'))
    print("Minor:", match.group('minor'))
    print("Patch:", match.group('patch'))
    print("Pre-release:", match.group('prerelease') or "")
    print("Build metadata:", match.group('buildmetadata') or "")
else:
    print("Invalid semantic version string format. See https://semver.org/ for complete specification.")
