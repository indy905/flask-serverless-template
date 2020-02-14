# flask-serverless
Flask, PynamoDB, Serverless를 활용하여 AWS API Gateway, Lambda, DynamoDB 환경에서 서비스하는 프로젝트입니다.

자세한 설명은 아래 블로그 URL을 참고하세요.

https://blog.naver.com/indy9052/



curl -XPUT "{ELASTICSERARCH_URL}/_ingest/pipeline/user-agent" -H 'Content-Type: application/json' -d'
{
  "description" : "Add user agent information",
  "processors" : [
    {
      "user_agent" : {
        "field" : "data.detail.user-agent"
      }
    }
  ]
}'
