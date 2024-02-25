from controller import Robot, Joystick

class PedestrianController(Robot):
    def __init__(self):
        super(PedestrianController, self).__init__()
        self.timestep = int(self.getBasicTimeStep())
        
        # Initialize joint devices (replace with your actual joint names)
        self.joint_names = [
            "PedestrianTorso", "PedestrianNeck",
            "PedestrianLeftUpperArm", "PedestrianLeftLowerArm", "PedestrianLeftHand",
            "PedestrianRightUpperArm", "PedestrianRightLowerArm", "PedestrianRightHand",
            "PedestrianLeftUpperLeg", "PedestrianLeftLowerLeg", "PedestrianLeftFoot",
            "PedestrianRightUpperLeg", "PedestrianRightLowerLeg", "PedestrianRightFoot",
            "PedestrianHead"
        ]
        
        self.joints = {name: self.getDevice(name) for name in self.joint_names}
        for joint in self.joints.values():
            joint.setPosition(0.0)  # Initialize all joints to a neutral position
        
        # Initialize joystick
        self.joystick = Joystick()
        self.joystick.enable(self.timestep)

    def run(self):
        while self.step(self.timestep) != -1:
            # Read joystick input
            x_axis = self.joystick.getAxis(0)  # X-axis (left-right)
            y_axis = self.joystick.getAxis(1)  # Y-axis (up-down)
            
            # Example movement: Adjust joint positions based on joystick input
            self.joints["PedestrianRightUpperArm"].setPosition(x_axis)  # Adjust arm position
            self.joints["PedestrianRightLowerArm"].setPosition(y_axis)  # Adjust elbow position
            # Add more complex movement logic here
            
if __name__ == "__main__":
    pedestrian_controller = PedestrianController()
    pedestrian_controller.run()
