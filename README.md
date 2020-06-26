# telegram_me

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](./LICENSE) [![Developer: @hearot](https://img.shields.io/badge/Developer-@hearot-blue.svg)](https://t.me/hearot)

A simple scraper for getting information from https://t.me links.

### Example

```python
from telegram_me import Link

link = Link.from_username("Wikisource_Bot")

print(link.bio)  # Output: A @wiki version for wikisource.org. [...]
print(link.image)  # Output: https://cdn4.telesco.pe/file/...
print(link.name)  # Output: Wikisource Search
print(link.username)  # Output: Wikisource_bot
```

### Installation

You can install this package by simply using `pip`:

    pip install telegram_me

### Changelog

> See [CHANGELOG.md](./CHANGELOG.md).
> Find new features in [FEATURES.md](./FEATURES.md).

### Commit messages

> See [Conventional Commits](https://www.conventionalcommits.org).

### Versioning

> See [PEP 440](https://www.python.org/dev/peps/pep-0440/).

### Copyright & License

- Copyright (C) 2020 [Hearot](https://github.com/hearot).
- Licensed under the terms of the [MIT License](./LICENSE).
