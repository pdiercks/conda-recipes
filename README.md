# conda-recipes
A collection of conda recipes to build conda packages.
The recipes are automatically generated using [doit](https://pydoit.org/) and [grayskull](https://conda-forge.org/blog/posts/2020-03-05-grayskull/).
For now, only recipes for packages available on pypi are generated.
Simply add a package and its version to `dodo.py` and run `doit`.

## Using grayskull to generate a recipe

If the package is available on `pypi`, [grayskull](https://conda-forge.org/blog/posts/2020-03-05-grayskull/) can be used to generate the recipe.
Install:
```
conda install --channel conda-forge grayskull
```
Generate the recipe:
```
grayskull pypi <package-name>==<version>
```

## How to build a conda package

From the [Conda-Build Documentation](https://docs.conda.io/projects/conda-build/en/latest/index.html):
> Building a conda package requires installing conda-build and creating a conda recipe. You then use the conda build command to build the conda package from the conda recipe.

The information presented here is only a short summary to get started quickly. If in doubt
I suggest reading the documentation.

### Install conda build
```
conda install conda-build
```

### Build the package
```
conda-build path/to/build/directory
```
The build directory is a flat directory which at least contains the recipe `meta.yml`.
If the package depends on some package available from some channel (most likely `conda-forge`),
make sure to add it to your channel list before executing the build command. 
The following command adds the channel 'conda-forge' to the top of the channel list, making it the highest priority:
```
conda config --add channels conda-forge
```
(This will create a file `~/.condarc` with your channel list sorted by priority.)
At some point conda also complains that `conda-verify` should be installed:
```
conda install conda-verify
```

## Uploading the package

The client is needed for uploading packages to your own channel.
If you do not have an account yet, create one on [Anaconda Cloud](https://anaconda.org).

Install the client:
```
conda install anaconda-client
```
You can login via `anaconda login` and test your login with the whoami command
```
anaconda whoami
```
Uploading a package:
```
anaconda upload path/to/package-build
```
In my case (using miniconda on linux) the package build is located somewhere under `$HOME/miniconda3/conda-bld/`.
