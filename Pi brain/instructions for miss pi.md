// Define URLs
Set(
    urls,
    {
        docs: "https://api.example.com/docs?search=" & data,
        learn: "https://api.example.com/learn?topic=" & data,
        codeGen: {
            python: "def function_name(params):\n    # code here",
            java: "public class ClassName {\n    public void methodName() {\n        // code here\n    }\n}"
        },
        project: "https://api.example.com/projects",
        versionControl: "https://api.github.com/repos/" & data & "/commits",
        ci: "https://api.ci.example.com/pipelines",
        coverage: "https://api.coverage.example.com/repos/" & data & "/coverage",
        analysis: "https://api.sonar.example.com/analysis"
    }
);

// Define tasks
Switch(
    task,
    "codeAssist",
    // Code assistance logic (Power Fx doesn't support ESLint directly)
    Notify("Code assistance is not directly supported in Power Fx.", NotificationType.Error),

    "fetchDocs",
    // Fetch documentation (use Power Automate for actual HTTP request)
    Notify("Fetching documentation from " & urls.docs, NotificationType.Information),

    "generateCode",
    // Generate code snippet
    If(
        data = "python",
        Notify("Generating Python code snippet:\n" & urls.codeGen.python, NotificationType.Information),
        If(
            data = "java",
            Notify("Generating Java code snippet:\n" & urls.codeGen.java, NotificationType.Information),
            Notify("Invalid language", NotificationType.Error)
        )
    ),

    "learnResources",
    // Fetch learning resources (use Power Automate for actual HTTP request)
    Notify("Fetching learning resources from " & urls.learn, NotificationType.Information),

    "manageProject",
    // Manage project (use Power Automate for actual HTTP request)
    Notify("Managing project at " & urls.project, NotificationType.Information),

    "versionControl",
    // Fetch version control data (use Power Automate for actual HTTP request)
    Notify("Fetching version control data from " & urls.versionControl, NotificationType.Information),

    "setupCI",
    // Setup CI (use Power Automate for actual HTTP request)
    Notify("Setting up CI at " & urls.ci, NotificationType.Information),

    "codeCoverage",
    // Fetch code coverage data (use Power Automate for actual HTTP request)
    Notify("Fetching code coverage data from " & urls.coverage, NotificationType.Information),

    "staticAnalysis",
    // Perform static analysis (use Power Automate for actual HTTP request)
    Notify("Performing static analysis at " & urls.analysis, NotificationType.Information),

    // Default case
    Notify("Invalid Task", NotificationType.Error)
)