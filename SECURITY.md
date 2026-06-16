# Security

## Reporting vulnerabilities

If you discover a security issue in this project, please report it privately by opening a security advisory on GitHub:

https://github.com/zhouquanhaiyan-stack/desktop-ai-job-runtime-contracts/security/advisories

Do not disclose the issue publicly until it has been addressed.

## Scope

This project does not handle real credentials, payment data, personal information, or server-side infrastructure. Security issues are most likely to involve:

- Unsafe deserialization (though we use only json.loads on trusted input)
- Path traversal in output directory handling
- Accidental inclusion of sensitive data in example files

## Response

We aim to acknowledge reports within 5 business days and issue a fix or mitigation within 30 days.
