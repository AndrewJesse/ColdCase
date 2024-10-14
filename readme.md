## How to install and use this package

1) cd to `root`
2) `pip install git+https://github.com/AndrewJesse/ColdCase.git`



Remove-Item -Recurse -Force dist, build
python setup.py sdist bdist_wheel
twine upload dist/*
