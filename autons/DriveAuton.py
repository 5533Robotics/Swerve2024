import commands2

from autons.BuildData import BuildData
from autons.Drive import Drive
from subsystems.command_swerve_drivetrain import CommandSwerveDrivetrain
from phoenix6 import swerve

class DriveAuton(commands2.SequentialCommandGroup):
    def __init__(self, drive: swerve.requests.FieldCentric, drive_train: CommandSwerveDrivetrain) -> None:
        super().__init__(commands2.Command)
        data = BuildData()
        data.time().add(5)

        self.addCommands(
            Drive(drive, drive_train, data)
        )
    