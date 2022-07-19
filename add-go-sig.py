#!/usr/bin/env python3

# Not mine: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/A4NEHUW52ELDHDMPQDCBSRJXHDPJK2QX/

# Original script: https://gist.github.com/decathorpe/9d128982cb00e2d345d9e397372538ec

# Add @go-sig group with "commit" access to one or multiple packages
# Script accepts package names as command line arguments (and strips ","
# characters from arguments, so copy-pasting comma-separated lists of package
# names from report emails is supported, as well).

import sys

import requests

TOKEN = "PASTE-YOUR-src.fedoraproject.org-TOKEN-with-Modify-an-existing-project-access-HERE"

def main():
    packages = [package.strip(",") for package in sys.argv[1:]]

    for package in packages:
        print(f" - adding @go-sig to {package} ...")

        url = f"https://src.fedoraproject.org/api/0/rpms/{package}/git/modifyacls"
        data = {
            "user_type": "group",
            "name": "go-sig",
            "acl": "commit",
        }
        headers = {
            "Authorization": f"token {TOKEN}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()

    return 0


if __name__ == "__main__":
    exit(main())

