"""
Local vulnerability database and detection functions.
"""

VULNERABILITY_DB = {
    "apache": {
        "2.4.41": {
            "risk": "Medium",
            "cve": "Multiple Known CVEs",
            "issue": "Outdated Apache HTTP Server.",
            "recommendation": "Upgrade to Apache 2.4.58 or later."
        },
        "2.4.49": {
            "risk": "Critical",
            "cve": "CVE-2021-41773",
            "issue": "Path traversal and remote code execution vulnerability.",
            "recommendation": "Upgrade immediately."
        }
    },

    "openssh": {
        "8.2": {
            "risk": "Low",
            "cve": "Multiple Known CVEs",
            "issue": "Older OpenSSH version detected.",
            "recommendation": "Upgrade to a supported release."
        }
    },

    "vsftpd": {
        "2.3.4": {
            "risk": "Critical",
            "cve": "CVE-2011-2523",
            "issue": "Backdoored vsFTPd release.",
            "recommendation": "Upgrade immediately."
        }
    },

    "nginx": {
        "1.18.0": {
            "risk": "Medium",
            "cve": "Multiple Known CVEs",
            "issue": "Older Nginx release detected.",
            "recommendation": "Upgrade to the latest stable version."
        }
    }
}


def check_vulnerability(banner):
    """
    Checks the banner against the local vulnerability database.
    """

    if not banner:
        return None

    banner = banner.lower()

    for software, versions in VULNERABILITY_DB.items():

        if software in banner:

            for version, details in versions.items():

                if version in banner:
                    return details

    return None

if __name__ == "__main__":

    test_banner = "Server: Apache/2.4.49"

    print(check_vulnerability(test_banner))