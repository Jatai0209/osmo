# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

import sys

from zara.log import log as logging
from oslo.config import cfg

# 因为log.py里用到了CONF，所以必须先使配置文件生效才行
cfg.CONF(sys.argv[1:], project='test', version='1.0',default_config_files=None)

CONF = cfg.CONF
print CONF.log_dir
print ". 代表当前目录"

logging.setup('test')
LOG = logging.getLogger(__name__)

LOG.info("jinlong.yang new test log")

