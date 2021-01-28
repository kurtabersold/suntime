from setuptools import find_packages, setup

requires = {
    'setup': [
        'invoke',
    ],
    'install': [
        'astral',
    ],
    'tests': [
        'pytest',
        'pytest-cov',
        'pytest-flake8',
    ],
}

# Yank together all subsections, including ones setup() isn't explictly
# otherwise using.  Doing this allows installation as package[all] for all
# possible dependencies.
requires['all'] = list({dep for deps in requires.values() for dep in deps})

setup(
    name='suntime',
    version='0.0.0',
    description='Sunrise Sunset Calculator',
    url='https://github.com/kurtabersold/suntime',
    author='Kurt Abersold',
    author_email='kurtabersold@gmail.com',
    packages=find_packages(exclude=['test', 'docs']),
    setup_requires=requires['setup'],
    install_requires=requires['install'],
    tests_require=requires['tests'],
    extras_require=requires,
    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            # 'suntime = suntime.cli:main',
        ],
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
    ],
)

