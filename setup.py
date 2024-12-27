from setuptools import setup, find_packages

setup(
    name="sdt_platform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    package_data={
        "sdt.mapper": ["data/*.json"],  # Specify the directory and file pattern
    },
    entry_points={
        "console_scripts": [
            "sdt_platform=sdt_platform.__main__:main",
        ]
    },
)
