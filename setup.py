import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="valve",
    version="0.0.1",
    author="LukeStrohbehn",
    author_email="luke.strohbehn@gmail.com",
    packages=["valve"],
    description="",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukestroh/valve",
    license='MIT',
    python_requires='>=3.8',
    install_requires=['pip'],
    setup_requires=['pip']
)
