from dataclasses import dataclass

# o/p of data ingestion i.e train & test file path , we will call it as dataingestion artifact

@dataclass
class DataIngestionArtifact:
    training_file_path:str
    test_file_path:str

# o/p of data validation     
@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str
    
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClasficationMetricsArtifact:
    f1_score:float
    precious_score: float
    recall_score:float
    
@dataclass
class ModelTrainingArtifact:
    trained_model_file_path: str
    train_metrics_artifact: ClasficationMetricsArtifact
    test_metrics_artifact: ClasficationMetricsArtifact
    