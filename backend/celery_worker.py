from celery import Celery, signals
from utils import generate_output
from langchain_community.llms import LlamaCpp

# from handlers import MyCustomHandler


def make_celery(app_name=__name__):
    backend = broker = 'redis://redis:6379/0'
    return Celery(app_name, backend=backend, broker=broker, broker_connection_retry_on_startup = True)


celery = make_celery()

llm = None
model_path = "model/phi-2.Q4_K_M.gguf"


@signals.worker_process_init.connect
def setup_model(signal, sender, **kwargs):
    global llm
    llm_cpp = LlamaCpp(
        model_path=model_path,
        temperature=0.75,
        max_tokens=20,
        top_p=1,
        # callbacks=callbacks,
        verbose=True
    )
    llm = llm_cpp


@celery.task
def generate_text_task(prompt):
    memory, time, outputs = generate_output(
        prompt, llm
    )
    return outputs, time, memory