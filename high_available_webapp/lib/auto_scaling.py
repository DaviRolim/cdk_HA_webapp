from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elb,
    aws_ec2 as ec2,
    core
)

with open("./high_available_webapp/lib/user_data.sh") as f:
    user_data = f.read()

class ASGLib:

    def __init__(self, scope: core.Construct, construct_id: str, vpc: ec2.Vpc, **kwargs) -> None:

        self.ASG = autoscaling.AutoScalingGroup(
            scope, 'ASG webapp',
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            #  machine_image=ec2.MachineImage.generic_linux(
            #     ami_map={
            #         'us-west-2': 'ami-0e999cbd62129e3b1'
            #     }
            # ),
            vpc=vpc,
            min_capacity=2,
            max_capacity=5,
            user_data=ec2.UserData.custom(user_data),
            health_check=autoscaling.HealthCheck.elb(grace=core.Duration.minutes(2))
        )
        self.ASG.scale_on_cpu_utilization('scaleOnCPUmetric',target_utilization_percent=75)
       



        # ec2.Instance(
        #     scope,
        #     f'{construct_id}Ec2Instance',
        #     instance_type=ec2.InstanceType('t2.micro'),
        #     machine_image=ec2.MachineImage.generic_linux(
        #         ami_map={
        #             'us-west-2': 'ami-0e999cbd62129e3b1'
        #         }
        #     ),
        #     user_data=ec2.UserData.custom(user_data),
        #     vpc=vpc,
        #     vpc_subnets=ec2.SubnetSelection(subnet_group_name='public-sub-1'),
        #     security_group=security_group
        # )
