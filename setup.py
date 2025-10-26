from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='behavioralflow',
    version='1.0.0',
    author='Ademilson',
    author_email='junior18ademilson@gmail.com',
    description='Uma biblioteca para simular alguns princípios comportamentais básicos, como reforçamento.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/varejad/behavioral_flow',
    packages=find_packages(),
    install_requires=[],  # Dependências necessárias
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache License 2.0',
    keywords='behavior analysis reinforcement learning psychology simulation',

)
