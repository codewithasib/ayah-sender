from setuptools import setup, find_packages
setup(
    name="ayah_sender",
    version="0.1.6",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ayah_sender': ['reciters.csv'],
    },
    install_requires=[
        "requests",
        "pydub",
    ],
    author="Asib Hossen",
    author_email="dev.asib@proton.me",
    description="Get Quranic audio and images easily.",
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

