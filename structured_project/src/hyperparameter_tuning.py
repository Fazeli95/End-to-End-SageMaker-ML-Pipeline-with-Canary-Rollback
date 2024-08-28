
import sagemaker
from sagemaker.tuner import HyperparameterTuner, ContinuousParameter, IntegerParameter
from sagemaker.xgboost import XGBoost

def hyperparameter_tuning(role, bucket):
    xgb = XGBoost(entry_point='train.py',
                  role=role,
                  instance_count=1,
                  instance_type='ml.m5.xlarge',
                  framework_version='1.3-1',
                  py_version='py3')

    hyperparameter_ranges = {
        'eta': ContinuousParameter(0, 1),
        'min_child_weight': ContinuousParameter(1, 10),
        'max_depth': IntegerParameter(1, 10)
    }

    tuner = HyperparameterTuner(estimator=xgb,
                                objective_metric_name='validation:logloss',
                                hyperparameter_ranges=hyperparameter_ranges,
                                max_jobs=10,
                                max_parallel_jobs=2)

    tuner.fit({'train': f's3://{bucket}/train', 'validation': f's3://{bucket}/validation'})

if __name__ == "__main__":
    hyperparameter_tuning('your-role-arn', 'your-s3-bucket')
