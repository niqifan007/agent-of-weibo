# Weibo Crew

欢迎来到由 [crewAI](https://crewai.com) 提供支持的微博 Crew 项目。该模板旨在帮助您利用crewAI提供的强大而灵活的框架轻松设置多代理人工智能系统。我们的目标是使您的代理能够有效地协作完成复杂的任务，最大限度地发挥他们的集体智慧和能力。

## Installation


```bash
pip install poetry
```

接下来，导航到您的项目目录并安装依赖项：

1. 首先锁定依赖项，然后安装它们：
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- 修改 `src/weibo/config/agents.yaml` 来定义您的代理
- 修改`src/weibo/config/tasks.yaml`来定义您的任务
- 修改 `src/weibo/crew.py` 添加您自己的逻辑、工具和特定参数
- 修改 `src/weibo/main.py` 为您的代理和任务添加自定义输入

## Running the Project

要启动您的 AI 代理团队并开始执行任务，请从项目的根文件夹运行以下命令：

```bash
poetry run weibo
```

此命令初始化 weibo Crew，组装代理并按照您的配置中定义的方式为它们分配任务。

此示例未经修改，将运行创建一个“report.md”文件，其中包含根文件夹中 LLM 研究的输出

## Understanding Your Crew

微博Crew由多个AI代理组成，每个代理都有独特的角色、目标和工具。这些代理协作执行“config/tasks.yaml”中定义的一系列任务，利用他们的集体技能来实现复杂的目标。 `config/agents.yaml` 文件概述了团队中每个代理的功能和配置。