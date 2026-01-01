This is the test suite to Toolkit.

It is its own repository to avoid pulling in the test data into every project using Toolkit as a submodule.

Tests can be run against the version of Toolkit included in this repository, or against an external version, to allow working on Toolkit as part of another project.

It requires nihtest an Python to be installed.

To test against the included version:

```sh
cd run
nihtest --all
```

To test against an external version:
```sh
./bin/setup run-external path/to/external/Toolkit
cd run-external
nihtest --all
```
