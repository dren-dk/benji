import os

running_pod_name = os.getenv('POD_NAME', 'unknown-pod-name')

benji_instance = os.getenv('BENJI_INSTANCE', 'benji')
benji_log_level = os.getenv('BENJI_LOG_LEVEL', 'INFO')