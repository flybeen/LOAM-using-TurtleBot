#!/usr/bin/env python3
import rospy
import tf
import geometry_msgs.msg
import math

def main():
    rospy.init_node('tf_custom_relay_node')

    listener = tf.TransformListener()
    broadcaster = tf.TransformBroadcaster()
    pub = rospy.Publisher('/tf_transformed', geometry_msgs.msg.TransformStamped, queue_size=10)

    rate = rospy.Rate(10.0)
    try:
        while not rospy.is_shutdown():
            try:
                # '/map'에서 '/camera_init'로의 tf 정보를 가져옵니다.
                rospy.loginfo("Trying to look up transform from '/map' to '/camera_init'")
                (trans, rot) = listener.lookupTransform('/map', '/camera_init', rospy.Time(0))

                rospy.loginfo("Transform lookup successful.")
                rospy.loginfo(f"Translation: {trans}")
                rospy.loginfo(f"Rotation: {rot}")

                # '/custom_parent'를 브로드캐스트합니다 (필요 시).
                rospy.loginfo("Broadcasting '/custom_parent' relative to '/map'.")
                broadcaster.sendTransform(
                    trans,
                    rot,
                    rospy.Time.now(),
                    '/custom_parent',  # 새 부모 프레임
                    '/map'
                )

                # '/camera_init_temp'를 '/camera_init'의 자식으로 생성합니다.
                rospy.loginfo("Creating '/camera_init_temp' relative to '/camera_init'.")
                new_transform = geometry_msgs.msg.TransformStamped()
                new_transform.header.stamp = rospy.Time.now()
                new_transform.header.frame_id = '/camera_init'  # 부모 프레임을 '/camera_init'로 설정
                new_transform.child_frame_id = '/camera_init_temp'

                # '/camera_init_temp'에 추가 회전 (-90도, x축)을 적용합니다.
                rospy.loginfo("Applying additional rotation of -90 degrees around x-axis.")
                additional_rotation = tf.transformations.quaternion_from_euler(-math.pi/2, 0, 0)
                new_quat = tf.transformations.quaternion_multiply(additional_rotation, [0, 0, 0, 1])  # 단위 쿼터니언과 곱셈

                new_transform.transform.translation.x = 0.0
                new_transform.transform.translation.y = 0.0
                new_transform.transform.translation.z = 0.0
                new_transform.transform.rotation.x = new_quat[0]
                new_transform.transform.rotation.y = new_quat[1]
                new_transform.transform.rotation.z = new_quat[2]
                new_transform.transform.rotation.w = new_quat[3]

                # '/camera_init_temp' 브로드캐스트
                rospy.loginfo("Broadcasting '/camera_init_temp' relative to '/camera_init'.")
                broadcaster.sendTransform(
                    (new_transform.transform.translation.x,
                     new_transform.transform.translation.y,
                     new_transform.transform.translation.z),
                    (new_transform.transform.rotation.x,
                     new_transform.transform.rotation.y,
                     new_transform.transform.rotation.z,
                     new_transform.transform.rotation.w),
                    rospy.Time.now(),
                    '/camera_init_temp',
                    '/camera_init'  # 부모 프레임을 '/camera_init'로 설정
                )

                # 변환 결과 퍼블리시
                rospy.loginfo("Publishing new transform to /tf_transformed topic.")
                pub.publish(new_transform)

            except tf.LookupException:
                rospy.logwarn("LookupException: Could not find transform between '/map' and '/camera_init'.")
            except tf.ConnectivityException:
                rospy.logwarn("ConnectivityException: Connectivity problem detected with tf tree.")
            except tf.ExtrapolationException:
                rospy.logwarn("ExtrapolationException: Time extrapolation issue detected.")
            except Exception as e:
                rospy.logerr(f"Unexpected error: {e}")

            rate.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo("Shutting down gracefully.")
    except KeyboardInterrupt:
        rospy.loginfo("KeyboardInterrupt detected. Exiting.")
        return  # 노드 종료
    finally:
        rospy.loginfo("Node has been shut down.")

if __name__ == '__main__':
    main()
