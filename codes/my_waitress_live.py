from waitress import serve
import Flask_api

serve(Flask_api.web_app, host='0.0.0.0', port=8080)
