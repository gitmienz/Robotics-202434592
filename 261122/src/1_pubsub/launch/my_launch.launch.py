from launch import LaunchDescription
from launch.actions import ExecuteProcess, RegisterEventHandler
from launch.event_handlers import OnProcessStart


def generate_launch_description():

    talker = ExecuteProcess(
        cmd=[
            'gnome-terminal', '--', 'bash', '-c',
            'source ~/robot_navigation/colcon_ws/install/setup.bash; '
            'ros2 run 1_pubsub talker; '
            'exec bash'
        ],
        output='screen'
    )

    processor = ExecuteProcess(
        cmd=[
            'gnome-terminal', '--', 'bash', '-c',
            'source ~/robot_navigation/colcon_ws/install/setup.bash; '
            'ros2 run 1_pubsub processor; '
            'exec bash'
        ],
        output='screen'
    )

    listener = ExecuteProcess(
        cmd=[
            'gnome-terminal', '--', 'bash', '-c',
            'source ~/robot_navigation/colcon_ws/install/setup.bash; '
            'ros2 run 1_pubsub listener; '
            'exec bash'
        ],
        output='screen'
    )

    return LaunchDescription([
        talker,

        RegisterEventHandler(
            OnProcessStart(
                target_action=talker,
                on_start=[processor]
            )
        ),

        RegisterEventHandler(
            OnProcessStart(
                target_action=processor,
                on_start=[listener]
            )
        ),
    ])