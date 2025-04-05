using Xunit;
using Microsoft.Extensions.Logging;
using Moq;

public class MyBotTests
{
    [Fact]
    public async Task GenerateResponse_ShouldReturnExpectedResponse()
    {
        // Arrange
        var loggerMock = new Mock<ILogger<MyBot>>();
        var sentimentAnalysisMock = new Mock<SentimentAnalysis>(loggerMock.Object);
        var httpClientFactoryMock = new Mock<IHttpClientFactory>();
        var bot = new MyBot(loggerMock.Object, httpClientFactoryMock.Object, sentimentAnalysisMock.Object);
        var userId = "testUser";
        var text = "Hello, how are you?";

        // Act
        var response = await bot.GenerateResponse(text, userId);

        // Assert
        Assert.NotNull(response);
        Assert.Contains("You are a helpful assistant.", response);
    }
}