from cnnClassifierr.entity.config_entity import EvaluationConfig
from cnnClassifierr.components.evaluation import Evaluation
from cnnClassifierr.config.configuration import ConfigurationManager
from cnnClassifierr import logger

STAGE_NAME = 'Evaluation Stage'

class EvaluationPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        valid_config = config.get_validation_config()
        evaluation = Evaluation(config=valid_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":

    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
