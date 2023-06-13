import rospy
from sensor_msgs.msg import PointCloud2
from cms_common.utils import make_point_cloud

class TF03:
    def __init__(self):
        rospy.init_node("benewake_sensor")
        self.point_cloud_pub = rospy.Publisher('benewake/pc', PointCloud2, queue_size=1)
    
    def send_data(self, z):
        pc = make_point_cloud([0,0,z/100.0])
        self.point_cloud_pub.publish(pc)
