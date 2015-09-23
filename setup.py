from setuptools import setup, find_packages


setup(
    name='appresso_sphinx_extensions',
    description='Sphinx documentation system extensions created by Appresso AS',
    version='1.0.0',
    license='BSD',
    url='https://github.com/appresso/appresso_sphinx_extensions',
    author='Espen Angell Kristiansen',
    author_email='post@espenak.net',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    long_description='See https://github.com/appresso/appresso_sphinx_extensions',
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: Python'
    ]
)