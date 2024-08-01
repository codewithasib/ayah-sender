from setuptools import setup, find_packages
setup(
    name="ayah-sender",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ayah-sender': ['reciters.csv'],
    },
    install_requires=[
        "requests",
        "pydub",
    ],
    author="Asib Hossen",
    author_email="dev.asib@proton.me",
    description="A package to get audio of a single verse or multiples verses from a Chapter of The Holy Quran",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/codewithasib/ayah-sender",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

