# `colors-core`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Core color functionality.*

## Installing

**Python 3.8 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install colors-core
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/colors-core.git
$ cd colors-core
$ python -m pip install .
```

### poetry

You can add `colors-core` as a dependency with the following command:

```console
$ poetry add colors-core
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
colors-core = "^1.1.0"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.colors-core]
git = "https://github.com/nekitdev/colors-core.git"
```

## Examples

```python
>>> from colors import Color
>>> color = Color(0x000000)
>>> print(color)
#000000
>>> color.to_rgb()
(0, 0, 0)
>>> color.to_rgba(0)
(0, 0, 0, 0)
>>> color.to_hsv()
(0.0, 0.0, 0.0)
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `colors-core` [here][Security].

## Contributing

If you are interested in contributing to `colors-core`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`colors-core` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/chat

[Actions]: https://github.com/nekitdev/colors-core/actions

[Changelog]: https://github.com/nekitdev/colors-core/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/colors-core/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/colors-core/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/colors-core/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/colors-core/blob/main/LICENSE

[Package]: https://pypi.org/project/colors-core
[Coverage]: https://codecov.io/gh/nekitdev/colors-core
[Documentation]: https://nekitdev.github.io/colors-core

[Discord Badge]: https://img.shields.io/discord/728012506899021874
[License Badge]: https://img.shields.io/pypi/l/colors-core
[Version Badge]: https://img.shields.io/pypi/v/colors-core
[Downloads Badge]: https://img.shields.io/pypi/dm/colors-core

[Documentation Badge]: https://github.com/nekitdev/colors-core/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/colors-core/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/colors-core/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/colors-core/branch/main/graph/badge.svg
