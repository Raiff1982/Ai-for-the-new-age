using System;
using System.Collections.Generic;
using Microsoft.ML;
using Microsoft.ML.Data;
using Microsoft.Extensions.Logging;

public class SentimentAnalysis
{
    private readonly ILogger<SentimentAnalysis> _logger;
    private readonly MLContext _mlContext;
    private readonly PredictionEngine<SentimentData, SentimentPrediction> _predictionEngine;

    public SentimentAnalysis(ILogger<SentimentAnalysis> logger)
    {
        _logger = logger;
        _mlContext = new MLContext();
        var model = TrainModel();
        _predictionEngine = _mlContext.Model.CreatePredictionEngine<SentimentData, SentimentPrediction>(model);
    }

    private ITransformer TrainModel()
    {
        var data = new List<SentimentData>
        {
            new SentimentData { Text = "I love this product! It's amazing.", Label = true },
            new SentimentData { Text = "This is the worst thing I've ever bought.", Label = false }
        };

        var trainData = _mlContext.Data.LoadFromEnumerable(data);
        var pipeline = _mlContext.Transforms.Text.FeaturizeText("Features", nameof(SentimentData.Text))
            .Append(_mlContext.BinaryClassification.Trainers.SdcaLogisticRegression(labelColumnName: nameof(SentimentData.Label), featureColumnName: "Features"));

        return pipeline.Fit(trainData);
    }

    public SentimentPrediction Predict(string text)
    {
        var sentimentData = new SentimentData { Text = text };
        return _predictionEngine.Predict(sentimentData);
    }

    public class SentimentData
    {
        public string Text { get; set; }
        public bool Label { get; set; }
    }

    public class SentimentPrediction : SentimentData
    {
        [ColumnName("PredictedLabel")]
        public bool Prediction { get; set; }
        public float Probability { get; set; }
        public float Score { get; set; }
    }
}