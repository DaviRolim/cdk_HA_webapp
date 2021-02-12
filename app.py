#!/usr/bin/env python3

from aws_cdk.core import App, Stack, CfnParameter, NestedStack
from high_available_webapp.stack.vpc_stack import NetworkStack
from high_available_webapp.stack.application_stack import ApplicationStack

app = App()

main_stack = Stack(app, 'High-Available-WebApps', env={'region': 'us-west-2'})

vpc_stack = NetworkStack(main_stack, 'VpcStack')

ha_app_stack = ApplicationStack(main_stack, 'HA-APP', vpc=vpc_stack.vpc)


# load_balancer = LoadBalancerLib(main_stack, 'ALB', vpc=vpc_stack.vpc, auto_scaling=auto_scaling.ASG)

# webapp_stack = NestedStack(main_stack, 'WebApps')
# webapp_app_1 = AppLib(webapp_stack, 'WebAppStack1', vpc=vpc_stack.vpc, security_group=vpc_stack.security_group)
# webapp_app_2 = AppLib(webapp_stack, 'WebAppStack2', vpc=vpc_stack.vpc, security_group=vpc_stack.security_group)

app.synth()
