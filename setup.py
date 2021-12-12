import pathlib
import setuptools
import io
import re

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

with io.open("shpd/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setuptools.setup(
    name="sphinx-demo",
    version=version,
    description="A personal sphinx demo",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/BossZou/sphinx-demo',
    license="Apache-2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],#"grpcio>=1.22.0", "grpcio-tools>=1.22.0", "requests>=2.22.0", "ujson>=2.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6'
)

