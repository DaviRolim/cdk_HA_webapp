from aws_cdk import (
    aws_iam as iam,
    aws_ec2 as ec2,
    core,
    aws_cloudformation as cfn
)

from lib.auto_scaling import ASGLib
from lib.load_balancer import LoadBalancerLib

class ApplicationStack(core.NestedStack):

    def __init__(self, scope: core.Construct, construct_id: str,
                vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.asg = ASGLib(self, 'ASG', vpc=vpc)

        self.alb = LoadBalancerLib(self, 'ALB', vpc=vpc, auto_scaling=self.asg.ASG)



