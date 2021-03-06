import config
import logging


connex_app = config.connex_app


@connex_app.route("/")
def home():
    return "<h1>This is main page<h1>"


if __name__ == "__main__":
    # Read swagger file
    connex_app.add_api("swagger.yml", arguments={'api_local': 'local_value'})
    logging.basicConfig(level="DEBUG", filename="app_log.log")
    logger = logging.getLogger()
    connex_app.run(debug=True, port=8000)



