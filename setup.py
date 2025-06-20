from setuptools import setup

setup(
    name='catmail',
    version="0.1.2",
    author='Mario Balibrera',
    author_email='mario.balibrera@gmail.com',
    license='MIT License',
    description='email tools for cats',
    long_description='simple classes for email automation',
    packages=[
        'catmail'
    ],
    zip_safe = False,
    install_requires = [
        "fyg >= 0.1.2.5",
        "rel >= 0.4.9.20",
        "yagmail >= 0.6.161"
    ],
    entry_points = '''''',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
