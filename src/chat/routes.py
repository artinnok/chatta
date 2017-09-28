from chat.views import add_message
from config.bootstrap import get_config


def setup_routes(router):
    config = get_config()

    router.add_get('/add', add_message)
    router.add_static('/static', config['base_path'] + '/static')
