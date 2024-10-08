from setuptools import find_packages, setup
from glob import glob

package_name = 'auto-navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/navigation.launch.py',
            'launch/turtlebot3_world.launch.py',
            'launch/robot_state_publisher.launch.py',
            'launch/spawn_turtlebot3.launch.py'
        ]),
        ('share/' + package_name+'/urdf/', glob('urdf/*')),
        ('share/' + package_name+'/rviz/', glob('rviz/*')),
        ('share/' + package_name+'/meshes/collision/', glob('meshes/collision/*')),
        ('share/' + package_name+'/meshes/visual/', glob('meshes/visual/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reno',
    maintainer_email='490412@student.fontys.nl',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
