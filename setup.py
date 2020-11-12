import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="hexoplus",
    version="0.0.1",
    author="Xiaojie Luo",
    author_email="xiaojieluoff@gmail.com",
    description="hexo enhancement tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/xiaojieluo/hexoplus.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_required='>=3.6',
)
