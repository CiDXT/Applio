import gradio as gr
import os
import pytube


def convert_yt_to_wav(url):
    if not url:
        return "First, introduce the video link", None
    
    try:
        print(f"Converting video {url}...")
        # Descargar el video utilizando pytube
        video = pytube.YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        video_output_folder = os.path.join(f"yt_videos")  # Ruta de destino de la carpeta
        audio_output_folder = 'assets/audios'

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
        return "The connection has been lost, please reload or try again later.", None
    except Exception as e:
        return str(e), None



      with gr.TabItem("Youtube"):
        gr.Markdown("## Convertir video de Youtube a audio")
        with gr.Row():
            yt_url = gr.Textbox(
                label="Url del video:",
                placeholder="https://www.youtube.com/watch?v=3vEiqil5d3Q"
            )
        yt_btn = gr.Button(value="Convertir")
                
        with gr.Row():
            yt_output1 = gr.Textbox(label="Salida")
            yt_output2 = gr.Audio(label="Audio de salida")   
            
        yt_btn.click(fn=convert_yt_to_wav, inputs=[yt_url], outputs=[yt_output1, yt_output2])
