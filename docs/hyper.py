from azure.ai.ml.sweep import Normal, Uniform, RandomParameterSampling

command_job_for_sweep = command_job(   
    learning_rate=Normal(mu=10, sigma=3),
    keep_probability=Uniform(min_value=0.05, max_value=0.1),
    batch_size=Choice(values=[16, 32, 64, 128]),
)

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = "random",
    ...
)