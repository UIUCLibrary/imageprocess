from setuptools import setup

setup(
    packages=['uiucprescon.images'],
    namespace_packages=["uiucprescon"],
    install_requires=["pykdu_compress"],
    setup_requires=['pytest-runner'],
    test_suite="tests",
    tests_require=[
        'pytest',
    ],
    zip_safe=False,
)
