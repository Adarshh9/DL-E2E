from cnnClassifierr import logger
from cnnClassifierr.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifierr.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifierr.pipeline.stage_03_training import TrainingPipeline
from cnnClassifierr.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Training Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Evaluation Stage'
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e