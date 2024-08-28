
import sagemaker
from sagemaker.model import Model

def deploy_model(model_data, role, endpoint_name):
    model = Model(model_data=model_data,
                  role=role,
                  image_uri=sagemaker.image_uris.retrieve('xgboost', sagemaker.Session().boto_region_name, version="1.3-1"))

    predictor = model.deploy(initial_instance_count=1, instance_type='ml.m5.xlarge', endpoint_name=endpoint_name)
    return predictor

if __name__ == "__main__":
    deploy_model('s3://your-bucket/xgb_model.tar.gz', 'your-role-arn', 'your-endpoint-name')
