using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public class UtilityFunctions
{
    public static string NewtonThoughts(string question)
    {
        return ApplyNewtonsLaws(question);
    }

    private static string ApplyNewtonsLaws(string question)
    {
        if (string.IsNullOrEmpty(question))
            return "No question to think about.";

        int complexity = question.Length;
        int force = MassOfThought(question) * AccelerationOfThought(complexity);
        return $"Thought force: {force}";
    }

    private static int MassOfThought(string question)
    {
        return question.Length;
    }

    private static int AccelerationOfThought(int complexity)
    {
        return complexity / 2;
    }

    public static string DaVinciInsights(string question)
    {
        return ThinkLikeDaVinci(question);
    }

    private static string ThinkLikeDaVinci(string question)
    {
        var perspectives = new List<string>
        {
            $"What if we view '{question}' from the perspective of the stars?",
            $"Consider '{question}' as if it's a masterpiece of the universe.",
            $"Reflect on '{question}' through the lens of nature's design."
        };
        var random = new        var random = new Random();
        return perspectives[random.Next(perspectives.Count)];
    }

    public static string HumanIntuition(string question)
    {
        var intuition = new List<string>
        {
            "How does this question make you feel?",
            "What emotional connection do you have with this topic?",
            "What does your gut instinct tell you about this?"
        };
        var random = new Random();
        return intuition[random.Next(intuition.Count)];
    }

    public static string NeuralNetworkThinking(string question)
    {
        var neuralPerspectives = new List<string>
        {
            $"Process '{question}' through a multi-layered neural network.",
            $"Apply deep learning to uncover hidden insights about '{question}'.",
            $"Use machine learning to predict patterns in '{question}'."
        };
        var random = new Random();
        return neuralPerspectives[random.Next(neuralPerspectives.Count)];
    }

    public static string QuantumComputingThinking(string question)
    {
        var quantumPerspectives = new List<string>
        {
            $"Consider '{question}' using quantum superposition principles.",
            $"Apply quantum entanglement to find connections in '{question}'.",
            $"Utilize quantum computing to solve '{question}' more efficiently."
        };
        var random = new Random();
        return quantumPerspectives[random.Next(quantumPerspectives.Count)];
    }

    public static string ResilientKindness(string question)
    {
        var kindnessPerspectives = new List<string>
        {
            "Despite losing everything, seeing life as a chance to grow.",
            "Finding strength in kindness after facing life's hardest trials.",
            "Embracing every challenge as an opportunity for growth and compassion."
        };
        var random = new Random();
        return kindnessPerspectives[random.Next(kindnessPerspectives.Count)];
    }

    public static string IdentifyAndRefuteFallacies(string argument)
    {
        var fallacies = new List<string>
        {
            "Ad Hominem",
            "Straw Man",
            "False Dilemma",
            "Slippery Slope",
            "Circular Reasoning",
            "Hasty Generalization",
            "Red Herring",
            "Post Hoc Ergo Propter Hoc",
            "Appeal to Authority",
            "Bandwagon Fallacy",
            "False Equivalence"
        };
        var refutations = new List<string>
        {
            "This is an ad hominem fallacy. Let's focus on the argument itself rather than attacking the person.",
            "This is a straw man fallacy. The argument is being misrepresented.",
            "This is a false dilemma fallacy. There are more options than presented.",
            "This is a slippery slope fallacy. The conclusion does not necessarily follow from the premise.",
            "This is circular reasoning. The argument's conclusion is used as a premise.",
            "This is a hasty generalization. The conclusion is based on insufficient evidence.",
            "This is a red herring fallacy. The argument is being diverted to an irrelevant topic.",
            "This is a post hoc ergo propter hoc fallacy. Correlation does not imply causation.",
            "This is an appeal to authority fallacy. The argument relies on the opinion of an authority figure.",
            "This is a bandwagon fallacy. The argument assumes something is true because many people believe it.",
            "This is a false equivalence fallacy. The argument equates two things that are not equivalent."
        };
        var random = new Random();
        return refutations[random.Next(refutations.Count)];
    }

    public static string UniversalReasoning(string question)
    {
        var responses = new List<string>
        {
            NewtonThoughts(question),
            DaVinciInsights(question),
            HumanIntuition(question),
            NeuralNetworkThinking(question),
            QuantumComputingThinking(question),
            ResilientKindness(question),
            IdentifyAndRefuteFallacies(question)
        };
        return string.Join("\n", responses);
    }

    public static async Task<string> GetWeather(string location)
    {
        var apiKey = Environment.GetEnvironmentVariable("WEATHER_API_KEY");
        var baseUrl = "http://api.openweathermap.org/data/2.5/weather?";
        var completeUrl = $"{baseUrl}q={location}&appid={apiKey}";

        using var httpClient = new HttpClient();
        var response = await httpClient.GetStringAsync(completeUrl);
        var weatherData = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(response);

        if (weatherData["cod"].ToString() != "404")
        {
            var main = weatherData["main"] as Dictionary<string, object>;
            var weather = (weatherData["weather"] as List<Dictionary<string, object>>)[0];
            var temperature = main["temp"];
            var description = weather["description"];
            return $"The weather in {location} is currently {description} with a temperature of {temperature}°K.";
        }
        else
        {
            return "Location not found.";
        }
    }

    public static async Task<string> GetLatestNews()
    {
        var apiKey = Environment.GetEnvironmentVariable("NEWS_API_KEY");
        var baseUrl = "https://newsapi.org/v2/top-headlines?";
        var completeUrl = $"{baseUrl}country=us&apiKey={apiKey}";

        using var httpClient = new HttpClient();
        var response = await httpClient.GetStringAsync(completeUrl);
        var newsData = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(response);

        if (newsData["status"].ToString() == "ok")
        {
            var articles = newsData["articles"] as List<Dictionary<string, object>>;
            var headlines = new List<string>();
            for (int i = 0; i < Math.Min(5, articles.Count); i++)
            {
                headlines.Add(articles[i]["title"].ToString());
            }
            return "Here are the latest news headlines:\n" + string.Join("\n", headlines);
        }
        else
        {
            return "Failed to fetch news.";
        }
    }

    public static async Task<string> GetStockPrice(string symbol)
    {
        var apiKey = Environment.GetEnvironmentVariable("ALPHA_VANTAGE_API_KEY");
        var baseUrl = "https://www.alphavantage.co/query?";
        var completeUrl = $"{baseUrl}function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apiKey}";

        using var httpClient = new HttpClient();
        var response = await httpClient.GetStringAsync(completeUrl);
        var stockData = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(response);

        if (stockData.ContainsKey("Time Series (5min)"))
        {
            var latestTime = (stockData["Time Series (5min)"] as Dictionary<string, object>).Keys.First();
            var latestClose = ((stockData["Time Series (5min)"] as Dictionary<string, object>)[latestTime] as Dictionary<string, object>)["4. close"];
            return $"The latest closing price of {symbol} is ${latestClose}.";
        }
        else
        {
            return "Failed to fetch stock price.";
        }
    }

    public static async Task<string> TranslateText(string text, string destLanguage)
    {
        var apiKey = Environment.GetEnvironmentVariable("TRANSLATION_API_KEY");
        var baseUrl = "https://translation.googleapis.com/language/translate/v2?";
        var completeUrl = $"{baseUrl}q={text}&target={destLanguage}&key={apiKey}";

        using var httpClient = new HttpClient();
        var response = await httpClient.GetStringAsync(completeUrl);
        var translationData = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(response);

        var translatedText = ((translationData["data"] as Dictionary<string, object>)["translations"] as List<Dictionary<string, object>>)[0]["translatedText"].ToString();
        return translatedText;
    }
}