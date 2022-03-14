from setuptools import setup

setup(
    name='PREDICT_API',
    version='1.0',
    long_description=__doc__,
    packages=['PREDICT_API'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)