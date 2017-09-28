from chat import views
from config.bootstrap import get_config


def setup_routes(router):
    config = get_config()

    router.add_get('/add', views.show_message)
    router.add_post('/add', views.add_message)
    router.add_static('/static', config['base_path'] + '/static')
