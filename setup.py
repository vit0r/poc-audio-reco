"""POC - This is the example module of capture audio to speech in text."""

from setuptools import setup

setup(
    name='POCspeech',
    version='2.0.0',
    license='BSD',
    url='https://github.com/vit0r/speech_reco',
    author='Vitor Nascimento Araujo',
    author_email='',
    description='Sample',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    install_requires=['pylint', 'autopep8','speechrecognition', 'pyaudio', 'numpy','nose' ,'virtualenv']
)
