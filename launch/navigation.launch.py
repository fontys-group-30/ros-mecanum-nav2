import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    config_dir = "/home/reno/turtlebot3_ws/src/auto-navigation/config"
    param_file = os.path.join(config_dir, "tb3_nav_params.yaml")
    map_file = os.path.join(config_dir, "my_map.yaml")
    rviz_config_dir = os.path.join(config_dir, 'navigation.rviz')

    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'turtlebot3_world.launch.py')]),
        # ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')]),
            launch_arguments={
                "map": map_file,
                "params_file": param_file,
            }.items()
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2_node",
            arguments=["-d", rviz_config_dir],
            output="screen",
        )
    ])
