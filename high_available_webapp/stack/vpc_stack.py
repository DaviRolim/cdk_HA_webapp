from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elb,
    aws_ec2 as ec2,
    core
)
with open("./high_available_webapp/lib/user_data.sh") as f:
    user_data = f.read()

class NetworkStack(core.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self, 'ProdVPC',
            cidr='10.0.0.0/16',
            max_azs=2,  # use all available AZs,
            subnet_configuration=[
                {
                    'cidrMask': 28,
                    'name': 'public-sub-1',
                    'subnetType': ec2.SubnetType.PUBLIC
                },
                {
                    'cidrMask': 28,
                    'name': 'private-sub-1',
                    'subnetType': ec2.SubnetType.PRIVATE
                }
      
            ]
        )

        # Security Group
        self.security_group = ec2.SecurityGroup(self, 'web-sg', vpc=self.vpc)
        self.security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_tcp(), description='allowall')



        # vpc = ec2.Vpc(
        #     self, 'ProdVPC',
        #     cidr='10.0.0.0/16',
        #     max_azs=2,  # use all available AZs,
        #     subnet_configuration=[
        #         {
        #             'cidrMask': 28,
        #             'name': 'public-sub-1',
        #             'subnetType': ec2.SubnetType.PUBLIC
        #         },
        #         {
        #             'cidrMask': 28,
        #             'name': 'private-sub-1',
        #             'subnetType': ec2.SubnetType.PRIVATE
        #         }
      
        #     ]
        # )

        # # Security Group
        # security_group = ec2.SecurityGroup(self, 'web-sg', vpc=vpc)
        # security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.all_tcp(), description='allowall')

        # elb1 = elb.ApplicationLoadBalancer(
        #     self, 'ALB-WebGroup',
        #     vpc=vpc,
        #     internet_facing=True,
        #     vpc_subnets=ec2.SubnetSelection(subnets=vpc.public_subnets)
        # )
        # listener = elb1.add_listener('Listener', port=80, open=True)

        # ASG = autoscaling.AutoScalingGroup(
        #     self, 'ASG webapp',
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
        #     machine_image=ec2.AmazonLinuxImage(),
        #     vpc=vpc,
        #     security_group=security_group,
        #     min_capacity=2,
        #     max_capacity=5,
        #     user_data=ec2.UserData.custom(user_data)
        # )
        # ASG.scale_on_cpu_utilization('scaleOnCPUmetric',target_utilization_percent=75)


        # # For the healthcheck I could leave most of parameters blank as the default would sufface, but I put them here for reference later.
        # listener.add_targets(
        #     'WebFleet',
        #     port=80,
        #     targets=[ASG], 
        #     health_check=elb.HealthCheck(
        #         enabled=True,
        #         healthy_http_codes='200-399',
        #         interval=core.Duration.seconds(30),
        #         path='/'
        #     )
        # )

      