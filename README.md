# RapidHTTP

RapidHTTP 是一个简单、高效的 Python HTTP 服务器。

## 特性

- 快速、高效的处理 HTTP 请求
- 支持静态文件服务
- 多线程处理请求
- 简单易用的 API

## 使用方法

1. 安装 Python 3.x （如果尚未安装）。
2. 下载或克隆 RapidHTTP 代码库。
3. 在命令行中进入 RapidHTTP 代码库的根目录。
4. 运行以下命令安装依赖项：

   ```
   pip install -r requirements.txt
   ```

5. 将你的静态文件放置在 RapidHTTP 代码库的根目录或子目录中。
6. 运行以下命令启动 RapidHTTP 服务器：

   ```
   python server.py
   ```

7. 访问 http://localhost:8000/ 以查看默认页面。

## 自定义配置

你可以根据需要自定义 RapidHTTP 服务器的配置。以下是一些可以自定义的选项：

- 修改 `server.py` 中的 `PORT` 变量以更改服务器监听的端口号。
- 自定义 `server.py` 中的 `SimpleHTTPRequestHandler` 类以满足你的需求，如添加其他处理函数或修改默认页面。

## 贡献

如果你发现了问题或有改进的建议，请随时提出 issue 或提交 pull 请求。我们欢迎并感谢你的贡献！

## 授权

本项目基于 MIT 授权许可进行发布。请查阅 [LICENSE](LICENSE) 文件以获取更多信息。

## 作者

RapidHTTP 由 [wiw](https://wolan.me) 开发和维护。

## 链接

- GitHub 代码库：[https://github.com/RapidHTTP/main/](https://github.com/RapidHTTP/main/))
