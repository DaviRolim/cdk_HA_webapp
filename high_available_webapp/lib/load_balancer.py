from aws_cdk import (
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elb,
    aws_ec2 as ec2,
    core
)

class LoadBalancerLib:

    def __init__(self, scope: core.Construct, construct_id: str, vpc: ec2.Vpc, auto_scaling: autoscaling.AutoScalingGroup, **kwargs) -> None:

        self.elb = elb.ApplicationLoadBalancer(
            scope, 'ALB-WebGroup',
            vpc=vpc,
            internet_facing=True,
            vpc_subnets=ec2.SubnetSelection(subnets=vpc.public_subnets)
        )
        listener = self.elb.add_listener('Listener', port=80, open=True)

        # For the healthcheck I could leave most of parameters blank as the default would sufface, but I put them here for reference later.
        listener.add_targets(
            'WebFleet',
            port=80,
            targets=[auto_scaling], 
            health_check=elb.HealthCheck(
                enabled=True,
                healthy_http_codes='200-399',
                interval=core.Duration.seconds(30),
                path='/index.php'
            )
        )
