# setup.sample.py

from setuptools import find_packages, setup

package_name = '1_pubsub'   # 자동 수정

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',   
            ['launch/my_launch.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = 1_pubsub.talker:main',   # 수정
            'processor = 1_pubsub.processor:main',   # 수정
            'listener = 1_pubsub.listener:main',   # 수정
        ],
    },
)