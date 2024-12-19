from setuptools import setup, find_packages

setup(
    name="sdt_platform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sdt_platform=sdt_platform.__main__:main",
        ]
    },
)
