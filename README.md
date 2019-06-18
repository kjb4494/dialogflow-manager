# Dialogflow Manager Project

#### 개발 메모장
- [*사용한 템플릿*](https://startbootstrap.com/themes/sb-admin-2/)
- [*템플릿 소스코드*](https://github.com/BlackrockDigital/startbootstrap-sb-admin-2)


#### 설정파일 생성하기
- config.py
    ```
    import os
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(base_dir, 'dialogflow-service-account.json')
    project_id = 'project_id'
    language_code = 'ko'
    ```
- dialogflow-service-account.json
    ```
    # dialogflow service account file
    {
      "type": "service_account",
      ...
      "client_x509_cert_url": "..."
    }
    ```
