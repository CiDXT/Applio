
import gradio as gr
import os
import subprocess
from IPython.display import Audio

def get_video_title(url):
    # 使用 yt-dlp 获取视频标题
    result = subprocess.run(["yt-dlp", "--get-title", url], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return "Unknown Video"

def fetch(url, custom_name, ext):
    title = get_video_title(url)
    # 截断标题为一个合理的长度
    max_length = 50  # 调整为适当的值
    truncated_title = title[:max_length].strip()
    
    filename = f"{custom_name}.{ext}" if custom_name else f"{truncated_title}.{ext}"
    opts = {
        "wav": ["-f", "ba", "-x", "--audio-format", "wav"],
    }[ext]
    command = ["yt-dlp"] + opts + [url, "-o", filename]
    subprocess.run(command)

    return filename



def yt_dlp():
    with gr.Column():
        gr.Markdown(
            "Tool inspired in the original [youtube_downloader](https://huggingface.co/spaces/Hev832/youtube_downloader) code."
        )
        url = gr.Textbox(label="Url  video:", placeholder="https://youtu.be/iN0-dRNsmRM?si=42PgawH73GIrvYLs")
        custom_name = gr.Textbox(label="file name:", placeholder="Defaults to video title")
        ext = gr.Button(value="Convert")
    with gr.Column():
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    value=("download youtube audio acapella"),
                    visible=True,
                )
                
                result = gr.Audio(label="audio output")
    fetch.click(
        fn=fetch,
        inputs=[url, custom_name],
        outputs=[result],
    )
