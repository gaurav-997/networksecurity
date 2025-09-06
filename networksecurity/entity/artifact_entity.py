from dataclasses import dataclass

# o/p of dataingestion i.e train & test file path , we will call it as dataingestion artifact

@dataclass
class DataIngestionArtifact:
    training_file_path:str
    test_file_path:str