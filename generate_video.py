import os
from moviepy.editor import TextClip, CompositeVideoClip

def generate_reel(prompt):
    txt_clip = TextClip(prompt, fontsize=70, color='white', size=(1080, 1920))
    txt_clip = txt_clip.set_duration(5)
    final_clip = CompositeVideoClip([txt_clip])
    output_path = f"{prompt[:10].replace(' ', '_')}_reel.mp4"
    final_clip.write_videofile(output_path, fps=24)
    return output_path