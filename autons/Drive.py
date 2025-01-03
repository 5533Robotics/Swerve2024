import commands2
from autons.BuildData import BuildData
from subsystems.command_swerve_drivetrain import CommandSwerveDrivetrain
from phoenix6 import swerve

class Drive(commands2.Command):
    def __init__(self, drive: swerve.requests.FieldCentric, drive_train: CommandSwerveDrivetrain, data: BuildData) -> None:
        drive_train.apply_request(
            lambda: drive.with_velocity_x(0).with_velocity_y(0).with_rotational_rate(0)
        ).withTimeout(data.time().get())