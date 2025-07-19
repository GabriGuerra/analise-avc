from setuptools import setup, find_packages

setup(
    name='analise_avc',
    version='1.0.0',
    author='Gabriel Guerra Samorano Pires',
    description='Exploratory analysis of clinical data related to stroke risk',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas>=1.3',
        'numpy>=1.21',
        'matplotlib>=3.4',
        'seaborn>=0.11',
        'scikit-learn>=1.0',
        'scipy>=1.7'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    python_requires='>=3.9',
)