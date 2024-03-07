
import gradio as gr
import os
import subprocess
from IPython.display import Audio

def get_video_title(url):
 def convert_yt_to_wav(url):
    if not url:
        return "Primero introduce el enlace del video", None
    
    try:
        print(f"converting video {url}...")
        # Descargar el video utilizando pytube
        video = pytube.YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        video_output_folder = os.path.join(f"yt_videos")  # Ruta de destino de la carpeta
        audio_output_folder = 'audios'

        print("Downloading video")
        video_file_path = stream.download(output_path=video_output_folder)
        print(video_file_path)

        file_name = os.path.basename(video_file_path)
        
        audio_file_path = os.path.join(audio_output_folder, file_name.replace('.mp4','.wav'))
        # convert mp4 to wav
        print("Converting to wav")
        sound = AudioSegment.from_file(video_file_path,format="mp4")
        sound.export(audio_file_path, format="wav")
        
        if os.path.exists(video_file_path):
            os.remove(video_file_path)
            
        return "Success", audio_file_path
    except ConnectionResetError as cre:
        return "Connection has been lost, recharge or try again later.", None
    except Exception as e:
        return str(e), None


def pytube():
    with gr.Column():
        gr.Markdown(
            "Tool inspired in the original [SimpleRVC](https://huggingface.co/spaces/juuxn/SimpleRVC) code."
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
                vc_output1 = gr.Textbox(label="information")
                vc_output2 = gr.Audio(label="audio output")
    command.click(
        fn=fetch,
        inputs=[url, custom_name],
        outputs=[result],
    )
