from setuptools import setup

package_name = 'reseq'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gio2chi',
    maintainer_email='gio.angaroni@gmail.com',
    description='Temperature logger for the reseq project',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'temperature_logger = reseq.temperature_logger:main',
            'temperature_sensor = reseq.temperature_sensor:main',
        ],
    },
)
