#!/usr/bin/env python3

from aws_cdk import core

app = core.App()

tokyo = core.Environment(account='843493563478', region='ap-northeast-1')
seoul = core.Environment(account='843493563478', region='ap-northeast-2')
singapore = core.Environment(account='843493563478', region='ap-southeast-1')
sydney = core.Environment(account='843493563478', region='ap-southeast-2')
mumbai = core.Environment(account='843493563478', region='ap-south-1')
#frankfurt = core.Environment(account='843493563478', region='eu-central-1')

# VPC 
from aws_http_test.vpc_stack import VPCStack

vpc_tokyo_stack = VPCStack(app, "tokyo", "10.0.0.0/16", env=tokyo)
vpc_tokyo = vpc_tokyo_stack.vpc

vpc_seoul_stack = VPCStack(app, "seoul", "10.0.0.0/16", env=seoul)
vpc_seoul = vpc_seoul_stack.vpc

vpc_singapore_stack = VPCStack(app, "singapore", "10.0.0.0/16", env=singapore)
vpc_singapore = vpc_singapore_stack.vpc

vpc_sydney_stack = VPCStack(app, "sydney", "10.0.0.0/16", env=sydney)
vpc_sydney = vpc_sydney_stack.vpc

vpc_mumbai_stack = VPCStack(app, "mumbai", "10.0.0.0/16", env=mumbai)
vpc_mumbai = vpc_mumbai_stack.vpc

#vpc_frankfurt_stack = VPCStack(app, "frankfurt", "10.0.0.0/16", env=frankfurt)
#vpc_frankfurt = vpc_frankfurt_stack.vpc

# http Server
from aws_http_test.http_server_stack import httpServer

http_server_tokyo = httpServer(app, "http-server-tokyo", vpc_tokyo, env=tokyo)
http_server_singapore = httpServer(app, "http-server-singapore", vpc_singapore, env=singapore)
#http_server_frankfurt = httpServer(app, "http-server-frankfurt", vpc_frankfurt, env=frankfurt)

# http Client
from aws_http_test.http_client_stack import httpClient

http_client_tokyo = httpClient(app, "http-client-tokyo", vpc_tokyo, env=tokyo)
http_client_seoul = httpClient(app, "http-client-seoul", vpc_seoul, env=seoul)
http_client_singapore = httpClient(app, "http-client-singapore", vpc_singapore, env=singapore)
http_client_sydney = httpClient(app, "http-client-sydney", vpc_sydney, env=sydney)
http_client_mumbai = httpClient(app, "http-client-mumbai", vpc_mumbai, env=mumbai)
#http_server_frankfurt = httpServer(app, "http-server-frankfurt", vpc_frankfurt, env=frankfurt)

app.synth()