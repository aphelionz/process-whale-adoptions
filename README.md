# Ocean Alliance Whale Adoptions _(process_whale_adoptions)_
> Script to run and process the adoption certificates from https://shop.whale.org

## Install

Prerequisitites:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- `libjpeg-dev` in Linux environments
- An AWS Account with API Keys for SES and S3

```bash
$ git clone git@bitbucket.org:mrhio/process_whale_adoptions.git
```

### Environment Variables

Copy [`.env.example`](./.env.example) to `.env` and set the following values:

- `SHOPIFY_API_KEY`
- `SHOPIFY_PASSWORD`
- `REGION_NAME`
- `SES_AWS_ACCESS_KEY_ID`
- `SES_AWS_SECRET_ACCESS_KEY`
- `S3_AWS_ACCESS_KEY_ID`
- `S3_AWS_SECRET_ACCESS_KEY`

### Local Installation

Setup:
```bash
$ python -m venv ./venv
$ ./venv/bin/pip install wheel
$ ./venv/bin/pip install -r ./requirements.txt
```

## Usage

This repo contains a convenience script, [`run.sh`](./run.sh)
```bash
$ ./run.sh
```

### Docker Deployment

TODO

## License

TODO
