<!-- 
Copyright (c) Legal Entities in the BISL Group 
SPDX-License-Identifier: LicenseRef-BISL-1.0
-->

# Project Name  <!-- omit in toc -->

[![License: BISL 1.0][license-badge]][license-docs]

> Add a brief description about the contents of this repository here.
> Consider linking to existing documentation.

## Table of Contents  <!-- omit in toc -->

- [Getting Started](#getting-started)
- [Building and Testing](#building-and-testing)
- [Contribution Guidelines](#contribution-guidelines)
- [Feedback](#feedback)
- [About](#about)
	- [Maintainers](#maintainers)
	- [Contributors](#contributors)
	- [3rd Party Licenses](#3rd-party-licenses)
	- [Used Encryption](#used-encryption)
	- [License](#license)

## Getting Started

> This section should contain information on how to use the content of this
> repository. If it contains SW, consider explaining how it is installed, run or integrated.

## Building and Testing

> If the repository contains SW, add instructions on how to build it from source
> and test it in this section.

## Contribution Guidelines

> Use this section to describe or link to documentation which explaining how users can make contributions to the contents of this repository. Consider adopting the [InnerSource way of solicitating and handing contributions][contributing-code].

Please read [our contribution guidelines][contribution].

## Feedback

> Consider using this section to describe how you would like other developers
> to get in contact with you or provide feedback.

## About

### Maintainers

> List the maintainers of this repository here. Consider linking to their Bosch
> Connect profile pages. Mention or link to their email as a minimum.

### Contributors

> Consider listing contributors in this section to give explicit credit. You
> could also ask contributors to add themselves in this file on their own.

### 3rd Party Licenses

> Declare all 3rd party software that is distributed with this repository along
> with their licenses. It is recommended to [use an SBoM][how-to-sbom]. If you
> do, please retain the following statement and add the SBoM file
> `sbom.spdx.json` or `sbom.cyclonedx.json` in the main directory:

Dependencies to 3rd party software are declared in the [SBoM](sbom.spdx.json).

> Alternatively, provide a list in the readme using a table like the following.

> | URL | Version | License |
> |----------|---------|-------------|
> |[Cobra](https://github.com/spf13/cobra) | 1.9.2 | [Apache 2.0 License](vendor/cobra/license.txt) |
>
> License texts of distributed dependencies should be stored in the `vendor`
> subdirectory.

### Used Encryption

> If the code in this repository **does not** contain or use encryption (other than TLS), please retain the following statement:

This repository does not contain or use encryption algorithms.

> If the code in this repository **does** contain or use encryption (other than TLS), please add the following statement to this readme:

The software in this repository uses non-custom, strong encryption (&lt;name of algorithm&gt;).
See [legal/&lt;name-of-algorithm&gt;-encryption.md] for more details.

> And provide the file `legal/<name-of-algorithm>-encryption.md` with details ([learn more][declaration-of-encrytion])

### License

[![License: BISL 1.0][license-badge]][license-docs]

We ❤️ to share this repository as [InnerSource][innersource-docs].

[license-docs]: https://docs.innersource.bosch.com/bisl-1/
[license-badge]: https://img.shields.io/badge/License-BISL--1.0-informational
[contribution]: CONTRIBUTING.md
[declaration-of-encrytion]: https://docs.innersource.bosch.com/developers-corner/start-new-project/add-innersource-metadata/#documenting-used-encryption
[contributing-code]: https://docs.innersource.bosch.com/developers-corner/run-project/ 
[how-to-sbom]: https://docs.innersource.bosch.com/developers-corner/start-new-project/how-to-sbom/
[innersource-docs]: https://docs.innersource.bosch.com/
