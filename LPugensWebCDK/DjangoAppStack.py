from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_route53 as route53,
    aws_route53_targets as targets,
    aws_ecs_patterns as ecs_patterns,
    aws_certificatemanager as acm,
    aws_elasticloadbalancingv2 as elbv2,
    aws_secretsmanager as secrets
)
from constructs import Construct

from LPugensWebCDK.StageConfigs import StageConfig


class DjangoAppStack(Stack):
    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            vpc: ec2.Vpc,
            stage_config: StageConfig,
            app_secrets: dict,
            **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = vpc

        self.ecs_cluster = ecs.Cluster(self, f"ECSCluster", vpc=self.vpc)

        # Instantiate the certificate which will be required by the load balancer later
        self.domain_certificate = acm.Certificate.from_certificate_arn(
            self, "DomainCertificate",
            certificate_arn='arn:aws:acm:us-east-1:721814170027:certificate/4cf95986-75ff-4c66-8303-23e8a501a61d'
        )

        self.fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            'DjangoApp',
            protocol=elbv2.ApplicationProtocol.HTTPS,
            certificate=self.domain_certificate,
            redirect_http=True,
            platform_version=ecs.FargatePlatformVersion.VERSION1_4,
            cluster=self.ecs_cluster,
            task_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
            cpu=stage_config.load_balancer_configs.cpu,
            memory_limit_mib=stage_config.load_balancer_configs.memory_limit_mib,
            desired_count=stage_config.load_balancer_configs.desired_count,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry(
                    name='lpugens/lpugens-web-django',
                    credentials=secrets.Secret.from_secret_name_v2(
                        self,
                        "DockerHubToken",
                        secret_name="/LPugensWeb/DockerHubToken"
                    ),
                ),
                container_name='django-app',
                container_port=8000,
                environment=stage_config.load_balancer_configs.environment,
                secrets=app_secrets,
            ),
            public_load_balancer=True,
        )

        self.hosted_zone = route53.HostedZone.from_lookup(
            self,
            "HostedZone",
            domain_name="lpugens.com"
        )
        self.dns_record = route53.ARecord(
            self,
            "ARecord",
            zone=self.hosted_zone,
            record_name=None,
            target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(self.fargate_service.load_balancer))
        )

