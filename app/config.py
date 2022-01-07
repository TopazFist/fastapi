from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str = "ec2-54-211-74-66.compute-1.amazonaws.com"
    database_port: str = "5432"
    database_password: str = "90f6f41cc9dc8e04f136896fc68d063ec659131c1a6c604fe5e00f99f1448266"
    database_name: str = "dbl1or5b13se4e"
    database_username: str = "kbhrksbwbigscz"
    secret_key: str = "hello"
    algorithm: str ="HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
