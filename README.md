This is the test suite to Toolkit.

It is its own repository to avoid pulling in the test data into every project using Toolkit as a submodule.

Tests can be run against the version of Toolkit included in this repository, or against an external version, to allow working on Toolkit as part of another project.

It requires nihtest an Python to be installed.

To test zip file creation, it needs zipcmp from libzip to be installed.

To test against the included version:

```sh
mkdir run
cd run
../bin/setup
nihtest --all
```

To test against an external version:
```sh
mkdir run-external
cd run-external
../bin/setup run-external path/to/external/Toolkit
nihtest --all
```
