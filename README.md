# flask-serverless
Flask, PynamoDB, Serverless를 활용하여 AWS API Gateway, Lambda, DynamoDB 환경에서 서비스하는 프로젝트입니다.

자세한 설명은 아래 블로그 URL을 참고하세요.

https://blog.naver.com/indy9052/221812731781

## 실행 환경과 테스트

Python 3.12를 사용합니다. Lambda 런타임도 `python3.12`로 설정되어 있습니다.
Flask 3의 JSON provider 설정을 사용하며, 최신 botocore와의 호환성을 위해 PynamoDB 6을 사용합니다.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m unittest -v test_compatibility
```

테스트는 Moto로 DynamoDB를 모의 실행하여 사용자 CRUD, 입력 검증, CORS와 한글 JSON 응답을 확인합니다.
실제 AWS 자격 증명이나 배포는 필요하지 않습니다.
