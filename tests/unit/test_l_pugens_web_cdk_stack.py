import aws_cdk as core
import aws_cdk.assertions as assertions

from l_pugens_web_cdk.l_pugens_web_cdk_stack import LPugensWebCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in l_pugens_web_cdk/l_pugens_web_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LPugensWebCdkStack(app, "l-pugens-web-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
