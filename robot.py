#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

# Run the program
# ---------------
#
# To run the program you will need to explicitly use the ws-client option:
#
#    # Windows
#    py -3 -m robotpy sim --xrp
#
#    # Linux/macOS/Chromebook
#    python -m robotpy sim --xrp
#
# By default the WPILib simulation GUI will be displayed. To disable the display
# you can add the --nogui option
#

import os
import wpilib

import drivetrain
import arm

# If your XRP isn't at the default address, set that here
os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"

class MyRobot(wpilib.TimedRobot):

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be used for any
        initialization code.
        """
        # Assumes a gamepad plugged into channnel 0
        self.joystick = wpilib.Joystick(0)

        # create a drivetrain (contains two motors, two encoders and a gyro)
        self.drivetrain = drivetrain.Drivetrain()
        self.arm = arm.Arm()


    def robotPeriodic(self) -> None:
        """This function is called periodically (by default, 50 times per second)"""
        super().robotPeriodic()

        # 1. driving: take the speeds from joystick
        fwd_speed = self.joystick.getRawAxis(1)
        turn_speed = self.joystick.getRawAxis(0)
        self.drivetrain.arcadeDrive(fwd_speed, turn_speed)
        self.drivetrain.periodic()  # updates odometry


    def teleopPeriodic(self) -> None:
        """This function is called periodically when in operator control mode"""


    def teleopInit(self) -> None:
        """This function is initially when operator control mode runs"""
        self.drivetrain.stop()


    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""
        self.drivetrain.stop()


    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""


    def autonomousInit(self) -> None:
        """This autonomous runs the autonomous command selected by your RobotContainer class."""
        self.drivetrain.stop()


    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""


    def testInit(self) -> None:
        """Cancels all running commands at the start of test mode"""
        self.drivetrain.stop()
