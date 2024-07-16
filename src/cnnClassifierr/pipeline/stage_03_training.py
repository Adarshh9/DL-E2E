from cnnClassifierr.entity.config_entity import PrepareBaseModelConfig ,TrainingConfig
from cnnClassifierr.components.prepare_callbacks import PrepareCallback
from cnnClassifierr.components.training import Training
from cnnClassifierr.config.configuration import ConfigurationManager
from cnnClassifierr import logger

STAGE_NAME = 'Training Stage'

class TrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callback_config = config.get_prepare_callback_config()
        prepare_callback = PrepareCallback(config=prepare_callback_config)
        callback_List = prepare_callback.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_List=callback_List
        )

if __name__ == "__main__":

    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
