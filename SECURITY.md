# Security policy

## Supported versions

Security fixes are made on `main` and released in the next version. Please
check that a problem still exists in the latest release before reporting it.

## Reporting a vulnerability

Please report vulnerabilities privately rather than in a public issue: open the
repository's **Security** tab and choose **Report a vulnerability**
(<https://github.com/tonyjurg/Doc4CF/security/advisories/new>).

Include the Doc4CF version, how you ran it, and the smallest input that shows
the problem.

## Scope notes

- API keys are read from environment variables (`OPENROUTER_API_KEY`,
  `ANTHROPIC_API_KEY`, and the other provider variables listed in the README)
  and are never written to generated sites or caches. Do not commit them.
- With `--model`, corpus feature profiles are sent to the selected provider.
  See "Data handling" in the README.
- Generated sites are static files. Model output and corpus values are
  HTML-escaped before they are written.
