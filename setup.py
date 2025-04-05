from setuptools import setup, find_packages

setup(
    name="pi2_0",
    version="1.0.0",
    description="P2_0 is an interactive Python bot that provides various perspectives and insights on a given question by simulating different ways of thinking.",
    author="RaiffsBits",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "openai==0.27.0",
        "httpx==0.23.0",
        "requests==2.28.1",
        "google-auth==2.14.1",
        "google-api-python-client==2.64.0",
        "googletrans==4.0.0-rc1",
        "textblob==0.17.1",
        "vaderSentiment==3.3.2",
        "tenacity==8.1.0",
        "python-dotenv==0.21.0",
        "tkinter==0.1.0",
        "botbuilder-core==4.16.2",
        "botbuilder-schema==4.16.2",
        "transformers==4.30.2",
        "torch==2.0.1",
        "scikit-learn==1.2.2"
    ],
    entry_points={
        'console_scripts': [
            'start=pi2_0.pibrain:main',
        ],
    },
)