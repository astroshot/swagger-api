# Swagger UI

This project displays API doc based on Swagger UI by python server.

## Dependence

1. Python 3
2. buildout

## Usage

Write your Swagger yaml document in dir swagger, and start server.

## Start

### buildout installation

```bash
python -m pip install zc.buildout
```

### compile

Just enter the project path and run `buildout`.

### start server

```bash
bin/swagger-api --port=${port}
```

Default port is 8005.
