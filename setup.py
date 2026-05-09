from setuptools import setup

setup(
    name='todex',
    version='1.0.0',
    py_modules=['task_tracker'], # The name of your python file (without the .py)
    install_requires=[
        'pandas' # This tells pip to automatically install pandas if they don't have it!
    ],
    entry_points={
        'console_scripts': [
            'todex=task_tracker:main', 
        ],
    },
)
