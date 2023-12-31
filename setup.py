from setuptools import setup

setup(
    name='tng_routines',
    version='0.1.0',    
    description='A example Python package',
    url='https://https://github.com/astropradyumna/tng_routines',
    author='Pradyumna Sadhu',
    author_email='pradyumna.sadhu@gmail.com',
    license='BSD 2-clause',
    packages=['tng_routines'],
    install_requires=['numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
)