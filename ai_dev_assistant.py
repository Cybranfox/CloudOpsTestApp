#!/usr/bin/env python3
"""
AI-Powered Development Assistant for AWS Cloud Orbit
Integrates with OpenAI/Anthropic APIs for automated code improvements
"""

import json
import os
import subprocess
from datetime import datetime
from typing import Any, Dict, List

import requests


class AIDevAssistant:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.repo_owner = "Cybranfox"
        self.repo_name = "CloudOpsTestApp"

    def analyze_codebase(self) -> Dict[str, Any]:
        """Analyze the current codebase and return insights"""
        analysis = {
            "files_analyzed": [],
            "issues_found": [],
            "suggestions": [],
            "metrics": {},
        }

        # Analyze Python files
        python_files = (
            subprocess.run(
                ["find", ".", "-name", "*.py", "-type", "f"],
                capture_output=True,
                text=True,
            )
            .stdout.strip()
            .split("\n")
        )

        for py_file in python_files:
            if py_file and os.path.exists(py_file):
                analysis["files_analyzed"].append(py_file)

                # Read file content
                with open(py_file, "r") as f:
                    content = f.read()

                # Basic analysis
                lines = len(content.split("\n"))
                analysis["metrics"][py_file] = {
                    "lines": lines,
                    "functions": content.count("def "),
                    "classes": content.count("class "),
                }

        return analysis

    def get_ai_suggestions(self, code_content: str) -> List[str]:
        """Get AI-powered suggestions for code improvement"""
        if not self.openai_api_key:
            return ["AI API key not configured"]

        prompt = f"""
        Analyze this Flask application code and provide specific, actionable improvements:
        
        ```python
        {code_content[:2000]}
        ```
        
        Focus on:
        1. Bug fixes and error handling
        2. Performance optimizations
        3. Security improvements
        4. Mobile UX enhancements
        5. Code quality improvements
        
        Provide exactly 5 specific suggestions in this format:
        - [CATEGORY] Brief description of improvement
        """

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.openai_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4",
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an expert Python/Flask developer focused on mobile app development.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": 500,
                    "temperature": 0.3,
                },
            )

            if response.status_code == 200:
                result = response.json()
                suggestions = result["choices"][0]["message"]["content"]
                return [
                    s.strip()
                    for s in suggestions.split("\n")
                    if s.strip().startswith("-")
                ]
            else:
                return [f"AI API error: {response.status_code}"]

        except Exception as e:
            return [f"AI integration error: {str(e)}"]

    def create_github_issue(self, title: str, body: str, labels: List[str]) -> bool:
        """Create a GitHub issue with AI suggestions"""
        if not self.github_token:
            print("GitHub token not configured")
            return False

        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues"

        data = {"title": title, "body": body, "labels": labels}

        try:
            response = requests.post(
                url,
                headers={
                    "Authorization": f"token {self.github_token}",
                    "Accept": "application/vnd.github.v3+json",
                },
                json=data,
            )

            if response.status_code == 201:
                issue_url = response.json()["html_url"]
                print(f"✅ Created issue: {issue_url}")
                return True
            else:
                print(f"❌ Failed to create issue: {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ Error creating issue: {str(e)}")
            return False

    def run_automated_improvements(self):
        """Run the full AI-powered improvement cycle"""
        print("🤖 Starting AI-powered development cycle...")

        # 1. Analyze codebase
        print("🔍 Analyzing codebase...")
        analysis = self.analyze_codebase()

        # 2. Get AI suggestions for main files
        if "app.py" in analysis["files_analyzed"]:
            with open("app.py", "r") as f:
                app_content = f.read()

            print("🧠 Getting AI suggestions...")
            suggestions = self.get_ai_suggestions(app_content)

            # 3. Create GitHub issues for suggestions
            for i, suggestion in enumerate(suggestions[:3]):  # Limit to 3 issues
                issue_title = f"🤖 AI Suggestion #{i+1}: {suggestion[:50]}..."
                issue_body = f"""
**AI-Generated Improvement Suggestion**

{suggestion}

**Context:**
- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- File analyzed: app.py
- Priority: Medium

**Next Steps:**
1. Review the suggestion
2. Implement if beneficial
3. Test thoroughly
4. Close this issue when complete

*This issue was automatically generated by the AI Development Assistant*
                """

                labels = ["ai-generated", "enhancement", "needs-review"]
                self.create_github_issue(issue_title, issue_body, labels)

        # 4. Generate development report
        report = f"""
# 🤖 AI Development Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Analysis Summary
- Files analyzed: {len(analysis['files_analyzed'])}
- Total Python files: {len([f for f in analysis['files_analyzed'] if f.endswith('.py')])}
- Issues created: {len(suggestions[:3])}

## 🎯 Automated Actions Taken
- ✅ Codebase analysis completed
- ✅ AI suggestions generated
- ✅ GitHub issues created
- ✅ Development report generated

## 📱 Next Recommended Steps
1. Review AI-generated issues in GitHub
2. Test current APK build process
3. Update mobile UI based on suggestions
4. Run full test suite

## 🔧 Code Metrics
"""

        for file_path, metrics in analysis["metrics"].items():
            report += f"- {file_path}: {metrics['lines']} lines, {metrics['functions']} functions\n"

        # Save report
        with open("AI_DEVELOPMENT_REPORT.md", "w") as f:
            f.write(report)

        print("✅ AI development cycle completed!")
        print("📄 Report saved to AI_DEVELOPMENT_REPORT.md")


if __name__ == "__main__":
    assistant = AIDevAssistant()
    assistant.run_automated_improvements()
