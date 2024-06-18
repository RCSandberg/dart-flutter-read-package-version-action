# Action to read package version from pubspec.yaml

Finds the row containing `version:` and extract the version that comes thereafter.

## Usage

```
name: Example action
on: [push]
jobs:
  example-job:
    name: Example
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      # With path set implicitly to default value
      - uses: RCSandberg/dart-read-package-semantic-version-action@v1.0.0
        id: call-action-1
      - run: echo "Read semantic version ${{ steps.call-action-1.outputs.semantic-version }}"
      - run: echo "Read version ${{ steps.call-action-1.outputs.version }}"
      - run: echo "Read major version ${{ steps.call-action-1.outputs.major }}"
      - run: echo "Read minor version ${{ steps.call-action-1.outputs.minor }}"
      - run: echo "Read patch version ${{ steps.call-action-1.outputs.patch }}"
      - run: echo "Read pre-release version ${{ steps.call-action-1.outputs.prerelease }}"
      - run: echo "Read build metadata ${{ steps.call-action-1.outputs.buildmetadata }}"


      # With path set explicitly
      - uses: RCSandberg/dart-read-package-semantic-version-action@v1.0.0
        id: call-action-2
        with:
          path: path/to/pubspec.yaml
      - run: echo "Read semantic version ${{ steps.call-action-2.outputs.semantic-version }}"
      - run: echo "Read version ${{ steps.call-action-2.outputs.version }}"
      - run: echo "Read major version ${{ steps.call-action-2.outputs.major }}"
      - run: echo "Read minor version ${{ steps.call-action-2.outputs.minor }}"
      - run: echo "Read patch version ${{ steps.call-action-2.outputs.patch }}"
      - run: echo "Read pre-release version ${{ steps.call-action-2.outputs.prerelease }}"
      - run: echo "Read build metadata ${{ steps.call-action-2.outputs.buildmetadata }}"
```

## Output Example

Having the line `version: 1.2.3+4` will produce the output:

| Output  | Value |
| ------------- | ------------- |
| semantic-version  | 1.2.3+4  |
| version  | 1.2.3  |
| major  | 1  |
| minor  | 2  |
| patch  | 3  |
| prerelease  | |
| buildmetadata  | 4  |


Having the line `version: 1.2.3-alpha-beta-321+build.42` will produce the output:

| Output  | Value |
| ------------- | ------------- |
| semantic-version  | 1.2.3-alpha-beta-321+build.42  |
| version  | 1.2.3  |
| major  | 1  |
| minor  | 2  |
| patch  | 3  |
| prerelease  | alpha-beta-321  |
| build-version  | build.42  |


## Input
**`path`** - Sets the path to the pubspec.yaml file relative to workspace directory.\
**Optional**&nbsp;&nbsp; Defaults to `./pubspec.yaml`