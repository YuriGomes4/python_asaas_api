from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='py_mp',
    version='0.0.1',
    license='MIT License',
    author='Yuri Gomes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='yurialdegomes@gmail.com',
    keywords='mercado pago',
    description=u'Wrapper não oficial do Mercado Pago',
    packages=['py_mp'],
    install_requires=['requests'],)